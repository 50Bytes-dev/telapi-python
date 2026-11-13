from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat import Chat


T = TypeVar("T", bound="ChatResponse")


@_attrs_define
class ChatResponse:
    """
    Attributes:
        success (bool):
        chat (Chat): A chat. `type`: `user`, `bot`, `group` (basic group or supergroup),
            `channel` (broadcast channel); new values may come. `about`,
            `blocked`, `linkedChatId` and `slowmodeSeconds` come only with the
            full view (`GET /chats/{chatId}`, `PATCH /chats/{chatId}`).

            `canWrite` is what Telegram's objects show, not a promise: left,
            removed, deactivated or migrated → `chat_closed`; a broadcast channel
            without the right to post → `not_admin`; a group whose rights (for
            all or for the account) ban sending, the account no admin →
            `restricted`; a deleted account → `deleted_user`; a user the account
            blocked → `blocked` (full view only); a user who takes messages only
            from contacts and Premium users, while the account has no Premium,
            is no mutual contact and has had no message from them →
            `premium_required`.
    """

    success: bool
    chat: Chat
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        chat = self.chat.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "chat": chat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat import Chat

        d = dict(src_dict)
        success = d.pop("success")

        chat = Chat.from_dict(d.pop("chat"))

        chat_response = cls(
            success=success,
            chat=chat,
        )

        chat_response.additional_properties = d
        return chat_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
