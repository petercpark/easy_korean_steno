# You need to use this with the Korean keyboard layout on your computer enabled

LONGEST_KEY = 1

# list of keys for consonants and vowels
strokes = {
    # consonants
    "TKPW": "r",  # ㄱ
    "TPH": "s",  # ㄴ
    "TK": "e",  # ㄷ
    "R": "f",  # ㄹ
    "HR": "f",  # ㄹ
    "PH": "a",  # ㅁ
    "PW": "q",  # ㅂ
    "S": "t",  # ㅅ
    "KWR": "d",  # ㄷ
    "SKWR": "w",  # ㅈ
    "KH": "c",  # ㅊ
    "K": "z",  # ㅋ
    "T": "x",  # ㅌ
    "P": "v",  # ㅍ
    "H": "g",  # ㅎ
    # tense consonants #
    "TKPW*": "R",  # ㄲ
    "TH": "E",  # ㄸ
    "TK*": "E",  # ㄸ
    "PW*": "Q",  # ㅃ
    "SKWR*": "W",  # ㅉ
    "S*": "T",  # ㅆ
    # vowels
    "A": "k",  # ㅏ
    "KWRA": "i",  # ㅑ
    "U": "j",  # ㅓ
    "KWRU": "u",  # ㅕ
    "O": "h",  # ㅗ
    "KWRO": "y",  # ㅛ
    "AOU": "n",  # ㅜ
    "AO": "n",  # ㅠ
    "KWRAOU": "b",  # ㅜ
    "KWRAO": "b",  # ㅠ
    "*U": "m",  # ㅡ
    "EU": "l",  # ㅣ
    # complex vowels
    "AEU": "o",  # ㅐ
    "A*EU": "p",  # ㅔ
    "KWRAEU": "O",  # ㅒ
    "KWRA*EU": "P",  # ㅖ
}


def lookup(outline):
    assert len(outline) <= LONGEST_KEY
    str = outline[0]
    # KeyError if first stroke is not one of the modifiers
    if str not in strokes:
        raise KeyError

    key = "{^}" + strokes[str] + "{^}"

    return key
