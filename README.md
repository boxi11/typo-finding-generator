# typo-finding-generator

## Requirement
```bash
> cspell --version                             
6.12.0
> python3 --version        
Python 3.10.9
```

## How to
1. Copy `typo-checker.py`, `cspell.config.yaml` and `project-words.txt` to the working directory.
2. Add the false-positive words to `project-words.txt`. 
   1. The list of typos will print out in the terminal, such that you can review and adjust the words in `project-words.txt`.
   2. Words in `project-words.txt` should be separated by newline, and the characters are case-insensitive.
3. Change the `acct_dirname` in `typo-checker.py` to have the correct file locations.
4. Change the `ext` in `typo-checker.py` to have the correct file extensions. e.g. "sol" for Solidity, "rs" for Rust, etc.
5. Change the `pid` in in `typo-checker.py` to have the correct project ID. `pid` can be found at the acct url. e.g. The `pid` of the project with link of `https://acc.audit.certikpowered.info/project/e0a5c3c0-0ae2-11ed-bdc5-fff6beacf5a5` is `e0a5c3c0-0ae2-11ed-bdc5-fff6beacf5a5`.
6. Run `python3 typo-checker.py <contract-path>`.
7. Copy all from `typos.json`, create a new finding on accelerator, and click the "Paste" button to fill the typo finding.
