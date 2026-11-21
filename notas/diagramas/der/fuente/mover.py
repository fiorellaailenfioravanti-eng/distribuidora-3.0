import re, sys
def aplicar(archivo, ents={}, rels={}, reemplazos=()):
    s = open(archivo, encoding='utf-8').read()
    for k, (x, y) in ents.items():
        s, n = re.subn(rf"E\('{k}', \d+, \d+,", f"E('{k}', {x}, {y},", s); assert n == 1, k
    for k, (x, y) in rels.items():
        s, n = re.subn(rf"(R\('{k}',[^\n]*?\)\], )\d+, \d+", rf"\g<1>{x}, {y}", s); assert n == 1, k
    for a, b in reemplazos:
        assert a in s, a; s = s.replace(a, b)
    open(archivo, 'w', encoding='utf-8').write(s)
