from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_member_result import AddMemberResult
    from ..models.chat import Chat


T = TypeVar("T", bound="CreateChatResponse")


@_attrs_define
class CreateChatResponse:
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
        results (list[AddMemberResult] | Unset): One result per `userIds` entry, in order, when `userIds` were given
    """

    success: bool
    chat: Chat
    results: list[AddMemberResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        chat = self.chat.to_dict()

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "chat": chat,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_member_result import AddMemberResult
        from ..models.chat import Chat

        d = dict(src_dict)
        success = d.pop("success")

        chat = Chat.from_dict(d.pop("chat"))

        _results = d.pop("results", UNSET)
        results: list[AddMemberResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = AddMemberResult.from_dict(results_item_data)

                results.append(results_item)

        create_chat_response = cls(
            success=success,
            chat=chat,
            results=results,
        )

        create_chat_response.additional_properties = d
        return create_chat_response

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
