from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_media import MessageMedia


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """A message

    Attributes:
        message_id (int):  Example: 4711.
        chat_id (int):  Example: 123456789.
        out (bool): Sent by this account
        date (int): Unix time in seconds
        text (str): The text or the caption ("" = none)
        forwarded (bool):
        sender_id (int | Unset): The sending user (absent for a channel's posts, this account's own posts included)
        edit_date (int | Unset): Unix time in seconds of the last edit
        reply_to (int | Unset): The id of a message of the same chat that this one answers; absent for a plain message
            in a forum topic, and for a reply to a message of another chat
        grouped_id (str | Unset): Shared by the messages of one album; a decimal string, since the 64-bit id does not
            fit a JSON number exactly Example: 13512445263829514.
        media (MessageMedia | Unset): The media of a message. `type`: `photo`, `video`, `audio`, `voice`, `document`,
            `sticker`, `animation`, `contact`, `location`, `poll`, `webpage`, `other`; new values may come.
    """

    message_id: int
    chat_id: int
    out: bool
    date: int
    text: str
    forwarded: bool
    sender_id: int | Unset = UNSET
    edit_date: int | Unset = UNSET
    reply_to: int | Unset = UNSET
    grouped_id: str | Unset = UNSET
    media: MessageMedia | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        chat_id = self.chat_id

        out = self.out

        date = self.date

        text = self.text

        forwarded = self.forwarded

        sender_id = self.sender_id

        edit_date = self.edit_date

        reply_to = self.reply_to

        grouped_id = self.grouped_id

        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageId": message_id,
                "chatId": chat_id,
                "out": out,
                "date": date,
                "text": text,
                "forwarded": forwarded,
            }
        )
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if edit_date is not UNSET:
            field_dict["editDate"] = edit_date
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if grouped_id is not UNSET:
            field_dict["groupedId"] = grouped_id
        if media is not UNSET:
            field_dict["media"] = media

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_media import MessageMedia

        d = dict(src_dict)
        message_id = d.pop("messageId")

        chat_id = d.pop("chatId")

        out = d.pop("out")

        date = d.pop("date")

        text = d.pop("text")

        forwarded = d.pop("forwarded")

        sender_id = d.pop("senderId", UNSET)

        edit_date = d.pop("editDate", UNSET)

        reply_to = d.pop("replyTo", UNSET)

        grouped_id = d.pop("groupedId", UNSET)

        _media = d.pop("media", UNSET)
        media: MessageMedia | Unset
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = MessageMedia.from_dict(_media)

        message = cls(
            message_id=message_id,
            chat_id=chat_id,
            out=out,
            date=date,
            text=text,
            forwarded=forwarded,
            sender_id=sender_id,
            edit_date=edit_date,
            reply_to=reply_to,
            grouped_id=grouped_id,
            media=media,
        )

        message.additional_properties = d
        return message

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
