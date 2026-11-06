"""Ricompone mappa-sedi.js dai file in sorgente/.

La pagina mappa-interattiva carica solo mappa-sedi.js da jsDelivr: cosi' per
aggiornare la mappa basta pubblicare qui, senza toccare il widget di Elementor.
"""
import json
import pathlib

QUI = pathlib.Path(__file__).parent
S = QUI / "sorgente"

stile = (S / "stile.css").read_text(encoding="utf-8")
pagina = (S / "pagina.html").read_text(encoding="utf-8").strip()
leaflet = (S / "leaflet-1.9.4.js").read_text(encoding="utf-8").replace("//# sourceMappingURL=leaflet.js.map", "")
mappa = (S / "mappa.js").read_text(encoding="utf-8").strip()

testa = (
    "(function(){var r=document.getElementById('ms-root');if(!r)return;"
    "var s=document.createElement('style');s.textContent=" + json.dumps(stile, ensure_ascii=False) + ";"
    "document.head.appendChild(s);r.innerHTML=" + json.dumps(pagina, ensure_ascii=False) + "})();\n"
)
# Il tema carica il suo Leaflet 1.3.4 dopo di noi: noConflict ci tiene il nostro
# e restituisce window.L a chi c'era prima. Mischiare le due versioni rompe i percorsi.
inizio = "(function(){var L=window.L;"
assert mappa.startswith(inizio), "mappa.js deve iniziare con " + inizio
mappa = "(function(){if(!document.getElementById('ms-root'))return;var L=window.L.noConflict();" + mappa[len(inizio):]

(QUI / "mappa-sedi.js").write_text(testa + leaflet + "\n" + mappa + "\n", encoding="utf-8")
print("mappa-sedi.js:", (QUI / "mappa-sedi.js").stat().st_size, "byte")
