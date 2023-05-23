# Easy Korean With Steno

Intuitive Korean steno with Plover. It is a Python dictionary and requires the Plover Python Dictionary plugin (get it from the plugin window in Plover). It works on a Macbook, but it is not tested on Windows or Linux.

## Demo

https://youtu.be/Z_MzDxAceqo

## How It Works

Plover outputs English/qwerty letters and your computer translates them into Korean letters using the built-in system Korean keyboard layout.

1. Toggle dictionary on when in use. Toggle the dictionary off when not in use.
2. Change computer keyboard layout to Korean. Get the Korean keyboard layout in your operating system.
3. Start stenoing Korean intuitively.

> Note: You have to do one letter at a time. Help/feedback is wanted to make chords a reality.

## Learn

```
# consonants
TKPW: ㄱ
TPH: ㄴ
TK: ㄷ
R: ㄹ
HR: ㄹ
PH: ㅁ
PW: ㅂ
S: ㅅ
KWR: ㄷ
SKWR: ㅈ
KH: ㅊ
K: ㅋ
T: ㅌ
P: ㅍ
H: ㅎ

# tense consonants
TKPW*: ㄲ
TH: ㄸ
TK*: ㄸ
PW*: ㅃ
SKWR*: ㅉ
S*: ㅆ

# vowels
A: ㅏ
KWRA: ㅑ
U: ㅓ
KWRU: ㅕ
O: ㅗ
KWRO: ㅛ
AOU: ㅜ
AO: ㅠ
KWRAOU: ㅜ
KWRAO: ㅠ
*U: ㅡ
EU: ㅣ

# complex vowels
AEU: ㅐ
A*EU: ㅔ
KWRAEU: ㅒ
KWRA*EU: ㅖ
```

## How you can contribute

Some features that can improve this idea:

- Chording Ability
- Use hgtk python library, or other suitable solution, to output Korean letters without using the "system keyboard layout" work around.
