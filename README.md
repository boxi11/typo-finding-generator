# typo-finding-generator

## Requirement
python3
cSpell

## How to
1. Copy `typo-checker.py` and `ignore.cspell.json` to the working directory.
2. Add the false-positive words to `ignore.cspell.json`. (You can also do it after run it once)
3. Change the `acct_dirname` in `typo-checker.py` to have the correct file locations.
4. Change the `ext` in `typo-checker.py` to have the correct file extensions. e.g. "sol" for Solidity, "rs" for Rust, etc.
5. Change the `pid` in in `typo-checker.py` to have the correct project ID. `pid` can be found at the acct url. e.g. https://acc.audit.certikpowered.info/project/e0a5c3c0-0ae2-11ed-bdc5-fff6beacf5a5
6. Run `python3 typo-checker.py <contract-path>`.
7. Copy all from `typos.json`, create a new finding on accelerator, and click the "Paste" button to fill the typo finding.
