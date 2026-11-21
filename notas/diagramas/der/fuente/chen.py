# -*- coding: utf-8 -*-
"""Motor mínimo para dibujar diagramas Entidad-Relación en notación de Chen (SVG).

Entidad:   E(id, x, y, nombre, attrs=[A(...)], debil=False, ref=False, arco=(a0, a1), r=95)
Relación:  R(id, nombre, [(entidad, '(min,max)'), ...], x, y, card='1:N', ident=False, attrs=[], arco=, r=)
Atributo:  A(nombre, tipo, clase) — clase: clave | parcial | simple | derivado | multivaluado | compuesto(sub=[A...])
Especialización: ESP(superclase, [subclases], x, y, letra='o'|'d', total=False)

Los ángulos van en grados (0 = derecha, 90 = abajo). Los atributos se reparten
en el arco indicado alrededor de su dueño.
"""
import math
from html import escape as e

FUENTE = 'Segoe UI, Arial, sans-serif'


class A:
    def __init__(self, nombre, tipo='', clase='simple', sub=None):
        self.nombre, self.tipo, self.clase, self.sub = nombre, tipo, clase, sub or []


class E:
    def __init__(self, id, x, y, nombre, attrs=(), debil=False, ref=False, arco=(0, 360), r=95, rx=None):
        self.id, self.x, self.y, self.nombre = id, x, y, nombre
        self.attrs, self.debil, self.ref, self.arco, self.r, self.rx = list(attrs), debil, ref, arco, r, rx
        self.w = max(120, len(nombre) * 9 + 30)
        self.h = 44


class R:
    def __init__(self, id, nombre, extremos, x, y, card='', ident=False, attrs=(), arco=(0, 360), r=80, rx=None):
        self.id, self.nombre, self.extremos, self.x, self.y = id, nombre, extremos, x, y
        self.card, self.ident, self.attrs, self.arco, self.r, self.rx = card, ident, list(attrs), arco, r, rx
        self.w = max(104, len(nombre) * 8.2 + 44)
        self.h = 58


class ESP:
    def __init__(self, sup, subs, x, y, letra='o', total=False):
        self.sup, self.subs, self.x, self.y, self.letra, self.total = sup, subs, x, y, letra, total


def tam_ovalo(a):
    ancho = max(len(a.nombre) * 7.0, len(a.tipo) * 6.0) + 26
    return max(ancho, 70), (36 if a.tipo else 26)


def borde_rect(cx, cy, w, h, tx, ty):
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    t = min((w / 2) / abs(dx) if dx else 9e9, (h / 2) / abs(dy) if dy else 9e9)
    return cx + dx * t, cy + dy * t


def borde_rombo(cx, cy, w, h, tx, ty):
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    t = 1 / (abs(dx) / (w / 2) + abs(dy) / (h / 2))
    return cx + dx * t, cy + dy * t


def borde_elipse(cx, cy, rx, ry, tx, ty):
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    t = 1 / math.sqrt((dx / rx) ** 2 + (dy / ry) ** 2)
    return cx + dx * t, cy + dy * t


class Diagrama:
    def __init__(self, titulo, ancho, alto, entidades, relaciones, esp=(), nota=''):
        self.titulo, self.W, self.H, self.nota = titulo, ancho, alto, nota
        self.ent = {x.id: x for x in entidades}
        self.rel = list(relaciones)
        self.esp = list(esp)
        self.ovalos = []   # (cx, cy, w, h, A, dueño_xy)
        self._ubicar_atributos()
        self._ajustar_lienzo()

    def _ajustar_lienzo(self, margen=40, arriba=80, abajo=50):
        """Corre todo para que el contenido arranque bajo el título y achica el lienzo."""
        xs, ys = [], []
        for x in self.ent.values():
            xs += [x.x - x.w / 2, x.x + x.w / 2]; ys += [x.y - x.h / 2, x.y + x.h / 2]
        for x in self.rel:
            xs += [x.x - x.w / 2, x.x + x.w / 2]; ys += [x.y - x.h / 2, x.y + x.h / 2]
        for ox, oy, w, h, *_ in self.ovalos:
            xs += [ox - w / 2, ox + w / 2]; ys += [oy - h / 2, oy + h / 2]
        dx, dy = margen - min(xs), arriba - min(ys)
        for x in list(self.ent.values()) + self.rel + self.esp:
            x.x += dx; x.y += dy
        self.ovalos = []
        self._ubicar_atributos()
        self.W = int(max(max(xs) + dx + margen, len(self.titulo) * 12 + 80))
        self.H = int(max(ys) + dy + abajo)

    # ── ubicación de atributos ──
    def _repartir(self, dueno, cx, cy, attrs, arco, r, rx):
        if not attrs:
            return
        arcos = arco if isinstance(arco[0], (tuple, list)) else [arco]
        n = len(attrs)
        rx = rx or r * 1.75
        # ángulos: se reparten los atributos entre los arcos según su largo
        fijos = sum(t[2] for t in arcos if len(t) == 3)
        total = sum(abs(t[1] - t[0]) for t in arcos if len(t) == 2) or 1
        angulos, resto = [], n
        for k, t in enumerate(arcos):
            a, b = t[0], t[1]
            if len(t) == 3:
                m = t[2]
            else:
                m = resto if k == len(arcos) - 1 else round((n - fijos) * abs(b - a) / total)
            m = min(m, resto)
            resto -= m
            if m == 0:
                continue
            if abs(b - a) >= 360:
                angulos += [a + (b - a) * (i + 0.5) / m for i in range(m)]
            else:
                angulos += [a + (b - a) * (i / (m - 1) if m > 1 else 0.5) for i in range(m)]
        # el radio crece hasta que los óvalos del mismo dueño no se pisen
        esc = 1.0
        while True:
            pos = []
            for i, (at, grados) in enumerate(zip(attrs, angulos)):
                ang = math.radians(grados)
                w, h = tam_ovalo(at)
                # con muchos atributos se alternan dos radios para que entren más cerca
                f = esc * (1.45 if (n >= 5 and i % 2) else 1.0)
                pos.append((cx + math.cos(ang) * rx * f, cy + math.sin(ang) * r * f, w, h))
            choque = any(abs(a[0] - b[0]) < (a[2] + b[2]) / 2 + 8 and abs(a[1] - b[1]) < (a[3] + b[3]) / 2 + 6
                         for i, a in enumerate(pos) for b in pos[i + 1:])
            if not choque:
                # la línea hacia cada óvalo no debe atravesar los demás óvalos del mismo dueño
                for i, a in enumerate(pos):
                    for j, b in enumerate(pos):
                        if i == j:
                            continue
                        for k in range(10, 95, 4):
                            t = k / 100
                            x, y = cx + (a[0] - cx) * t, cy + (a[1] - cy) * t
                            if ((x - b[0]) / (b[2] / 2 + 4)) ** 2 + ((y - b[1]) / (b[3] / 2 + 4)) ** 2 < 1:
                                choque = True
                                break
                        if choque:
                            break
                    if choque:
                        break
            if not choque or esc > 3:
                break
            esc += 0.05
        for at, grados, (ox, oy, w, h) in zip(attrs, angulos, pos):
            ang = math.radians(grados)
            self.ovalos.append((ox, oy, w, h, at, (cx, cy), dueno))
            # subatributos de un compuesto: más afuera, en la misma dirección
            k = len(at.sub)
            ux, uy = math.cos(ang), math.sin(ang)
            px, py = -uy, ux  # perpendicular
            for j, sub in enumerate(at.sub):
                sw, sh = tam_ovalo(sub)
                # se apilan en perpendicular a la dirección del compuesto
                paso = abs(px) * (sw + 14) + abs(py) * (sh + 12)
                desp = (j - (k - 1) / 2) * paso
                avance = abs(ux) * (w / 2 + sw / 2 + 40) + abs(uy) * (h / 2 + sh / 2 + 34)
                sx = ox + ux * avance + px * desp
                sy = oy + uy * avance + py * desp
                self.ovalos.append((sx, sy, sw, sh, sub, (ox, oy), at))

    def _ubicar_atributos(self):
        for x in self.ent.values():
            self._repartir(x, x.x, x.y, x.attrs, x.arco, x.r, x.rx)
        for x in self.rel:
            self._repartir(x, x.x, x.y, x.attrs, x.arco, x.r, x.rx)

    # ── geometría de las líneas ──
    def _lineas_relacion(self):
        """(p, q, rel, entidad, cardinalidad, doble)"""
        res = []
        for rel in self.rel:
            vistos = {}
            for ent_id, card in rel.extremos:
                ent = self.ent[ent_id]
                k = vistos.get(ent_id, 0)
                vistos[ent_id] = k + 1
                off = 0 if [i for i, _ in rel.extremos].count(ent_id) == 1 else (-14 if k == 0 else 14)
                # en autorrelaciones se separan las dos líneas
                ex, ey = ent.x + (off if abs(rel.y - ent.y) > abs(rel.x - ent.x) else 0), ent.y + (off if abs(rel.y - ent.y) <= abs(rel.x - ent.x) else 0)
                rx_, ry_ = rel.x + (off if abs(rel.y - ent.y) > abs(rel.x - ent.x) else 0), rel.y + (off if abs(rel.y - ent.y) <= abs(rel.x - ent.x) else 0)
                p = borde_rect(ent.x, ent.y, ent.w + (8 if ent.debil else 0), ent.h + (8 if ent.debil else 0), rx_, ry_)
                if off:
                    p = (p[0] + (off if abs(rel.y - ent.y) > abs(rel.x - ent.x) else 0), p[1] + (off if abs(rel.y - ent.y) <= abs(rel.x - ent.x) else 0))
                q = borde_rombo(rel.x, rel.y, rel.w, rel.h, ex, ey)
                if off:
                    q = borde_rombo(rel.x, rel.y, rel.w, rel.h, p[0], p[1])
                res.append((p, q, rel, ent, card, rel.ident and ent.debil))
        return res

    def _lineas_atributo(self):
        res = []
        for ox, oy, w, h, at, (dx, dy), dueno in self.ovalos:
            q = borde_elipse(ox, oy, w / 2, h / 2, dx, dy)
            if isinstance(dueno, E):
                p = borde_rect(dx, dy, dueno.w, dueno.h, ox, oy)
            elif isinstance(dueno, R):
                p = borde_rombo(dx, dy, dueno.w, dueno.h, ox, oy)
            else:  # subatributo: sale del óvalo padre
                pw, ph = tam_ovalo(dueno)
                p = borde_elipse(dx, dy, pw / 2, ph / 2, ox, oy)
            res.append((p, q, (ox, oy), dueno))
        return res

    # ── verificación ──
    def verificar(self):
        cajas = []  # (nombre, cx, cy, w, h, tipo)
        for x in self.ent.values():
            cajas.append((x.id, x.x, x.y, x.w + 10, x.h + 10, 'rect'))
        for x in self.rel:
            cajas.append((x.id, x.x, x.y, x.w + 6, x.h + 6, 'rombo'))
        for ox, oy, w, h, at, _, dueno in self.ovalos:
            cajas.append((f'{getattr(dueno, "id", getattr(dueno, "nombre", "?"))}.{at.nombre}', ox, oy, w + 8, h + 6, 'ovalo'))
        cajas.append(('__titulo', self.W / 2, 34, len(self.titulo) * 11 + 40, 40, 'rect'))
        prob = []
        for i, a in enumerate(cajas):
            if a[1] - a[3] / 2 < 4 or a[1] + a[3] / 2 > self.W - 4 or a[2] - a[4] / 2 < 4 or a[2] + a[4] / 2 > self.H - 4:
                prob.append(f'fuera del lienzo: {a[0]}')
            for b in cajas[i + 1:]:
                if abs(a[1] - b[1]) < (a[3] + b[3]) / 2 and abs(a[2] - b[2]) < (a[4] + b[4]) / 2:
                    prob.append(f'superposición: {a[0]} / {b[0]}')

        def dentro(x, y, c):
            _, cx, cy, w, h, tipo = c
            if tipo == 'ovalo':
                return ((x - cx) / (w / 2)) ** 2 + ((y - cy) / (h / 2)) ** 2 < 1
            if tipo == 'rombo':
                return abs(x - cx) / (w / 2) + abs(y - cy) / (h / 2) < 1
            return abs(x - cx) < w / 2 and abs(y - cy) < h / 2

        segs = [(p, q, f'rel {r.id}-{en.id}', {r.id, en.id}) for p, q, r, en, _, _ in self._lineas_relacion()]
        for (p, q, (ox, oy), d), ov in zip(self._lineas_atributo(), self.ovalos):
            dueno = getattr(d, 'id', getattr(d, 'nombre', '?'))
            propio = f'{getattr(ov[6], "id", getattr(ov[6], "nombre", "?"))}.{ov[4].nombre}'
            padre = None
            if isinstance(d, A):  # subatributo: el padre es un óvalo
                padre = next((f'{getattr(o[6], "id", "?")}.{o[4].nombre}' for o in self.ovalos if o[4] is d), None)
            segs.append((p, q, f'attr {dueno}', {dueno, propio, padre}))
        for p, q, nombre, ignorar in segs:
            for c in cajas:
                if c[0] in ignorar:
                    continue
                for k in range(3, 98):
                    t = k / 100
                    x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
                    if dentro(x, y, c):
                        # tocar la propia figura en los extremos es normal
                        if (t < .08 or t > .92):
                            continue
                        prob.append(f'{nombre} cruza {c[0]}')
                        break
        return sorted(set(prob))

    # ── dibujo ──
    def svg(self):
        s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" width="{self.W}" height="{self.H}" font-family="{FUENTE}">',
             '<style>.l{stroke:#1f2937;stroke-width:1.3;fill:none}.ent{fill:#dbeafe;stroke:#1e3a8a;stroke-width:1.6}'
             '.ref{fill:#f1f5f9;stroke:#64748b;stroke-width:1.4;stroke-dasharray:5 3}'
             '.rel{fill:#fef3c7;stroke:#92400e;stroke-width:1.5}.ov{fill:#fff;stroke:#334155;stroke-width:1.2}'
             '.tn{font-size:14px;font-weight:700;fill:#0f172a}.rn{font-size:12.5px;font-weight:600;fill:#78350f}'
             '.an{font-size:11.5px;fill:#0f172a}.at{font-size:9.5px;fill:#64748b;font-style:italic}'
             '.cd{font-size:11.5px;font-weight:700;fill:#b91c1c}.cr{font-size:10.5px;fill:#92400e;font-weight:600}'
             '.tt{font-size:22px;font-weight:700;fill:#0f172a}.nt{font-size:12px;fill:#475569}</style>',
             f'<rect width="{self.W}" height="{self.H}" fill="#fff"/>',
             f'<text x="{self.W/2}" y="40" text-anchor="middle" class="tt">{e(self.titulo)}</text>']
        if self.nota:
            s.append(f'<text x="{self.W/2}" y="{self.H-14}" text-anchor="middle" class="nt">{e(self.nota)}</text>')
        # líneas de atributos
        for p, q, _, _ in self._lineas_atributo():
            s.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" class="l"/>')
        # líneas de relaciones (+ cardinalidad junto a la entidad)
        for p, q, rel, ent, card, doble in self._lineas_relacion():
            if doble:
                s.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="#1f2937" stroke-width="5"/>'
                         f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="#fff" stroke-width="2.4"/>')
            else:
                s.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" class="l"/>')
            if card:
                L = math.hypot(q[0] - p[0], q[1] - p[1]) or 1
                ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L
                d = min(30, L * 0.3)
                nx, ny = -uy, ux
                if ny > 0 or (abs(ny) < 1e-6 and nx < 0):
                    nx, ny = -nx, -ny
                cx, cy = p[0] + ux * d + nx * 10, p[1] + uy * d + ny * 10
                ancla = 'middle' if abs(nx) < .5 else ('start' if nx > 0 else 'end')
                s.append(f'<text x="{cx:.1f}" y="{cy+4:.1f}" text-anchor="{ancla}" class="cd" paint-order="stroke" stroke="#fff" stroke-width="3">{card}</text>')
        # especializaciones
        for sp in self.esp:
            sup = self.ent[sp.sup]
            p = borde_rect(sup.x, sup.y, sup.w, sup.h, sp.x, sp.y)
            q = borde_elipse(sp.x, sp.y, 15, 15, sup.x, sup.y)
            if sp.total:
                for dx in (-2.5, 2.5):
                    s.append(f'<line x1="{p[0]+dx:.1f}" y1="{p[1]:.1f}" x2="{q[0]+dx:.1f}" y2="{q[1]:.1f}" class="l"/>')
            else:
                s.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" class="l"/>')
            for sub_id in sp.subs:
                sub = self.ent[sub_id]
                a = borde_elipse(sp.x, sp.y, 15, 15, sub.x, sub.y)
                b = borde_rect(sub.x, sub.y, sub.w, sub.h, sp.x, sp.y)
                s.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" class="l"/>')
                mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
                ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
                s.append(f'<path d="M -7 -8 A 8 8 0 0 0 -7 8" class="l" stroke-width="1.8" transform="translate({mx:.1f},{my:.1f}) rotate({ang:.1f})"/>')
            s.append(f'<circle cx="{sp.x}" cy="{sp.y}" r="15" fill="#fff" stroke="#1f2937" stroke-width="1.4"/>'
                     f'<text x="{sp.x}" y="{sp.y+5}" text-anchor="middle" class="tn">{sp.letra}</text>')
        # relaciones
        for rel in self.rel:
            x, y, w, h = rel.x, rel.y, rel.w, rel.h
            pts = f'{x},{y-h/2} {x+w/2},{y} {x},{y+h/2} {x-w/2},{y}'
            s.append(f'<polygon points="{pts}" class="rel"/>')
            if rel.ident:
                pts2 = f'{x},{y-h/2+6} {x+w/2-11},{y} {x},{y+h/2-6} {x-w/2+11},{y}'
                s.append(f'<polygon points="{pts2}" class="rel"/>')
            yn = y + (0 if not rel.card else -3)
            s.append(f'<text x="{x}" y="{yn+1:.1f}" text-anchor="middle" class="rn">{e(rel.nombre)}</text>')
            if rel.card:
                s.append(f'<text x="{x}" y="{y+15:.1f}" text-anchor="middle" class="cr">{e(rel.card)}</text>')
        # entidades
        for ent in self.ent.values():
            x0, y0 = ent.x - ent.w / 2, ent.y - ent.h / 2
            clase = 'ref' if ent.ref else 'ent'
            if ent.debil:
                s.append(f'<rect x="{x0-4}" y="{y0-4}" width="{ent.w+8}" height="{ent.h+8}" class="{clase}"/>')
            s.append(f'<rect x="{x0}" y="{y0}" width="{ent.w}" height="{ent.h}" class="{clase}"/>')
            s.append(f'<text x="{ent.x}" y="{ent.y+5}" text-anchor="middle" class="tn">{e(ent.nombre)}</text>')
        # atributos
        for ox, oy, w, h, at, _, _ in self.ovalos:
            punteado = ' stroke-dasharray="4 3"' if at.clase == 'derivado' else ''
            s.append(f'<ellipse cx="{ox:.1f}" cy="{oy:.1f}" rx="{w/2:.1f}" ry="{h/2:.1f}" class="ov"{punteado}/>')
            if at.clase == 'multivaluado':
                s.append(f'<ellipse cx="{ox:.1f}" cy="{oy:.1f}" rx="{w/2-4:.1f}" ry="{h/2-4:.1f}" class="ov"/>')
            ty = oy + (-2 if at.tipo else 4)
            deco = ''
            if at.clase == 'clave':
                deco = ' text-decoration="underline"'
            s.append(f'<text x="{ox:.1f}" y="{ty:.1f}" text-anchor="middle" class="an"{deco}>{e(at.nombre)}</text>')
            if at.clase == 'parcial':
                ancho = len(at.nombre) * 6.2
                s.append(f'<line x1="{ox-ancho/2:.1f}" y1="{ty+3:.1f}" x2="{ox+ancho/2:.1f}" y2="{ty+3:.1f}" stroke="#0f172a" stroke-dasharray="3 2"/>')
            if at.tipo:
                s.append(f'<text x="{ox:.1f}" y="{oy+11:.1f}" text-anchor="middle" class="at">{e(at.tipo)}</text>')
        s.append('</svg>')
        return '\n'.join(s)
