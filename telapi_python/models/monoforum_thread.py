from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="MonoforumThread")


@_attrs_define
class MonoforumThread:
    """The conversation of one user with a channel's direct messages (a
    monoforum), as the channel's admins see it. `monoforumPeerId` is the
    user, and the value a send's `monoforumPeerId` takes to answer them.

        Attributes:
            monoforum_peer_id (int): The user's chat id
            title (str): The user's name
            unread_count (int):
            last_message (Message | Unset): A message
    """

    monoforum_peer_id: int
    title: str
    unread_count: int
    last_message: Message | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monoforum_peer_id = self.monoforum_peer_id

        title = self.title

        unread_count = self.unread_count

        last_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_message, Unset):
            last_message = self.last_message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monoforumPeerId": monoforum_peer_id,
                "title": title,
                "unreadCount": unread_count,
            }
        )
        if last_message is not UNSET:
            field_dict["lastMessage"] = last_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message

        d = dict(src_dict)
        monoforum_peer_id = d.pop("monoforumPeerId")

        title = d.pop("title")

        unread_count = d.pop("unreadCount")

        _last_message = d.pop("lastMessage", UNSET)
        last_message: Message | Unset
        if isinstance(_last_message, Unset):
            last_message = UNSET
        else:
            last_message = Message.from_dict(_last_message)

        monoforum_thread = cls(
            monoforum_peer_id=monoforum_peer_id,
            title=title,
            unread_count=unread_count,
            last_message=last_message,
        )

        monoforum_thread.additional_properties = d
        return monoforum_thread

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
