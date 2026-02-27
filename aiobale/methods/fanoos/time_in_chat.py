from pydantic import Field
from typing import TYPE_CHECKING, Optional
from ...enums import Services, ChatType
from ...types.responses import DefaultResponse
from ..base import BaleMethod

class TimeInChat(BaleMethod):
    """
    ارسال رویداد time_in_chat به سرویس fanoos
    این رویداد نشان می‌دهد که کاربر چه مدتی در چت سپری کرده است
    """
    __service__ = "bale.fanoos.v1.fanoos"
    __method__ = "Send"
    __returning__ = DefaultResponse

    peer_id: int = Field(..., alias="1")
    peer_type: ChatType = Field(..., alias="2")
    duration_seconds: float = Field(..., alias="3")
    unread_count: Optional[int] = Field(0, alias="4")
    client_name: str = Field("web", alias="5")

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            peer_id: int,
            peer_type: ChatType,
            duration_seconds: float,
            unread_count: int = 0,
            client_name: str = "web",
            **__pydantic_kwargs
        ) -> None:
            super().__init__(
                peer_id=peer_id,
                peer_type=peer_type,
                duration_seconds=duration_seconds,
                unread_count=unread_count,
                client_name=client_name,
                **__pydantic_kwargs
            )
