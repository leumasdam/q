# -*- coding: utf-8 -*-
"""Vyrobí QR kódy pre všetky kódy z links.json do priečinka qr/ (PNG na tlač + SVG).

    python make_qr.py            # všetky
    python make_qr.py krojarka   # len jeden

QR obsahuje len krátku adresu https://leumasdam.github.io/q/<kód>.
Cieľ sa mení v links.json (commit + push), QR netreba znova tlačiť.
"""
import json, os, sys
import qrcode, qrcode.image.svg
BASE = 'https://leumasdam.github.io/q/'
os.makedirs('qr', exist_ok=True)
links = json.load(open('links.json', encoding='utf-8'))
for code in (sys.argv[1:] or links):
    url = BASE + code
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=2)
    q.add_data(url); q.make(fit=True)
    q.make_image(fill_color='#181614', back_color='white').save(f'qr/{code}.png')
    q.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(f'qr/{code}.svg')
    print(code, '→', url, '→', links.get(code))
