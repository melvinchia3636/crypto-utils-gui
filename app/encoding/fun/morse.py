from ...base.encoder import Encoder

_MORSE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}
_REV_MORSE = {v: k for k, v in _MORSE.items()}


class MorseEncoder(Encoder):
    name = "Morse"

    def encode(self, data: bytes) -> str:
        s = data.hex()
        return " ".join(_MORSE.get(c, "?") for c in s)

    def decode(self, text: str) -> bytes:
        hex_str = "".join(_REV_MORSE.get(m, "00") for m in text.strip().split())
        return bytes.fromhex(hex_str)
