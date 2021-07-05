# Automatically generated by pb2py
# fmt: off
# isort:skip_file
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosActionBuyRamBytes(p.MessageType):

    def __init__(
        self,
        *,
        payer: Optional[int] = None,
        receiver: Optional[int] = None,
        bytes: Optional[int] = None,
    ) -> None:
        self.payer = payer
        self.receiver = receiver
        self.bytes = bytes

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('payer', p.UVarintType, None),
            2: ('receiver', p.UVarintType, None),
            3: ('bytes', p.UVarintType, None),
        }
