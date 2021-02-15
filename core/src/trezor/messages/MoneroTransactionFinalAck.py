# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroTransactionFinalAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 518

    def __init__(
        self,
        *,
        cout_key: bytes = None,
        salt: bytes = None,
        rand_mult: bytes = None,
        tx_enc_keys: bytes = None,
        opening_key: bytes = None,
    ) -> None:
        self.cout_key = cout_key
        self.salt = salt
        self.rand_mult = rand_mult
        self.tx_enc_keys = tx_enc_keys
        self.opening_key = opening_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('cout_key', p.BytesType, None),
            2: ('salt', p.BytesType, None),
            3: ('rand_mult', p.BytesType, None),
            4: ('tx_enc_keys', p.BytesType, None),
            5: ('opening_key', p.BytesType, None),
        }
