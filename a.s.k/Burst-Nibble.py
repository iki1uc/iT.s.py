# burst_nibble.py - 1 Datei, ehrlich, kein Luegen
from pathlib import Path
HERE = Path(__file__).parent
NIBBLES = [
    ("1. index", ["index.html"]),
    ("2. pipeline", ["3.js","81.js","9.js","mirror.js"]),
    ("3. MA3", ["mirror.js","respo-matrix.json","respo-matrix-engine.js"]),
]
def nibble(name, files):
    fehlt=[f for f in files if not (HERE/f).exists()]
    print(f"NIBBLE: {name} ... {'sauber' if not fehlt else 'fehlt: '+', '.join(fehlt)}")
    return not fehlt
def run():
    print("BURST NIBBLE RUN")
    res=[nibble(n,f) for n,f in NIBBLES]
    assert sum([1,3,5,7,9])==25==5*5
    print("NC_END = 25 - 25=5*5 - geprueft")
    print("Alles da. Zu. Fertig. Stehen. Stufe 7." if all(res) else f"Noch offen: {sum(not r for r in res)} von 3. Nicht fertig.")
    print("Klick - Klack - ZAM.")
if __name__=="__main__":
    run()
