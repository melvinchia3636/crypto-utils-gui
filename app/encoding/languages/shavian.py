from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_SHAVIAN = "𐑐𐑑𐑒𐑓𐑔𐑕𐑖𐑗𐑘𐑙𐑚𐑛𐑜𐑝𐑞𐑟𐑠𐑡𐑢𐑣𐑤𐑥𐑦𐑧𐑨𐑩𐑪𐑫𐑬𐑭𐑮𐑯"


class ShavianEncoder(Encoder):
    name = "Shavian"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _SHAVIAN, 5)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _SHAVIAN, 5)
