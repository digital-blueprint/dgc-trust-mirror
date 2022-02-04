#!/usr/bin/env python

import json
import sys
from tabulate import tabulate

def main(argv):
    with open(argv[1], "rb") as h:
        rules = json.loads(h.read())

    all_ = []
    columns = [
        "Identifier", "Version", "CertificateType", "Description", "ValidFrom", "ValidTo", "Region"]

    for r in rules["r"]:
        rule = json.loads(r["r"])
        if rule["Country"] == "AT" and rule["Engine"] == "CERTLOGIC":
            for desc in list(rule["Description"]):
                if desc["lang"] == "en":
                    rule["Description"] = desc["desc"]
            row = []
            for column in columns:
                row.append(rule.pop(column, ""))
            all_.append(row)
    all_.sort(key=lambda e: (e[-1], e[-3], e[0]), reverse=True)
    print(tabulate(all_, columns, tablefmt="github"))

if __name__ == "__main__":
    main(sys.argv)
