# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeInputScriptType = Literal[0, 1, 2, 3, 4]
    except ImportError:
        pass


class SignMessage(p.MessageType):
    MESSAGE_WIRE_TYPE = 38

    def __init__(
        self,
        *,
        message: bytes,
        address_n: List[int] = None,
        coin_name: str = "Bitcoin",
        script_type: EnumTypeInputScriptType = 0,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.message = message
        self.coin_name = coin_name
        self.script_type = script_type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('message', p.BytesType, p.FLAG_REQUIRED),
            3: ('coin_name', p.UnicodeType, "Bitcoin"),  # default=Bitcoin
            4: ('script_type', p.EnumType("InputScriptType", (0, 1, 2, 3, 4)), 0),  # default=SPENDADDRESS
        }
