# Automatically generated by pb2py
# fmt: off
# isort:skip_file
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxOutputBinType(p.MessageType):

    def __init__(
        self,
        *,
        amount: int,
        script_pubkey: bytes,
        decred_script_version: Optional[int] = None,
    ) -> None:
        self.amount = amount
        self.script_pubkey = script_pubkey
        self.decred_script_version = decred_script_version

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('amount', p.UVarintType, p.FLAG_REQUIRED),
            2: ('script_pubkey', p.BytesType, p.FLAG_REQUIRED),
            3: ('decred_script_version', p.UVarintType, None),
        }
