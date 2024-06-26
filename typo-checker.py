#!/usr/bin/env python3

import subprocess
import json
import os
import sys
from collections import defaultdict
import re
import copy

# variables need to be configured before running
acct_dirname = "$/github.com/CertiKProject/certik-audit-projects/tree/41bfd7b179417ad851abc541bf92635e9972c393/projects/algofi"
ext = "sol"
sort = True
pid = "e0a5c3c0-0ae2-11ed-bdc5-fff6beacf5a5"


class Location:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def execute_cspell(path):
    path = path + "/**/*." + ext
    # print(path)
    process_cspell = subprocess.run(
        [
            "cspell",
            path,
            "--config",
            "cspell.config.yaml"
        ],
        capture_output=True
    )
    return process_cspell.stdout.decode("utf-8").splitlines()


def handle_special_char(string):

    string = string.replace("[", r"\[")
    string = string.replace("]", r"\]")
    string = string.replace("-", r"\-")
    string = string.replace("(", r"\(")
    string = string.replace(")", r"\)")
    string = string.replace("{", r"\{")
    string = string.replace("}", r"\}")

    return string


def generate_acct_json(text):
    finding = {
        "title": "Typos in Comments and Codes",
        "type": "finding",
        "locations": [],
        "category": [
            "coding-style"
        ],
        "severity": "info",
        "confidence": "high",
        "description": "There are several typos in the contracts, please see the locations above, where the words with typos are listed:\n - ",
        "recommendation": "Recommend correcting all of the typos in the contracts to provide better readability for open-source purposes.",
        "status": "pending",
        "origin": {
            "type": "manual"
        }
    }
    location_template = {
        "start": {
            "line": 0,
            "column": 0
        },
        "end": {
            "line": 0,
            "column": 0
        },
        "file": ""
    }

    typo_set = set()

    # get local directory to be replaced with accelerator directory
    local_dirname = os.path.dirname(__file__)
    local_dirname = handle_special_char(local_dirname)

    for line in text:
        contract_file, contract_line, word = line.split(":")

        print(local_dirname)
        print(line)
        print(re.search((local_dirname) +
              r'(.*\.{0})'.format(ext), contract_file))

        contract_file = re.sub((local_dirname) + r'(.*\.{0})'.format(ext),
                               (acct_dirname) + r'\1', contract_file)
        word = re.search(r'\((.*)\)', word)

        location = copy.deepcopy(location_template)
        location['file'] = contract_file
        location['start']['line'] = int(contract_line)
        location['start']['column'] = 1
        location['end']['line'] = int(contract_line) + 1
        location['end']['column'] = 1

        typo_set.add(word.group(1))
        # print(word.group(1))

        if not is_duplicated(finding['locations'], location):
            finding['locations'].append(location)

    if sort:
        typo_set = sorted(typo_set)

    # print for easier checking/adding false positives (project level terms)
    print(typo_set)

    typo_str = '\n - '.join(str(s) for s in typo_set)

    finding['description'] += typo_str
    return finding


def is_duplicated(locations, location):
    for lo in locations:
        if lo['start']['line'] == location['start']['line'] and lo['file'] == location['file']:
            return True


def main(argv):
    raw_output = execute_cspell(argv[0])
    # print(raw_output)

    formatted_output = generate_acct_json(raw_output)
    # print(formatted_output)
    with open("typos.json", "w") as file:
        json.dump(formatted_output, file)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python3 typo-checker.py <path>")
        sys.exit(1)
    main(sys.argv[1:])
