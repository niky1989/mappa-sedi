# Mappa sedi UNIPD per appartamentibp.it

Mappa interattiva delle sedi dell'Università di Padova (aule di lezione, aule studio,
dipartimenti, biblioteche) con i percorsi a piedi da ogni appartamento.

La pagina `mappa-interattiva` del sito carica `mappa-sedi.js` da jsDelivr.
L'appartamento di partenza si sceglie con `?da=`, per esempio `?da=falloppio-34`.

Per aggiornarla: modificare i file in `sorgente/`, poi `python3 costruisci.py` e pubblicare.

Mappa © OpenStreetMap contributors. Percorsi a piedi e in bici calcolati con OSRM (profili foot e bicycle) su estratto Geofabrik nord-est, novembre 2026. Leaflet 1.9.4 (BSD-2-Clause).
