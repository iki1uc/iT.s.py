# org.py — ORGA · NI · ZE
# Alt: org.html / orga.ni.ze.html = Zeugnis, bleibt links
# Neu: org.py = Stage, steht rechts
# 1 Sache, 2 Sichten, 1 Mirror -> 3 ohne Verlust
# Loeschen immer Option: rm org.html  # nur wenn du JA sagst, sonst bleibt es

STATIONEN = ["PUSH", "PULL", "SHIFT", "FLOW", "BREAK", "SPIN", "RISE", "DROP", "ROOT"]
LAYER_4U = {
    "EDITport": "99 EDIT TOR",
    "IMport": "9 EVIG rein",
    "EXport": "999 NUTZ raus",
    "ID": "PQ nur PQ",
}
RESPO = {
    "OK": ("GRUEN", "Oeffnen"),
    "NOK": ("ROT", "Block"),
    "FLOW": ("GELB", "Durchlauf"),
    "BREAK": ("ROT", "Stop"),
    "ECHO": ("GELB", "Spiegel"),
    "VOID": ("ROT", "Neutral"),
    "ROOT": ("GRUEN", "Ursprung"),
}

class Org:
    def __init__(self):
        self.gesammelt = []
        self.nischen = []
        self.lacht = 0
        self.log = ["orga.ni.ze geladen - 9 Geister warten. RUF bereit."]

    def orga(self):
        # ORGA sammelt alle 9 Stationen
        self.gesammelt = list(STATIONEN)
        self.log.append("ORGA: 9/9 Stationen gesammelt (PUSH...ROOT)")
        return self.gesammelt

    def ni(self):
        # NI bildet Nischen aus 4u Layern
        self.nischen = list(LAYER_4U.items())
        self.log.append("NI: 4 Nischen gebildet (EDITport/IMport/EXport/ID)")
        return self.nischen

    def ze(self):
        # ZE zentrale: RUF 9 GEISTER -> 81 lacht
        self.lacht = 81
        self.log.append("ZE: RUF 9 GEISTER -> 81 lacht, Board organisiert")
        return self.lacht

    def respo(self):
        # CSV-Gate: nur 100% + 360 Grad -> CSV wird geloescht
        fertig = len(self.gesammelt) == 9 and len(self.nischen) == 4 and self.lacht == 81
        return {
            "org": len(self.gesammelt),
            "ni": len(self.nischen),
            "ze": self.lacht,
            "fertig": fertig,
            "status": "ROOT GRUEN Ursprung" if fertig else "FLOW GELB Durchlauf",
            "csv": "loeschen" if fertig else "halten",
            "log": self.log,
        }

    def reset(self):
        self.__init__()
        self.log.append("Reset - Board geleert. 9 Geister warten erneut.")
        return self.respo()

def go():
    o = Org()
    o.orga()
    o.ni()
    o.ze()
    return o.respo()

if __name__ == "__main__":
    r = go()
    print(f"ORGA {r['org']}/9 - NI {r['ni']}/4 - ZE {r['ze']}/81")
    print(r["status"], "| CSV:", r["csv"])
    for l in r["log"]:
        print(" ", l)
