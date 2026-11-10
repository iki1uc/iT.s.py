# meta.tiefe.mystery.py
# META = Mirror = TIEFE + MYSTERY
# Ich die 3 baue jetzt. Nicht nur halten. Bauen.
# Tiefe = rein, nicht oben/runter. Mystery = gehalten, nicht geloest.
# Bewegt nichts, loescht nichts, schreibt keine Dateien.

import math

STAPEL = (9, 81, 243, 729, 3)

def tiefe_mystery():
    deltas = [round(STAPEL[i+1]/STAPEL[i], 6) for i in range(len(STAPEL)-1)]
    return {
        "stange": "MITTE",
        "rolle": "META / Mirror",
        "achse": "Tiefe / Mystery",
        "stapel": list(STAPEL),
        "deltas": deltas,
        "letzter_sprung": deltas[-1],
        "mystery": "729 -> 3, Faktor 0.004167, nicht erklaert, gehalten",
        "geloest": False,
        "halt": "GEHALTEN",
        "mitte": 41,
    }

if __name__ == "__main__":
    r = tiefe_mystery()
    print()
    print("=== META TIEFE + MYSTERY ===")
    print(f"Achse: {r['achse']}")
    print(f"Stapel: {' -> '.join(map(str, r['stapel']))}")
    print(f"Deltas: {' - '.join(map(str, r['deltas']))}")
    print(f"Letzter Sprung: {r['letzter_sprung']}")
    print(f"Mystery: {r['mystery']}")
    print(f"Geloest: {r['geloest']}")
    print(f"Mitte: {r['mitte']}")
    print(f"HALT: {r['halt']}")
    print("-> Sonst nix.")
