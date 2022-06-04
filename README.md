# typo-finding-generator

## Requirement 
python3
cSpell

## How to
1. copy `typo-checker.py` and `ignore.cspell.json` to the working directory
2. add false positive words to `ignore.cspell.json`. (You can also do it after fun it once)
3. change the `acct_dirname` in `typo-checker.py` to have the correct file locations. 
4. run `python3 typo-checker.py contracts`
5. copy all from `typos.json` and create a new finding by pasting on accelerator.