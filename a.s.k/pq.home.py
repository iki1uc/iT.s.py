# pq.home.py — TAUSCH: HTML gegen PY
# Alt: pq.home.html = RAUS (Zeugnis in /zeugnis/, nicht in Stage)
# Neu: pq.home.py = REIN (Stage, laeuft)
# 1 raus, 1 rein. Kein Mix. Kein Python-JS. Nur PY.
# Dieses Skript verschiebt und loescht nie Dateien. Es meldet nur den Stand.

import json
import time
from pathlib import Path
from types import MappingProxyType

HERE = Path(__file__).parent

Z = ("9", "99", "999", "PQ", "HOME", "ORT", "REAL.PC", "INDEX")
TRUTHS = MappingProxyType({
    "PQ": "alles in einem Queue Ort",
    "HOME": "Ich+Du Radar HOME",
    "ORT": "Ort ist offen",
    "INDEX": "EYE that sees itself",
})
ACHSEN = MappingProxyType({
    "SO": ")so(",
    "U_ME": "du nutzt = PUSH PULL SHIFT",
    "OUR": "nutzt dich = FLOW BREAK SPIN",
    "BOTH": "so = i.d.md = RISE DROP ROOT = FINAL",
})

FELDER = range(1, 82)
KARO = tuple(range(1, 82, 8))
SURFER_BASIS = 1.618
SURFER_RESET = 1.0
FUSION_SCHRITT = 0.33
RADAR_SCHRITT = 0.21


def ist_feld(x):
    return isinstance(x, int) and not isinstance(x, bool) and x in FELDER


class PQHome:
    def __init__(self):
        self.h = Z.index("PQ")
        self.visited = set(KARO)
        self.basis = SURFER_BASIS
        self.mode = "BIOS"
        self.fusion = False
        self.radar_boost = False
        self.draft = 0
        self.karo_shift = 0

    @property
    def current(self):
        return Z[self.h]

    @property
    def nxt(self):
        return Z[min(self.h + 1, len(Z) - 1)]

    @property
    def pred(self):
        return list(Z[self.h + 1:self.h + 4])

    @property
    def surfer(self):
        return round(self.basis - FUSION_SCHRITT * self.fusion + RADAR_SCHRITT * self.radar_boost, 4)

    @property
    def q(self):
        return len(self.visited) / len(FELDER)

    @property
    def evig(self):
        return self.visited == set(FELDER)

    def tausch(self):
        if (HERE / "pq.home.html").exists():
            return "OFFEN: pq.home.html liegt noch in der Stage"
        zeugnis = (HERE / "zeugnis" / "pq.home.html").exists()
        return "RAUS: pq.home.html nicht in der Stage" + (", Zeugnis gefunden" if zeugnis else ", kein Zeugnis gefunden")

    def raus(self):
        if self.current != "PQ":
            return self.respo(f"raus gilt nur auf PQ, du bist auf {self.current}")
        self.h = Z.index("HOME")
        self.draft += 1
        return self.respo()

    def orten(self, feld):
        if not ist_feld(feld):
            return self.respo(f"Feld {feld!r} ungueltig, erlaubt sind ganze Zahlen 1 bis 81")
        self.visited ^= {feld}
        self.draft += 1
        return self.respo()

    def harmonisieren(self):
        self.visited = set(FELDER)
        self.basis = SURFER_RESET
        self.fusion = False
        self.radar_boost = False
        self.draft += 1
        return self.respo()

    def generator_81(self):
        self.karo_shift = (self.karo_shift + 9) % 81
        neu = {(f - 1 + 9) % 81 + 1 for f in self.visited}
        neu |= {(k - 1 + self.karo_shift) % 81 + 1 for k in KARO}
        self.visited = neu
        self.draft += 1
        return self.respo()

    def charm(self):
        self.fusion = not self.fusion
        self.draft += 1
        return self.respo()

    def kakao(self):
        self.radar_boost = not self.radar_boost
        self.draft += 1
        return self.respo()

    def toggle_mode(self):
        self.mode = "BIO" if self.mode == "BIOS" else "BIOS"
        return self.respo()

    def go(self, name):
        if name not in Z:
            return self.respo(f"{name!r} unbekannt, gueltig: {', '.join(Z)}")
        self.h = Z.index(name)
        return self.respo()

    def respo(self, hinweis=""):
        return {
            **ACHSEN,
            "tausch": self.tausch(),
            "current": self.current,
            "next": self.nxt,
            "pred": self.pred,
            "truth": TRUTHS.get(self.current, ""),
            "visited_n": len(self.visited),
            "loop_pct": round(self.q * 100, 1),
            "evig": "EVIG LOOP READY" if self.evig else "LOOP OPEN",
            "surfer": self.surfer,
            "mode": self.mode,
            "fusion": "Kaiser=Drache ON" if self.fusion else "Fusion OFF",
            "radar": "HOME BOOST" if self.radar_boost else "HOME idle",
            "draft": self.draft,
            "hinweis": hinweis,
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def export(self, path=None, ueberschreiben=False):
        p = Path(path) if path else HERE / "pq.home.json"
        if p.exists() and not ueberschreiben:
            raise FileExistsError(f"{p} gibt es schon. Mit ueberschreiben=True nur nach deinem JA.")
        d = self.respo()
        d["meta"] = "lokale Datei, nur auf Aufruf geschrieben"
        p.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
        return str(p)


if __name__ == "__main__":
    nc = PQHome()
    print(json.dumps(nc.respo(), indent=2, ensure_ascii=False))
    print("--- TAUSCH: RAUS PQ -> HOME ---")
    print(json.dumps(nc.raus(), indent=2, ensure_ascii=False))
