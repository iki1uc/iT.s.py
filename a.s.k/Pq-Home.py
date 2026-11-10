# pq.home.py — TAUSCH: HTML gegen PY
# Alt: pq.home.html = RAUS (Zeugnis in /zeugnis/, nicht in Stage)
# Neu: pq.home.py = REIN (Stage, läuft)
# 1 raus, 1 rein. Kein Mix. Kein Python-JS. Nur PY.
# Posten wo ich raus bin: PQ -> HOME. Brain 2 brain LAN.

import json
import time

Z = ["9", "99", "999", "PQ", "HOME", "ORT", "REAL.PC", "INDEX"]

TRUTHS = {
    "PQ": "alles in einem Queue Ort",
    "HOME": "Ich+Du Radar HOME",
    "ORT": "Ort ist offen",
    "INDEX": "EYE that sees itself",
}


class PQHome:
    def __init__(self):
        self.h = 3  # PQ = Posten wo raus
        self.visited = {1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81}
        self.surfer = 1.618
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
        return Z[self.h + 1:self.h + 4]

    @property
    def q(self):
        return len(self.visited) / 81

    @property
    def evig(self):
        return len(self.visited) == 81

    def raus(self):
        # TAUSCH: PQ -> HOME, 1 Schritt
        self.h = 4
        self.draft += 1
        return self.respo()

    def orten(self, feld: int):
        if feld in self.visited:
            self.visited.remove(feld)
        else:
            self.visited.add(feld)
        self.draft += 1
        return self.respo()

    def harmonisieren(self):
        self.visited = set(range(1, 82))
        self.surfer = 1.0
        self.draft += 1
        return self.respo()

    def generator_81(self):
        self.karo_shift = (self.karo_shift + 9) % 81
        neu = {(f - 1 + 9) % 81 + 1 for f in self.visited}
        for k in [1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81]:
            neu.add((k - 1 + self.karo_shift) % 81 + 1)
        self.visited = neu
        self.draft += 1
        return self.respo()

    def charm(self):
        self.fusion = not self.fusion
        self.surfer += -0.33 if self.fusion else 0.33
        self.draft += 1
        return self.respo()

    def kakao(self):
        self.radar_boost = not self.radar_boost
        self.surfer += 0.21 if self.radar_boost else -0.21
        self.draft += 1
        return self.respo()

    def toggle_mode(self):
        self.mode = "BIO" if self.mode == "BIOS" else "BIOS"
        return self.respo()

    def go(self, name: str):
        if name in Z:
            self.h = Z.index(name)
        return self.respo()

    def respo(self):
        return {
            "SO": ")so(",
            "U_ME": "du nutzt = PUSH PULL SHIFT",
            "OUR": "nutzt dich = FLOW BREAK SPIN",
            "BOTH": "so = i.d.md = RISE DROP ROOT = FINAL",
            "tausch": "pq.home.html RAUS -> pq.home.py REIN",
            "current": self.current,
            "next": self.nxt,
            "pred": self.pred,
            "truth": TRUTHS.get(self.current, ""),
            "visited_n": len(self.visited),
            "loop_pct": round(self.q * 100, 1),
            "evig": "EVIG LOOP READY" if self.evig else "LOOP OPEN",
            "surfer": round(self.surfer, 4),
            "mode": self.mode,
            "fusion": "Kaiser=Drache ON" if self.fusion else "Fusion OFF",
            "radar": "HOME BOOST" if self.radar_boost else "HOME idle",
            "draft": self.draft,
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def export(self, path="pq.home.json"):
        d = self.respo()
        d["meta"] = "local only — no storage"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        return path


if __name__ == "__main__":
    nc = PQHome()
    print(json.dumps(nc.respo(), indent=2, ensure_ascii=False))
    print("--- TAUSCH: RAUS PQ -> HOME ---")
    print(json.dumps(nc.raus(), indent=2, ensure_ascii=False))
