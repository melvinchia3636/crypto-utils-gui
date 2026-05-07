from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_DESERET = "𐐀𐐁𐐂𐐃𐐄𐐅𐐆𐐇𐐈𐐉𐐊𐐋𐐌𐐍𐐎𐐏𐐐𐐑𐐒𐐓𐐔𐐕𐐖𐐗𐐘𐐙𐐚𐐛𐐜𐐝𐐞𐐟"


class DeseretEncoder(Encoder):
    name = "Deseret"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _DESERET, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _DESERET, 5)
