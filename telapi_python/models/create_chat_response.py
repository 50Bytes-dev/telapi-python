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
            `channel` (broadcast channel); new values may come. The fields from
            `about` on come only with the full view (`GET /chats/{chatId}`,
            `PATCH /chats/{chatId}`); the traits before them come from the
            chat's own object, so the list has them too. Boolean traits are
            present only when true.

            `canWrite` is what Telegram's objects show, not a promise, by the
            rules of Telegram's own apps, in this order. A basic group that
            became a supergroup → `migrated` (with `migratedToChatId`); left,
            removed or deleted → `chat_closed`. A supergroup or channel that
            banned the account (`bannedRights.viewMessages`; a ban stays after
            its `untilDate`) → `chat_closed`. A monoforum is never joined and is
            writable unless its channel, in the same answer, no longer takes
            direct messages → `chat_closed`. Left: a discussion group
            (`hasLink`) takes comments without joining unless `joinToSend` is
            on → `join_required`; anything else left → `chat_closed`. A
            gigagroup takes messages from its creator and admins only, a
            broadcast channel from its creator and admins with the right to
            post → `not_admin`. In a supergroup the creator and admins write;
            others are `restricted` while their own restriction lasts (until
            `bannedRights.untilDate`) or the group's default rights restrict,
            which stop holding for an account that boosted the group enough
            (full view only: `boostsApplied` ≥ `boostsUnrestrict` > 0). Rights
            restrict when they ban `sendMessages`, or `sendPlain` and every
            media kind (`sendPhotos`, `sendVideos`, `sendRoundvideos`,
            `sendAudios`, `sendVoices`, `sendDocs`, `sendStickers`, `sendGifs`,
            `sendPolls`). A deleted account → `deleted_user`; a user the
            account blocked → `blocked` (full view only); a user who takes
            messages only from contacts and Premium users, while the account
            has no Premium, is no mutual contact and has had no message from
            them → `premium_required`. Paid messages and slow mode never change
            `canWrite`. New reasons may come.
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
