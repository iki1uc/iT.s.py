# vor.rueck.bauen.py
# VOR + RUECK = 1 Achse, laengs
# VOR = CORE, RUECK = Zeugnis
# Bewegt nichts, loescht nichts, schreibt keine Dateien.

import hashlib, json, time

VOR = {
    "stange": "VOR",
    "tab": 3,
    "name": "CORE",
    "achse": "Pruefen / HALT",
    "auftrag": "Pruef 1+2+3 = 6. Offen 2 stehen lassen. Sonst nix.",
    "guckt": "nach hinten, zum Zeugnis, und nach vorne, zum Bau",
    "summe": 6,
    "offen": ["729 -> 3 nicht erklaert", "1+2+3 ergibt 6, nicht 9"],
}

RUECK = {
    "stange": "RUECK",
    "tab": 0,
    "name": "ZEUGNIS",
    "achse": "Was war",
    "auftrag": "Haelt NEUTRAL geloescht, 0.8.66 geloescht, Bank gesprengt. Sonst nix.",
    "guckt": "nach vorne, zur Mitte",
    "steht": ["NEUTRAL geloescht", "H0/0.8.66 geloescht -> NIE.md", "Bank gesprengt"],
}

def laengs_bauen(vor, rueck):
    return {
        "achse": "LAENGS",
        "vor": vor["name"],
        "rueck": rueck["name"],
        "mitte": 41,
        "summe": vor["summe"],
        "offen": vor["offen"],
        "zeugnis": rueck["steht"],
        "halt": "ZIEL",
    }

if __name__ == "__main__":
    q = laengs_bauen(VOR, RUECK)
    print()
    print("=== VOR.RUECK BAUEN ===")
    print(f"VOR   = {q['vor']} — Summe {q['summe']}, offen {len(q['offen'])}")
    print(f"RUECK = {q['rueck']} — haelt {len(q['zeugnis'])} Zeugnisse")
    print(f"LAENGS = 1 Achse, Mitte {q['mitte']}")
    for o in q["offen"]:
        print(f"offen: {o}")
    for z in q["zeugnis"]:
        print(f"zeugnis: {z}")
    print("HALT = ZIEL")
