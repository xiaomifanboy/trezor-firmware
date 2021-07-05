# Automatically generated by pb2py
# fmt: off
# isort:skip_file
import protobuf as p

from .EosPermissionLevel import EosPermissionLevel

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosAuthorizationAccount(p.MessageType):

    def __init__(
        self,
        *,
        account: Optional[EosPermissionLevel] = None,
        weight: Optional[int] = None,
    ) -> None:
        self.account = account
        self.weight = weight

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('account', EosPermissionLevel, None),
            2: ('weight', p.UVarintType, None),
        }
