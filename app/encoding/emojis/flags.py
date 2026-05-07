from ...base.encoder import Encoder
from ..fun.bits import bits_chunk_encode, bits_chunk_decode

_COUNTRIES = [
    'US','GB','CA','AU','DE','FR','IT','ES','PT','NL','BE','CH','SE','NO','DK','FI',
    'JP','KR','CN','IN','BR','MX','AR','CL','CO','PE','ZA','EG','NG','KE','MA','DZ',
    'RU','TR','SA','AE','IL','IQ','IR','PK','BD','TH','VN','PH','ID','MY','SG','TW',
    'PL','CZ','HU','RO','BG','GR','HR','RS','UA','AT','IE','SK','SI','LT','LV','EE',
    'NZ','CU','DO','PR','GT','HN','SV','CR','PA','JM','TT','BS','BB','GY','UY',
    'PY','BO','EC','VE','NI','LU','MT','CY','IS','FO','GL','LI','MC','SM','VA','AD',
    'AF','AM','AZ','BH','BN','KH','GE','JO','KZ','KW','KG','LA','LB','MV','MN','MM',
    'NP','OM','QA','LK','SY','TJ','TL','TM','UZ','YE','BY','BA','MD','MK','ME','AL',
    'ET',
]

_FLAGS = [
    chr(0x1F1E6 + ord(c[0]) - ord('A')) + chr(0x1F1E6 + ord(c[1]) - ord('A'))
    for c in _COUNTRIES
]


class FlagsEncoder(Encoder):
    name = "Flags"

    def encode(self, data: bytes) -> str:
        return bits_chunk_encode(data, _FLAGS, 7)

    def decode(self, text: str) -> bytes:
        return bits_chunk_decode(text, _FLAGS, 7)
