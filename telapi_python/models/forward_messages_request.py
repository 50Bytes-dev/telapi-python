from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForwardMessagesRequest")


@_attrs_define
class ForwardMessagesRequest:
    """
    Attributes:
        from_chat_id (int): The chat the messages are in; the account's own id is Saved Messages Example: 123456789.
        message_ids (list[int]): Distinct ids of messages of `fromChatId`, forwarded in this order
        drop_author (bool | Unset): Forward as copies, without the "Forwarded from" header
        drop_captions (bool | Unset): Also drop the captions of media; only with `dropAuthor`
        silent (bool | Unset): No notification sound
        schedule_date (int | Unset): Unix time in seconds; the copies go into the scheduled queue and the answer's ids
            are ids there. 0 or absent forwards now.
        ref (str | Unset): Your idempotency key, as on `POST /messages`
        topic_id (int | Unset): As on `POST /messages`: the forum topic of this chat the messages go into; 1 (General)
            is no topic.
        monoforum_peer_id (int | Unset): As on `POST /messages`: the user's thread of this chat's direct messages.
        send_as (int | Unset): As on `POST /messages`
        allow_paid_stars (int | Unset): As on `POST /messages`: the ceiling for the whole forward, price × the number of
            `messageIds`.
    """

    from_chat_id: int
    message_ids: list[int]
    drop_author: bool | Unset = UNSET
    drop_captions: bool | Unset = UNSET
    silent: bool | Unset = UNSET
    schedule_date: int | Unset = UNSET
    ref: str | Unset = UNSET
    topic_id: int | Unset = UNSET
    monoforum_peer_id: int | Unset = UNSET
    send_as: int | Unset = UNSET
    allow_paid_stars: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_chat_id = self.from_chat_id

        message_ids = self.message_ids

        drop_author = self.drop_author

        drop_captions = self.drop_captions

        silent = self.silent

        schedule_date = self.schedule_date

        ref = self.ref

        topic_id = self.topic_id

        monoforum_peer_id = self.monoforum_peer_id

        send_as = self.send_as

        allow_paid_stars = self.allow_paid_stars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromChatId": from_chat_id,
                "messageIds": message_ids,
            }
        )
        if drop_author is not UNSET:
            field_dict["dropAuthor"] = drop_author
        if drop_captions is not UNSET:
            field_dict["dropCaptions"] = drop_captions
        if silent is not UNSET:
            field_dict["silent"] = silent
        if schedule_date is not UNSET:
            field_dict["scheduleDate"] = schedule_date
        if ref is not UNSET:
            field_dict["ref"] = ref
        if topic_id is not UNSET:
            field_dict["topicId"] = topic_id
        if monoforum_peer_id is not UNSET:
            field_dict["monoforumPeerId"] = monoforum_peer_id
        if send_as is not UNSET:
            field_dict["sendAs"] = send_as
        if allow_paid_stars is not UNSET:
            field_dict["allowPaidStars"] = allow_paid_stars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_chat_id = d.pop("fromChatId")

        message_ids = cast(list[int], d.pop("messageIds"))

        drop_author = d.pop("dropAuthor", UNSET)

        drop_captions = d.pop("dropCaptions", UNSET)

        silent = d.pop("silent", UNSET)

        schedule_date = d.pop("scheduleDate", UNSET)

        ref = d.pop("ref", UNSET)

        topic_id = d.pop("topicId", UNSET)

        monoforum_peer_id = d.pop("monoforumPeerId", UNSET)

        send_as = d.pop("sendAs", UNSET)

        allow_paid_stars = d.pop("allowPaidStars", UNSET)

        forward_messages_request = cls(
            from_chat_id=from_chat_id,
            message_ids=message_ids,
            drop_author=drop_author,
            drop_captions=drop_captions,
            silent=silent,
            schedule_date=schedule_date,
            ref=ref,
            topic_id=topic_id,
            monoforum_peer_id=monoforum_peer_id,
            send_as=send_as,
            allow_paid_stars=allow_paid_stars,
        )

        forward_messages_request.additional_properties = d
        return forward_messages_request

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
