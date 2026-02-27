from pydantic import Field
from typing import TYPE_CHECKING
from ...enums import Services, ChatType
from ...types.responses import DefaultResponse
from ..base import BaleMethod

class OpenDialogue(BaleMethod):
    """
    ارسال رویداد OpenDialogue به سرویس fanoos
    این رویداد نشان می‌دهد که کاربر یک چت را باز کرده است
    """
    __service__ = "bale.fanoos.v1.fanoos"
    __method__ = "Send"
    __returning__ = DefaultResponse

    peer_type: ChatType = Field(..., alias="1")
    peer_id: int = Field(..., alias="2")
    client_name: str = Field("web", alias="3")

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            peer_type: ChatType,
            peer_id: int,
            client_name: str = "web",
            **__pydantic_kwargs
        ) -> None:
            super().__init__(
                peer_type=peer_type,
                peer_id=peer_id,
                client_name=client_name,
                **__pydantic_kwargs
            )
