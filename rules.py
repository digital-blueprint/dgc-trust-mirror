#!/usr/bin/env python

import json
import sys
from tabulate import tabulate

def main(argv):
    with open(argv[1], "rb") as h:
        rules = json.loads(h.read())

    all_ = []
    keys = []

    for r in rules["r"]:
        rule = json.loads(r["r"])
        if rule["Country"] == "AT" and rules["Engine"] == "CERTLOGIC":

            rule.pop("Logic", None)
            rule.pop("AffectedFields", None)
            rule.pop("SchemaVersion", None)
            rule.pop("EngineVersion", None)
            rule.pop("Country", None)

            for desc in list(rule["Description"]):
                if desc["lang"] == "en":
                    rule["Description"] = desc["desc"]

            all_.append(list(rule.values()))
            keys = list(rule.keys())
    all_.sort(key=lambda e: (e[-1], e[-3], e[0]), reverse=True)
    print(tabulate(all_, keys, tablefmt="github"))

if __name__ == "__main__":
    main(sys.argv)
