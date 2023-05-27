# Easy Korean With Steno

Intuitive Korean steno with Plover. It is a Python dictionary and requires the Plover Python Dictionary plugin (get it from the plugin window in Plover). It works on a Macbook, but it is not tested on Windows or Linux.

## Demo

https://youtu.be/MfRnoFWqE-E

Toggle the Easy Korean dictionary by using the Plover dict command plugin: https://github.com/KoiOates/plover_dict_commands

After installing the plugin, define in user.json:

`KRAO*EPB: {PLOVER:TOGGLE_DICT:!easy_korean_steno.py,!main.json,!user.json}`

## How It Works

Plover outputs English/qwerty letters and your computer translates them into Korean letters using the built-in system Korean keyboard layout.

1. Toggle dictionary on when in use. Toggle the dictionary off when not in use.
2. Change computer keyboard layout to Korean. Get the Korean keyboard layout in your operating system.
3. Start stenoing Korean intuitively.

> Note: You have to do one letter at a time. Help/feedback is wanted to make chords a reality.

## Learn

```
starting_consonants = {
    "regular": {
        # consonants
        "K": "r",  # ㄱ
        "TKPW": "r",  # ㄱ
        "TPH": "s",  # ㄴ
        "TK": "e",  # ㄷ
        "R": "f",  # ㄹ
        "HR": "f",  # ㄹ
        "PH": "a",  # ㅁ
        "PW": "q",  # ㅂ
        "S": "t",  # ㅅ
        "W": "d",  # ㅇ
        "SKWR": "w",  # ㅈ
        "KH": "c",  # ㅊ
        "KP": "z",  # ㅋ
        "T": "x",  # ㅌ
        "P": "v",  # ㅍ
        "H": "g",  # ㅎ
        # extra
        "TH": "E",  # ㄸ
        "": "d",  # ㅇ
    },
    "tense": {
        # tense consonants (add *)
        "K": "R",  # ㄲ
        "TKPW": "R",  # ㄲ
        "TK": "E",  # ㄸ
        "PW": "Q",  # ㅃ
        "SKWR": "W",  # ㅉ
        "S": "T",  # ㅆ
    },
    "special": {
        # adds "y" to vowels
        "KW": "r",  # ㄱ
        "TKPWR": "r",  # ㄱ
        "TPWH": "s",  # ㄴ
        "TKW": "e",  # ㄷ
        "WR": "f",  # ㄹ
        "WHR": "f",  # ㄹ
        "KPWHR": "a",  # ㅁ
        "KPWR": "q",  # ㅂ
        "SH": "t",  # ㅅ
        "KWR": "d",  # ㅇ
        "SKW": "w",  # ㅈ
        "KWH": "c",  # ㅊ
        "KPW": "z",  # ㅋ
        "TKWR": "x",  # ㅌ
        "KPR": "v",  # ㅍ
        "WH": "g",  # ㅎ
        "STKPWHR": "",  # empty
    },
}
vowels = {
    # vowels (press * to suppress automatic ㅇ)
    "A": "k",  # ㅏ
    "U": "j",  # ㅓ
    "O": "h",  # ㅗ
    "AO": "n",  # ㅜ
    "AOU": "m",  # ㅡ
    "AU": "m",  # ㅡ
    "EU": "l",  # ㅣ
    # complex vowels
    "AEU": "o",  # ㅐ
    "AE": "p",  # ㅔ
    # extra/compound
    "E": "ml",  # ㅢ
    "OEU": "hl",  # ㅚ
    "AOU": "nj",  # ㅝ
    "OU": "hk",  # ㅘ
    "AOEU": "nl",  # ㅟ
    "": "",  # empty
}
y_vowels = {
    # "y" vowels
    "A": "i",  # ㅑ
    "U": "u",  # ㅕ
    "O": "y",  # ㅛ
    "OE": "y",  # ㅛ
    "AOU": "b",  # ㅠ
    "AO": "b",  # ㅠ
    "AEU": "O",  # ㅒ
    "AE": "P",  # ㅖ
    "EU": "l",  # ㅣ
    "": "",  # empty
}
ending_consonants = {
    # consonants
    "G": "r",  # ㄱ
    "PB": "s",  # ㄴ
    "D": "e",  # ㄷ
    "R": "f",  # ㄹ
    "L": "f",  # ㄹ
    "PL": "a",  # ㅁ
    "B": "q",  # ㅂ
    "S": "t",  # ㅅ
    "PBG": "d",  # ㅇ
    "PBLG": "w",  # ㅈ
    "FP": "c",  # ㅊ
    "BG": "z",  # ㅋ
    "T": "x",  # ㅌ
    "P": "v",  # ㅍ
    "F": "g",  # ㅎ
    # tense consonants (add -R)
    "RG": "R",  # ㄲ
    "RD": "E",  # ㄸ
    "RB": "Q",  # ㅃ
    "RPBLG": "W",  # ㅉ
    "RS": "T",  # ㅆ
    "Z": "T",  # ㅆ
    "": "",  # empty
}
```

## How you can contribute

Some features that can improve this idea:

- Chording Ability
- Use hgtk python library, or other suitable solution, to output Korean letters without using the "system keyboard layout" work around.
