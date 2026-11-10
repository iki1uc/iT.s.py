# octa.hub.py — TAUSCH: orga.ni.ze.html RAUS, octa.hub.py REIN
# Regel: Name = Funktion. Funktion hier = 8 Oktanten -> 1 Suite bauen + halten + pruefen.
# Alt: orga.ni.ze.html = Zeugnis in /zeugnis/, nicht in Stage.
# Neu: octa.hub.py = Stage, laeuft. 1 raus, 1 rein. Nur PY.
# Dieses Skript verschiebt und loescht nie Dateien. Es meldet nur den Stand.

import json
import time
from pathlib import Path
from types import MappingProxyType

HERE = Path(__file__).parent
ALT = "orga.ni.ze.html"

# --- 1 Sache: OCTA = 8 Richtungen = 8 Suiten = 1 Geschoss ---
OCTA = MappingProxyType({
    "N":  {"code": "11",    "name": "BIOS",          "welt": "9.html EVIG Zustand",               "rolle": "Boot / Grundzustand"},
    "NE": {"code": "22",    "name": "VERBUND",       "welt": "99.html EDIT TOR OPEN",            "rolle": "Verbindung / Tor"},
    "E":  {"code": "33",    "name": "RECALL",        "welt": "999.html BENCH born.t",             "rolle": "Gedächtnis / Abruf"},
    "SE": {"code": "44",    "name": "PEAK",          "welt": "PQ.html nur PQ",                   "rolle": "Lastspitze / Leistung"},
    "S":  {"code": "55",    "name": "KAISER_DRACHE", "welt": "REAL_PC.html V2 55=KAISER=DRACHE", "rolle": "Zentrale / Thron"},
    "SW": {"code": "66",    "name": "RAM",           "welt": "home.html HOME BIOS RADAR SAT",    "rolle": "Arbeitsspeicher"},
    "W":  {"code": "77",    "name": "CALC",          "welt": "ort.html ORT von 9 UNI ORT BIOS",   "rolle": "Rechnung / Ort"},
    "NW": {"code": "88+99", "name": "ROM_SYS",       "welt": "index.html EYE BRAIN.OPEN OS",     "rolle": "System / Auge"},
})
GATES = ("EYE_OPEN", "BRAIN_OPEN", "SYSTEM_OPEN", "MAINBOARD_OPEN", "EVIG_9", "TOR_OPEN_99", "NUTZ_999", "PQ")
BENCH = ("111 BIOS", "222 VERBUND", "333 RECALL", "444 PEAK", "555 ABWEHR", "666 ENERGIE", "777 CO2", "888 ATOM", "999 BENCH")
SUS = ("PUSH", "PULL", "SHIFT", "FLOW", "BREAK", "SPIN", "RISE", "DROP", "ROOT")
SUS_RESPO = ("OK", "FLOW", "ECHO", "ROOT", "BREAK", "NOK", "VOID")
STABIL = frozenset({"OK", "ROOT", "FLOW", "ECHO"})
EINWILLIGUNG = ("NUR ICH", "ESSEN ICH+DU")
ALLE = "ALLE-8"
EYE_KEY = "rauch"   # Anzeige-Schalter, kein Geheimnisschutz: steht im Quelltext
LOW, HIGH = 0.33, 0.66


def room_at(b, h, t):
    # b = Breite Ost-West, h = Hoehe Nord-Sued (beide 0..1), t = Tiefe Ebene
    for v in (b, h):
        if not isinstance(v, (int, float)) or isinstance(v, bool) or not 0 <= v <= 1:
            raise ValueError("b und h muessen Zahlen von 0 bis 1 sein")
    if h < LOW:
        d = "NW" if b < LOW else "NE" if b > HIGH else "N"
    elif h > HIGH:
        d = "SW" if b < LOW else "SE" if b > HIGH else "S"
    else:
        d = "W" if b < LOW else "E" if b > HIGH else "HUB"
    if d == "HUB":
        return {"code": "00", "name": "OCTA-HUB", "dir": d}
    return {**OCTA[d], "dir": d}


class OctaHub:
    def __init__(self):
        self.einsuite = False
        self.geheim_sichtbar = False
        self.eye = False
        self.einwilligung = EINWILLIGUNG[0]
        self.register = []
        self.geister = 0
        self.bench_ok = False
        self.bench_ergebnis = []
        self.sus = ["OK", "FLOW", "ECHO", "ROOT", "BREAK", "NOK", "VOID", "OK", "FLOW"]
        self.log = ["NC.Hub.continuum geladen · 8 Welten erkannt"]
        self.draft = 0

    def j(self, msg):
        self.log.append(f"{time.strftime('%H:%M:%S')} · {msg}")
        del self.log[:-40]

    def tausch(self):
        if (HERE / ALT).exists():
            return f"OFFEN: {ALT} liegt noch in der Stage"
        zeugnis = (HERE / "zeugnis" / ALT).exists()
        return f"RAUS: {ALT} nicht in der Stage" + (", Zeugnis gefunden" if zeugnis else ", kein Zeugnis gefunden")

    def einsuite_bauen(self):
        self.einsuite = True
        self.draft += 1
        self.j("EINSUITE GEBAUT — 8 Oktanten -> 1 Suite = ganzes Geschoss · ÜBERMASS")
        self.j("Geheim-Halterung montiert: Tür, Schiene, Strom verborgen")
        return self.respo()

    def map_to_suite(self, b, h, t, state):
        raum = room_at(b, h, t)
        zu = [g for g in GATES if state.get(g) is not True]
        if not zu:
            return {"type": "EINSUITE", "floor": t, "qm": 120, "rooms": 8,
                    "geheimHalterung": True, "modus": "UEBERMASS", "gebaut": self.einsuite}
        return {"type": "NORMALRAUM", **raum, "floor": t, "tore_zu": zu}

    def _belegt_durch(self, octant, holder):
        for e in self.register:
            if e["holder"] != holder and (ALLE in (octant, e["octant"]) or e["octant"] == octant):
                return e["holder"]
        return None

    def suite_halten(self, holder, octant=ALLE, geheim=True, note=""):
        if not isinstance(holder, str) or not holder.strip():
            return self.respo("Halter fehlt")
        if octant != ALLE and octant not in OCTA:
            return self.respo(f"Oktant {octant!r} unbekannt, gueltig: {ALLE}, {', '.join(OCTA)}")
        if any(e["holder"] == holder and e["octant"] == octant for e in self.register):
            return self.respo(f"{holder} haelt {octant} schon")
        anderer = self._belegt_durch(octant, holder)
        if anderer:
            return self.respo(f"{octant} ist belegt durch {anderer}")
        self.register.append({"holder": holder, "octant": octant, "geheim": geheim, "note": note,
                              "seit": time.strftime("%Y-%m-%dT%H:%M:%S")})
        self.draft += 1
        self.j(f"Register: {holder} hält {octant}{' · GEHEIM' if geheim else ''}")
        return self.respo()

    def suite_freigeben(self, holder):
        vor = len(self.register)
        self.register = [e for e in self.register if e["holder"] != holder]
        if len(self.register) == vor:
            return self.respo(f"{holder} hält nichts")
        self.draft += 1
        self.j(f"Register: {holder} freigegeben")
        return self.respo()

    def public_map(self):
        return [e for e in self.register if not e["geheim"]]

    def full_map(self, eye_key=""):
        return list(self.register) if (self.eye or eye_key == EYE_KEY) else self.public_map()

    def eye_toggle(self):
        self.eye = not self.eye
        self.draft += 1
        self.j("EYE=rauch aktiv — Register vollständig sichtbar" if self.eye else "EYE zu — Geheim wieder verborgen")
        return self.respo()

    def geheim_toggle(self):
        self.geheim_sichtbar = not self.geheim_sichtbar
        self.draft += 1
        self.j("Geheim-Halterung SICHTBAR: Tür · Schiene · Strom" if self.geheim_sichtbar else "Geheim-Halterung wieder verborgen")
        return self.respo()

    def einwilligung_setzen(self, wert):
        if wert not in EINWILLIGUNG:
            return self.respo(f"{wert!r} ungueltig, erlaubt: {' / '.join(EINWILLIGUNG)}")
        self.einwilligung = wert
        self.draft += 1
        return self.respo()

    def bench(self):
        erg = []
        for label, text, fn in CHECKS:
            try:
                ok = bool(fn(OctaHub()))
            except Exception:
                ok = False
            erg.append((label, text, ok))
        erg.append((BENCH[-1], "alle vorigen bestanden", all(o for _, _, o in erg)))
        self.bench_ergebnis = erg
        self.bench_ok = all(o for _, _, o in erg)
        self.draft += 1
        self.j(f"BENCH: {sum(o for _, _, o in erg)}/{len(erg)} bestanden" + ("" if self.bench_ok else " · DURCHGEFALLEN"))
        return self.respo()

    def geister_rufen(self):
        self.geister = len(SUS) ** 2
        self.draft += 1
        self.j(f"Geister-Ruf: {len(SUS)} gerufen — NEIN MANN — {self.geister} gekommen ({len(SUS)}x{len(SUS)}), alle lachen")
        return self.respo()

    def geister_weg(self):
        self.geister = 0
        self.draft += 1
        self.j("Geister weggeschickt — sie kommen eh wieder (9x9)")
        return self.respo()

    def sus_tippen(self, i):
        if not isinstance(i, int) or isinstance(i, bool) or not 0 <= i < len(SUS):
            return self.respo(f"Station {i!r} ungueltig, erlaubt 0 bis {len(SUS) - 1}")
        alt = self.sus[i]
        neu = SUS_RESPO[(SUS_RESPO.index(alt) + 1) % len(SUS_RESPO)] if alt in SUS_RESPO else "OK"
        self.sus[i] = neu
        self.draft += 1
        self.j(f"SUS Station {SUS[i]}: RESPO {alt} -> {neu}")
        return self.respo()

    def sus_stabilitaet(self):
        instabil = [s for s, x in zip(SUS, self.sus) if x not in STABIL]
        ok = not instabil
        n = len(SUS) - len(instabil)
        self.j(f"SUS: {n}/{len(SUS)} stabil · CSV freigegeben (hier wird nichts geladen oder geloescht)" if ok
               else f"SUS: {n}/{len(SUS)} stabil — CSV bleibt gesperrt")
        return {**self.respo(), "stabil": ok, "instabil": instabil}

    def respo(self, hinweis=""):
        sichtbar = self.full_map()
        if self.bench_ok:
            bench = "born.t BESTANDEN"
        elif self.bench_ergebnis:
            bench = f"BENCH DURCHGEFALLEN ({sum(o for _, _, o in self.bench_ergebnis)}/{len(self.bench_ergebnis)})"
        else:
            bench = "BENCH BEREIT"
        return {
            "SO": ")so(", "PAT": "octa.hub",
            "tausch": self.tausch(),
            "korrekter_name": "octa.hub.py — Name = Funktion = 8 Oktanten -> 1 Suite halten",
            "einsuite": "EINSUITE AKTIV" if self.einsuite else "8 RÄUME · NORMAL",
            "geheim": "GEHEIM SICHTBAR" if self.geheim_sichtbar else "GEHEIM VERBORGEN",
            "eye": "EYE=rauch AKTIV" if self.eye else "EYE AUS",
            "einwilligung": self.einwilligung,
            "register_sichtbar": len(sichtbar), "register_gesamt": len(self.register),
            "geheim_verborgen": len(self.register) - len(sichtbar),
            "geister": f"{self.geister} DA · ALLE LACHEN" if self.geister else "0 DA · NOCH RUHIG",
            "bench": bench,
            "sus": list(self.sus),
            "draft": self.draft,
            "hinweis": hinweis,
            "log": self.log[-5:],
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        }


def _c_octa(h):
    return len(OCTA) == 8 and len({v["code"] for v in OCTA.values()}) == 8

def _c_raster(h):
    return {room_at(b, c, 0)["dir"] for b in (0.1, 0.5, 0.9) for c in (0.1, 0.5, 0.9)} == set(OCTA) | {"HUB"}

def _c_recall(h):
    h.suite_halten("A", "N")
    h.suite_freigeben("A")
    return h.register == []

def _c_peak(h):
    return h.map_to_suite(0.5, 0.5, 0, dict.fromkeys(GATES, True))["type"] == "EINSUITE"

def _c_abwehr(h):
    eins_zu = {**dict.fromkeys(GATES, True), "PQ": False}
    try:
        room_at(float("nan"), 0.5, 0)
        nan_abgelehnt = False
    except ValueError:
        nan_abgelehnt = True
    return h.map_to_suite(0.5, 0.5, 0, eins_zu)["type"] == "NORMALRAUM" and nan_abgelehnt

def _c_energie(h):
    h.suite_halten("A", "N")
    h.suite_halten("B", "N")
    return len(h.register) == 1

def _c_co2(h):
    h.suite_halten("A", "N", geheim=True)
    h.suite_halten("B", "S", geheim=False)
    return [e["holder"] for e in h.public_map()] == ["B"]

def _c_atom(h):
    start = h.sus[0]
    for _ in SUS_RESPO:
        h.sus_tippen(0)
    return h.sus[0] == start

CHECKS = tuple(zip(BENCH[:8], (
    "8 Oktanten mit 8 eindeutigen Codes",
    "3x3-Raster erreicht alle 8 Oktanten und den HUB",
    "Register: halten und freigeben stellt den Zustand her",
    "8 offene Tore ergeben EINSUITE",
    "1 geschlossenes Tor und NaN werden abgewiesen",
    "zweiter Halter fuer denselben Oktanten wird abgewiesen",
    "public_map blendet Geheim-Eintraege aus",
    "SUS-Zyklus laeuft einmal komplett durch",
), (_c_octa, _c_raster, _c_recall, _c_peak, _c_abwehr, _c_energie, _c_co2, _c_atom)))


if __name__ == "__main__":
    hub = OctaHub()
    print(json.dumps(hub.respo(), indent=2, ensure_ascii=False))
    print("--- EINSUITE BAUEN ---")
    print(json.dumps(hub.einsuite_bauen(), indent=2, ensure_ascii=False))
    print("--- GEISTER ---")
    print(json.dumps(hub.geister_rufen()["geister"], indent=2, ensure_ascii=False))
    print("--- BENCH ---")
    hub.bench()
    for label, text, ok in hub.bench_ergebnis:
        print(f"  {label}: {'OK ' if ok else 'FEHLT'} {text}")
