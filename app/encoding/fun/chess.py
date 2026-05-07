from ...base.encoder import Encoder

from .bits import bits_chunk_encode, bits_chunk_decode

_CHESS = ["♔", "♕", "♖", "♗", "♘", "♙", "♚", "♛"]


class ChessEncoder(Encoder):
    name = "Chess"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _CHESS, 3)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _CHESS, 3)
