import random

from ...base.encoder import Encoder

_DIT = ["·", "•", "●", "∙", "⋅", "●", "⬤", "⊙"]
_DAH = ["−", "—", "━", "▬", "≡", "═", "➖", "⎯"]
_SEP = [" ", " ", " ", " "]

_MORSE = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.",
}

_VISUAL = str.maketrans({".": "{dit}", "-": "{dah}"})


class MorseVisualEncoder(Encoder):
    name = "Morse Visual"

    def encode(self, data: bytes) -> str:
        hex_str = data.hex()
        parts = []
        for ch in hex_str:
            pattern = _MORSE[ch]
            chars = []
            for sym in pattern:
                pool = _DIT if sym == "." else _DAH
                chars.append(random.choice(pool))
            parts.append("".join(chars))
        return random.choice(_SEP).join(parts)

    def decode(self, text: str) -> bytes:
        _ALL = set(_DIT + _DAH)
        _REV = {}
        for d in _DIT:
            _REV[d] = "."
        for d in _DAH:
            _REV[d] = "-"

        letters = []
        current = []
        for c in text:
            if c in _SEP:
                if current:
                    letters.append("".join(current))
                    current = []
            elif c in _ALL:
                current.append(c)
            else:
                _SEP
        if current:
            letters.append("".join(current))

        rev_morse = {v: k for k, v in _MORSE.items()}
        hex_str = "".join(
            rev_morse.get("".join(_REV.get(c, ".") for c in l), "0")
            for l in letters
        )
        return bytes.fromhex(hex_str)
