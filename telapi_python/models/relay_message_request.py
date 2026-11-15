from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parse_mode import ParseMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="RelayMessageRequest")


@_attrs_define
class RelayMessageRequest:
    """Exactly one of `chatId`, `phone` and `username`; `text`, `attachments` or both.

    Attributes:
        chat_id (int | Unset):  Example: -1001234567890.
        phone (str | Unset): Digits with the country code; the user must let this account find them by number Example:
            79001234567.
        username (str | Unset): A username, with or without `@`, in any case Example: shop_channel.
        text (str | Unset): The text, or the caption of the first attachment Example: Платье, 1200 ₽.
        parse_mode (ParseMode | Unset): How `text` is marked up; absent sends it as it is. `html` is
            Telegram's HTML style (`<b>`, `<i>`, `<u>`, `<s>`, `<a href>`,
            `<code>`, `<pre>`, `<blockquote>`, `<tg-spoiler>`). `markdown` is
            CommonMark: `**bold**`, `*italic*`, `~~strike~~`, `||spoiler||`,
            `` `code` ``, fenced code blocks, `[text](url)`, `> quote`; other
            constructs stay plain text. A mention (`tg://user?id=…`) of a user
            this account never saw is `404 peer_not_found`.
        attachments (list[str] | Unset): Handles from `POST /media`; 2 to 10 make an album
        silent (bool | Unset): No notification sound
        ref (str | Unset): Your idempotency key (up to 128 bytes); the same `ref` never posts twice Example:
            product-1042.
        topic_id (int | Unset): As on `POST /messages`: the forum topic the forward goes into (1, General, is no topic).
            The copy in Saved Messages has none.
        monoforum_peer_id (int | Unset): As on `POST /messages`: the user's thread of the channel's direct messages the
            forward goes into.
        send_as (int | Unset): As on `POST /messages`: the chat the forward is sent as. The copy in Saved Messages is
            the account's own.
        allow_paid_stars (int | Unset): As on `POST /messages`: the ceiling for the forward into the chat, price ×
            messages (an album of 3 is 3). The copy in Saved Messages is free.
    """

    chat_id: int | Unset = UNSET
    phone: str | Unset = UNSET
    username: str | Unset = UNSET
    text: str | Unset = UNSET
    parse_mode: ParseMode | Unset = UNSET
    attachments: list[str] | Unset = UNSET
    silent: bool | Unset = UNSET
    ref: str | Unset = UNSET
    topic_id: int | Unset = UNSET
    monoforum_peer_id: int | Unset = UNSET
    send_as: int | Unset = UNSET
    allow_paid_stars: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        phone = self.phone

        username = self.username

        text = self.text

        parse_mode: str | Unset = UNSET
        if not isinstance(self.parse_mode, Unset):
            parse_mode = self.parse_mode.value

        attachments: list[str] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        silent = self.silent

        ref = self.ref

        topic_id = self.topic_id

        monoforum_peer_id = self.monoforum_peer_id

        send_as = self.send_as

        allow_paid_stars = self.allow_paid_stars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if username is not UNSET:
            field_dict["username"] = username
        if text is not UNSET:
            field_dict["text"] = text
        if parse_mode is not UNSET:
            field_dict["parseMode"] = parse_mode
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if silent is not UNSET:
            field_dict["silent"] = silent
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
        chat_id = d.pop("chatId", UNSET)

        phone = d.pop("phone", UNSET)

        username = d.pop("username", UNSET)

        text = d.pop("text", UNSET)

        _parse_mode = d.pop("parseMode", UNSET)
        parse_mode: ParseMode | Unset
        if isinstance(_parse_mode, Unset):
            parse_mode = UNSET
        else:
            parse_mode = ParseMode(_parse_mode)

        attachments = cast(list[str], d.pop("attachments", UNSET))

        silent = d.pop("silent", UNSET)

        ref = d.pop("ref", UNSET)

        topic_id = d.pop("topicId", UNSET)

        monoforum_peer_id = d.pop("monoforumPeerId", UNSET)

        send_as = d.pop("sendAs", UNSET)

        allow_paid_stars = d.pop("allowPaidStars", UNSET)

        relay_message_request = cls(
            chat_id=chat_id,
            phone=phone,
            username=username,
            text=text,
            parse_mode=parse_mode,
            attachments=attachments,
            silent=silent,
            ref=ref,
            topic_id=topic_id,
            monoforum_peer_id=monoforum_peer_id,
            send_as=send_as,
            allow_paid_stars=allow_paid_stars,
        )

        relay_message_request.additional_properties = d
        return relay_message_request

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
