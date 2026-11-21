# -*- coding: utf-8 -*-
"""python render.py <modulo> [--forzar]: verifica, escribe SVG y PNG."""
import importlib, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
AQUI = os.path.dirname(os.path.abspath(__file__))

nombre = sys.argv[1]
d = importlib.import_module(nombre).DIAGRAMA
prob = d.verificar()
print('\n'.join(prob) or 'sin problemas')
if prob and '--forzar' not in sys.argv:
    sys.exit(1)
svg = os.path.join(AQUI, nombre + '.svg')
open(svg, 'w', encoding='utf-8').write(d.svg())
html = os.path.join(AQUI, nombre + '.html')
open(html, 'w', encoding='utf-8').write('<!doctype html><meta charset="utf-8"><style>html,body{margin:0}</style>' + d.svg())
png = os.path.join(AQUI, nombre + '.png')
subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=2',
                f'--window-size={d.W},{d.H}', f'--screenshot={png}', 'file:///' + html.replace('\\', '/')],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
print('png', os.path.getsize(png))
