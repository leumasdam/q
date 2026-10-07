# Dynamické QR kódy (zadarmo)

QR vedie na `https://leumasdam.github.io/q/<kód>`; cieľ je v `links.json`.

- **Zmeniť cieľ:** uprav adresu v `links.json` (aj priamo na GitHube cez ceruzku) a ulož. Do minúty platí, QR netreba tlačiť znova.
- **Nový QR:** pridaj riadok `"kod": "https://..."` do `links.json`, potom `python make_qr.py kod` → `qr/kod.png` a `qr/kod.svg`.

- **Štatistiky:** https://leumasdam.github.io/q/stats.html (počet naskenovaní celkovo a po dňoch; počítadlo Abacus, zadarmo, bez účtu).
