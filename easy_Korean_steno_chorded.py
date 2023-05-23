# You need to use this with the Korean keyboard layout on your computer enabled

import re

LONGEST_KEY = 1

# list of keys for consonants and vowels
starting_consonants = {
    "regular": {
        # consonants
        "K": "r",  # ㄱ
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
        "": "d",  # ㅇ
    },
    "tense": {
        # tense consonants (add *)
        "K*": "R",  # ㄲ
        "TH": "E",  # ㄸ
        "TH*": "E",  # ㄸ
        "TK*": "E",  # ㄸ
        "PW*": "Q",  # ㅃ
        "SKWR*": "W",  # ㅉ
        "S*": "T",  # ㅆ
    },
    "special": {
        # adds "y" to vowels
        "KW": "r",  # ㄱ
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
        "STKPWHR": "",
    },
}
vowels = {
    # vowels
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
    "E": "ml",  # ㅢ
    "": "",
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
    "": "",
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
    "": "",  #
}


def lookup(chord):
    stroke = chord[0]
    if len(chord) != 1:
        raise KeyError
    assert len(chord) <= LONGEST_KEY
    # backspacing
    if stroke == "*":
        return "{#right}{#backspace}"
    # the regex decomposes a stroke into the following groups/variables:
    # start consonants               #STKPWHR
    # vowel 1                                 AO
    # stress start consonants                    */-
    # vowel 2                                        EU
    # end consonants                                    FRPBLGTSDZ
    match = re.fullmatch(r"([#STKPWHR]*)([AO]*)([*-]?)([EU]*)([FRPBLGTSDZ]*)", stroke)

    if match is None:
        raise KeyError
    (
        start_consonant,
        vowel1,
        stress,
        vowel2,
        end_consonant,
    ) = match.groups()

    # get start consonant
    add_y = False
    if start_consonant in starting_consonants["regular"]:
        start_final = starting_consonants["regular"][start_consonant]
    elif start_consonant in starting_consonants["special"]:
        add_y = True
        start_final = starting_consonants["special"][start_consonant]
    # detect stress
    elif start_consonant + stress in starting_consonants["tense"]:
        start_final = starting_consonants["tense"][start_consonant]
    else:
        raise KeyError

    # get vowel
    vowel = vowel1 + vowel2
    if vowel not in vowels and vowel not in y_vowels:
        raise KeyError
    if start_consonant in starting_consonants["special"] and not vowel:
        raise KeyError
    if add_y:
        vowel_final = y_vowels[vowel]
    else:
        vowel_final = vowels[vowel]

    # only vowel output using *
    if stress == "*" and start_consonant == "":
        start_final = ""

    # get end consonant
    if end_consonant not in ending_consonants:
        raise KeyError
    # only end output
    if end_consonant and start_consonant == "":
        start_final = ""

    # combine output
    output = (
        "{^}" + start_final + vowel_final + ending_consonants[end_consonant] + "{^}"
    )
    return output
