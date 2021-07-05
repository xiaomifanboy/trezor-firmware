# Automatically generated by pb2py
# fmt: off
# isort:skip_file
from .. import protobuf as p

from .MoneroTransactionDestinationEntry import MoneroTransactionDestinationEntry
from .MoneroTransactionRsigData import MoneroTransactionRsigData

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroTransactionSetOutputRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 511

    def __init__(
        self,
        *,
        dst_entr: Optional[MoneroTransactionDestinationEntry] = None,
        dst_entr_hmac: Optional[bytes] = None,
        rsig_data: Optional[MoneroTransactionRsigData] = None,
        is_offloaded_bp: Optional[bool] = None,
    ) -> None:
        self.dst_entr = dst_entr
        self.dst_entr_hmac = dst_entr_hmac
        self.rsig_data = rsig_data
        self.is_offloaded_bp = is_offloaded_bp

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('dst_entr', MoneroTransactionDestinationEntry, None),
            2: ('dst_entr_hmac', p.BytesType, None),
            3: ('rsig_data', MoneroTransactionRsigData, None),
            4: ('is_offloaded_bp', p.BoolType, None),
        }
