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
        sender_id (int | Unset): The sending user (absent for a channel's posts, this account's own posts included, for
            an anonymous admin and for a message sent as a channel; senderChatId names the sender then)
        sender_chat_id (int | Unset): Marked id of the chat that sent the message when no user did: a broadcast
            channel's own post (the channel), an anonymous admin (the group itself) or a message sent as a channel (that
            channel). Never together with senderId Example: -1001234567890.
        edit_date (int | Unset): Unix time in seconds of the last edit
        reply_to (int | Unset): The id of a message of the same chat that this one answers; absent for a plain message
            in a forum topic, and for a reply to a message of another chat. Never the topic itself (topicId)
        topic_id (int | Unset): Forum supergroups only. The topic, which is the id of the message that opened it, or 1
            for General. Absent outside forums (bot chats in threaded mode included), and for a General message of a forum
            the gateway has not seen since it started; a message of any other topic still has it Example: 1.
        monoforum_peer_id (int | Unset): A channel's direct messages (monoforum) only. Marked id of the user (or chat)
            whose conversation with the channel the message belongs to. Absent everywhere else, Saved Messages included
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
    sender_chat_id: int | Unset = UNSET
    edit_date: int | Unset = UNSET
    reply_to: int | Unset = UNSET
    topic_id: int | Unset = UNSET
    monoforum_peer_id: int | Unset = UNSET
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

        sender_chat_id = self.sender_chat_id

        edit_date = self.edit_date

        reply_to = self.reply_to

        topic_id = self.topic_id

        monoforum_peer_id = self.monoforum_peer_id

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
        if sender_chat_id is not UNSET:
            field_dict["senderChatId"] = sender_chat_id
        if edit_date is not UNSET:
            field_dict["editDate"] = edit_date
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if topic_id is not UNSET:
            field_dict["topicId"] = topic_id
        if monoforum_peer_id is not UNSET:
            field_dict["monoforumPeerId"] = monoforum_peer_id
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

        sender_chat_id = d.pop("senderChatId", UNSET)

        edit_date = d.pop("editDate", UNSET)

        reply_to = d.pop("replyTo", UNSET)

        topic_id = d.pop("topicId", UNSET)

        monoforum_peer_id = d.pop("monoforumPeerId", UNSET)

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
            sender_chat_id=sender_chat_id,
            edit_date=edit_date,
            reply_to=reply_to,
            topic_id=topic_id,
            monoforum_peer_id=monoforum_peer_id,
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
