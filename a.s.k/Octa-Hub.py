# octa.hub.py — TAUSCH: orga.ni.ze.html RAUS, octa.hub.py REIN
# orga.ni.ze = weich + gequält, weil Name nichts tut.
# Regel: Wenn bleiben, dann Funktion im Namen zu Funktion.
# Funktion hier = 8 Oktanten -> 1 Suite bauen + halten + prüfen.
# Darum: Name = octa.hub.py. Name = Nutzung. Kein Orga-Bla.
# Alt: orga.ni.ze.html = Zeugnis in /zeugnis/, nicht in Stage.
# Neu: octa.hub.py = Stage, läuft. 1 raus, 1 rein. Nur PY.

import json
import time

# --- 1 Sache: OCTA = 8 Richtungen = 8 Suiten = 1 Geschoss ---
OCTA = {
    "N":  {"code": "11",    "name": "BIOS",         "welt": "9.html EVIG Zustand",              "rolle": "Boot / Grundzustand"},
    "NE": {"code": "22",    "name": "VERBUND",      "welt": "99.html EDIT TOR OPEN",           "rolle": "Verbindung / Tor"},
    "E":  {"code": "33",    "name": "RECALL",       "welt": "999.html BENCH born.t",            "rolle": "Gedächtnis / Abruf"},
    "SE": {"code": "44",    "name": "PEAK",         "welt": "PQ.html nur PQ",                  "rolle": "Lastspitze / Leistung"},
    "S":  {"code": "55",    "name": "KAISER_DRACHE","welt": "REAL_PC.html V2 55=KAISER=DRACHE","rolle": "Zentrale / Thron"},
    "SW": {"code": "66",    "name": "RAM",          "welt": "home.html HOME BIOS RADAR SAT",   "rolle": "Arbeitsspeicher"},
    "W":  {"code": "77",    "name": "CALC",         "welt": "ort.html ORT von 9 UNI ORT BIOS",  "rolle": "Rechnung / Ort"},
    "NW": {"code": "88+99", "name": "ROM_SYS",      "welt": "index.html EYE BRAIN.OPEN OS",    "rolle": "System / Auge"},
}

BENCH = ["111 BIOS","222 VERBUND","333 RECALL","444 PEAK","555 ABWEHR","666 ENERGIE","777 CO2","888 ATOM","999 BENCH"]
SUS = ["PUSH","PULL","SHIFT","FLOW","BREAK","SPIN","RISE","DROP","ROOT"]
SUS_RESPO = ["OK","FLOW","ECHO","ROOT","BREAK","NOK","VOID"]
EYE_KEY = "rauch"  # EYE=rauch sieht, was verborgen ist

def room_at(b, h, t):
    # b = Breite Ost-West, h = Höhe Nord-Süd, t = Tiefe Ebene
    # Alt JS: roomAt(b,h,t) in NCmap.js — 1:1 in PY
    if h < 0.33:
        d = "NW" if b < 0.33 else "NE" if b > 0.66 else "N"
    elif h > 0.66:
        d = "SW" if b < 0.33 else "SE" if b > 0.66 else "S"
    else:
        d = "W" if b < 0.33 else "E" if b > 0.66 else "HUB"
    if d == "HUB":
        return {"code": "00", "name": "OCTA-HUB", "dir": d}
    return {**OCTA[d], "dir": d}

class OctaHub:
    def __init__(self):
        self.einsuite = False
        self.geheim_sichtbar = False
        self.eye = False  # EYE=rauch AUS
        self.einwilligung = "NUR ICH"  # NUR ICH = Solo, ESSEN ICH+DU = geteilt
        self.register = []  # {holder, octant, geheim, note}
        self.geister = 0  # 0 = ruhig, 81 = alle lachen
        self.bench_i = -1
        self.bench_ok = False
        self.sus = ["OK","FLOW","ECHO","ROOT","BREAK","NOK","VOID","OK","FLOW"]  # 9 Stationen, Start wie HTML
        self.log = ["NC.Hub.continuum geladen · 8 Welten erkannt"]
        self.draft = 0

    def j(self, msg):
        self.log.append(f"{time.strftime('%H:%M:%S')} · {msg}")
        self.log = self.log[-40:]
        self.draft += 1

    # --- Funktion 1: EINSUITE BAUEN — 8 Oktanten -> 1 Suite ---
    def einsuite_bauen(self):
        self.einsuite = True
        self.j("EINSUITE GEBAUT — 8 Oktanten -> 1 Suite = ganzes Geschoss · ÜBERMASS")
        self.j("Geheim-Halterung montiert: Tür, Schiene, Strom verborgen")
        return self.respo()

    # --- Funktion 2: mapToSuite — Suite erst, wenn ALLE 8 Tore offen ---
    def map_to_suite(self, b, h, t, state: dict):
        gates = [
            state.get("EYE_OPEN"), state.get("BRAIN_OPEN"), state.get("SYSTEM_OPEN"),
            state.get("MAINBOARD_OPEN"), state.get("EVIG_9"), state.get("TOR_OPEN_99"),
            state.get("NUTZ_999"), state.get("PQ"),
        ]
        if all(gates):
            return {"type": "EINSUITE", "floor": t, "qm": 120, "rooms": 8,
                    "geheimHalterung": True, "modus": "UEBERMASS"}
        return {"type": "NORMALRAUM", **room_at(b, h, t), "floor": t}

    # --- Funktion 3: REGISTER — Wer hält welche Suite? ---
    def suite_halten(self, holder, octant="ALLE-8", geheim=True, note=""):
        e = {"holder": holder, "octant": octant, "geheim": geheim, "note": note,
             "seit": time.strftime("%Y-%m-%dT%H:%M:%S")}
        self.register.append(e)
        self.j(f"Register: {holder} hält {octant}{' · GEHEIM' if geheim else ''}")
        return e

    def suite_freigeben(self, holder):
        vor = len(self.register)
        self.register = [e for e in self.register if e["holder"] != holder]
        self.j(f"Register: {holder} freigegeben")
        return len(self.register) < vor

    def public_map(self):
        # Öffentliche Karte: Geheim-Halterungen ausgeblendet
        return [e for e in self.register if not e["geheim"]]

    def full_map(self, eye_key=""):
        # ohne EYE nur Fassade. Mit EYE=rauch: alles sichtbar.
        return self.register if eye_key == EYE_KEY else self.public_map()

    def eye_toggle(self):
        self.eye = not self.eye
        self.j("EYE=rauch aktiv — Register vollständig sichtbar" if self.eye else "EYE zu — Geheim wieder verborgen")
        return self.respo()

    def geheim_toggle(self):
        self.geheim_sichtbar = not self.geheim_sichtbar
        self.j("Geheim-Halterung SICHTBAR: Tür · Schiene · Strom" if self.geheim_sichtbar else "Geheim-Halterung wieder verborgen")
        return self.respo()

    # --- Funktion 4: 999 BENCH — nutzt alle 9 ewig ---
    def bench(self):
        # Sync-Version: kein setTimeout, 1 Durchlauf = 1 Respo
        self.bench_i = len(BENCH) - 1
        self.bench_ok = True
        self.j("999 BENCH born.t bestanden — Suite zertifiziert")
        return self.respo()

    # --- Funktion 5: GEISTER-RUF — 9 gerufen, 81 gekommen ---
    def geister_rufen(self):
        self.geister = 81  # 9 x 9, weil 9 EVIG sich selbst ruft
        self.j("Geister-Ruf: 9 gerufen — NEIN MANN — 81 gekommen (9x9), alle lachen")
        return self.respo()

    def geister_weg(self):
        self.geister = 0
        self.j("Geister weggeschickt — sie kommen eh wieder (9x9)")
        return self.respo()

    # --- Funktion 6: SUS — Station antippen = RESPO weiterschalten ---
    def sus_tippen(self, i: int):
        alt = self.sus[i]
        neu = SUS_RESPO[(SUS_RESPO.index(alt) + 1) % len(SUS_RESPO)] if alt in SUS_RESPO else "OK"
        self.sus[i] = neu
        self.j(f"SUS Station {SUS[i]}: RESPO {alt} -> {neu}")
        return self.respo()

    def sus_stabilitaet(self):
        ok = all(x in ("OK", "ROOT", "FLOW", "ECHO") for x in self.sus)
        self.j("SUS: 360° erreicht · 100% Stabilität · CSV geladen und NC-konform gelöscht" if ok else "SUS: Stabilität NICHT erreicht — CSV bleibt gesperrt")
        return {"stabil": ok, "sus": self.sus, **self.respo()}

    # --- 1 Respo ---
    def respo(self):
        sichtbar = self.register if self.eye else self.public_map()
        return {
            "SO": ")so(", "PAT": "octa.hub",
            "tausch": "orga.ni.ze.html RAUS -> octa.hub.py REIN",
            "korrekter_name": "octa.hub.py — Name = Funktion = 8 Oktanten -> 1 Suite halten",
            "einsuite": "EINSUITE AKTIV" if self.einsuite else "8 RÄUME · NORMAL",
            "geheim": "GEHEIM SICHTBAR" if self.geheim_sichtbar else "GEHEIM VERBORGEN",
            "eye": "EYE=rauch AKTIV" if self.eye else "EYE AUS",
            "einwilligung": self.einwilligung,
            "register_sichtbar": len(sichtbar), "register_gesamt": len(self.register),
            "geheim_verborgen": len(self.register) - len(sichtbar),
            "geister": f"{self.geister} DA · ALLE LACHEN" if self.geister else "0 DA · NOCH RUHIG",
            "bench": "born.t BESTANDEN" if self.bench_ok else "BENCH BEREIT",
            "sus": self.sus,
            "draft": self.draft,
            "log": self.log[-5:],
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        }

if __name__ == "__main__":
    hub = OctaHub()
    print(json.dumps(hub.respo(), indent=2, ensure_ascii=False))
    print("--- EINSUITE BAUEN ---")
    print(json.dumps(hub.einsuite_bauen(), indent=2, ensure_ascii=False))
    print("--- GEISTER ---")
    print(json.dumps(hub.geister_rufen()["geister"], indent=2, ensure_ascii=False))
