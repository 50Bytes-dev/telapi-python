from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parse_mode import ParseMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMessageRequest")


@_attrs_define
class SendMessageRequest:
    """Exactly one of `chatId`, `phone` and `username`; `text`, `attachments` or both.

    Attributes:
        chat_id (int | Unset):  Example: 123456789.
        phone (str | Unset): Digits with the country code; the user must let this account find them by number Example:
            79001234567.
        username (str | Unset): A username, with or without `@`, in any case Example: anna_p.
        text (str | Unset): The text, or the caption of the first attachment Example: Hello!.
        parse_mode (ParseMode | Unset): How `text` is marked up; absent sends it as it is. `html` is
            Telegram's HTML style (`<b>`, `<i>`, `<u>`, `<s>`, `<a href>`,
            `<code>`, `<pre>`, `<blockquote>`, `<tg-spoiler>`). `markdown` is
            CommonMark: `**bold**`, `*italic*`, `~~strike~~`, `||spoiler||`,
            `` `code` ``, fenced code blocks, `[text](url)`, `> quote`; other
            constructs stay plain text. A mention (`tg://user?id=…`) of a user
            this account never saw is `404 peer_not_found`.
        attachments (list[str] | Unset): Handles from `POST /media`; 2 to 10 make an album
        reply_to (int | Unset): The id of the message to answer
        silent (bool | Unset): No notification sound
        no_webpage (bool | Unset): No link preview
        ref (str | Unset): Your idempotency key (up to 128 bytes); the same `ref` never sends twice Example:
            order-1842-confirmation.
        schedule_date (int | Unset): Unix time in seconds to send the message at; it goes into the chat's scheduled
            queue and the answer's ids are ids in that queue. 0 or absent sends now.
        topic_id (int | Unset): A forum topic of the supergroup (the id of the message that created it). 1 is General,
            which takes messages without a topic. With `replyTo` the reply is made inside the topic. Only into a supergroup
            or channel; not with `monoforumPeerId`. Into a chat this account knows to be no forum it is `400 invalid_input`
            without a call. An unknown topic is `404 topic_invalid`. Example: 42.
        monoforum_peer_id (int | Unset): For an admin of a channel's direct messages (a monoforum): the user whose
            thread the message goes to; with `replyTo` the reply is made in that thread. Only into a channel; not with
            `topicId` or `sendAs`. Into a chat this account knows to be no channel's direct messages it is `400
            invalid_input` without a call. A user this account never saw is `404 monoforum_peer_invalid` without a call.
        send_as (int | Unset): The chat to send as: a chat id from `GET /chats/{chatId}/send-as`, or the account's own
            id. Absent: Telegram decides (the chat's saved `defaultSendAs` may apply). A chat this account never saw is `403
            send_as_invalid` without a call; another user's id is `400 invalid_input`, and so is `sendAs` into a private
            chat, a basic group, or a chat this account knows to be a channel's direct messages (Telegram ignores the sender
            there). Example: -1001234567890.
        allow_paid_stars (int | Unset): The most Telegram Stars the call may spend when the recipient charges for
            messages: the total of the call, price × messages (an album of 3 is 3 messages). 0 or absent never pays: a paid
            recipient answers `402 payment_required`. Telegram charges only what is due. Telegram's apps do not schedule
            paid messages; with `scheduleDate` the gateway passes both and answers what Telegram says. Example: 30.
    """

    chat_id: int | Unset = UNSET
    phone: str | Unset = UNSET
    username: str | Unset = UNSET
    text: str | Unset = UNSET
    parse_mode: ParseMode | Unset = UNSET
    attachments: list[str] | Unset = UNSET
    reply_to: int | Unset = UNSET
    silent: bool | Unset = UNSET
    no_webpage: bool | Unset = UNSET
    ref: str | Unset = UNSET
    schedule_date: int | Unset = UNSET
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

        reply_to = self.reply_to

        silent = self.silent

        no_webpage = self.no_webpage

        ref = self.ref

        schedule_date = self.schedule_date

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
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if silent is not UNSET:
            field_dict["silent"] = silent
        if no_webpage is not UNSET:
            field_dict["noWebpage"] = no_webpage
        if ref is not UNSET:
            field_dict["ref"] = ref
        if schedule_date is not UNSET:
            field_dict["scheduleDate"] = schedule_date
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

        reply_to = d.pop("replyTo", UNSET)

        silent = d.pop("silent", UNSET)

        no_webpage = d.pop("noWebpage", UNSET)

        ref = d.pop("ref", UNSET)

        schedule_date = d.pop("scheduleDate", UNSET)

        topic_id = d.pop("topicId", UNSET)

        monoforum_peer_id = d.pop("monoforumPeerId", UNSET)

        send_as = d.pop("sendAs", UNSET)

        allow_paid_stars = d.pop("allowPaidStars", UNSET)

        send_message_request = cls(
            chat_id=chat_id,
            phone=phone,
            username=username,
            text=text,
            parse_mode=parse_mode,
            attachments=attachments,
            reply_to=reply_to,
            silent=silent,
            no_webpage=no_webpage,
            ref=ref,
            schedule_date=schedule_date,
            topic_id=topic_id,
            monoforum_peer_id=monoforum_peer_id,
            send_as=send_as,
            allow_paid_stars=allow_paid_stars,
        )

        send_message_request.additional_properties = d
        return send_message_request

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
