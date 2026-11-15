from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_banned_rights import ChatBannedRights
    from ..models.message import Message


T = TypeVar("T", bound="Chat")


@_attrs_define
class Chat:
    """A chat. `type`: `user`, `bot`, `group` (basic group or supergroup),
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

        Attributes:
            chat_id (int):  Example: -1001234567890.
            type_ (str):  Example: group.
            title (str): The title, or the name of a user or bot Example: Team.
            can_write (bool): The account may send messages here, as far as Telegram's objects show
            unread_count (int):
            pinned (bool):
            muted (bool): Notifications are off now (muted until a time still ahead)
            archived (bool): The chat is in the archive folder
            username (str | Unset):
            user_id (int | Unset): `user` and `bot`: the user id
            members_count (int | Unset): Members of a group or channel, when Telegram tells it
            cant_write_reason (str | Unset): When `canWrite` is false: `chat_closed`, `migrated`, `join_required`,
                `not_admin`, `restricted`, `deleted_user`, `blocked`, `premium_required`; new values may come
            last_message (Message | Unset): A message
            forum (bool | Unset): A supergroup with forum topics
            monoforum (bool | Unset): A channel's direct messages (a monoforum), which the account never joins
            linked_monoforum_id (int | Unset): A channel's monoforum, or a monoforum's channel
            broadcast_messages_allowed (bool | Unset): A broadcast channel takes direct messages (through
                `linkedMonoforumId`)
            gigagroup (bool | Unset): A broadcast group, where only the creator and admins write
            has_link (bool | Unset): A channel with a discussion group, or a discussion group of a channel
            slowmode_enabled (bool | Unset): The group has slow mode (`slowmodeSeconds` in the full view)
            join_to_send (bool | Unset): A discussion group takes messages from members only
            join_request (bool | Unset): Joining needs an admin's approval
            noforwards (bool | Unset): The chat's content is protected from forwarding and copying out of it; it never
                limits sending into the chat or relay. A private chat's comes in the full view only.
            send_paid_messages_stars (int | Unset): The chat charges Stars per message. The list gives the chat's price (a
                user's, a supergroup's, or a channel's direct messages, its monoforum's); the full view gives what this account
                pays instead, `0` when the account is exempt and absent when it pays nothing. Never on a broadcast channel (its
                direct messages are priced on its monoforum). Never changes `canWrite`.
            default_banned_rights (ChatBannedRights | Unset): Telegram's rights of a group member: each right is `true`
                where it
                is taken away, and every right is always present. `untilDate` comes
                only with `bannedRights`, and only when the restriction or ban ends
                (absent means forever).
            banned_rights (ChatBannedRights | Unset): Telegram's rights of a group member: each right is `true` where it
                is taken away, and every right is always present. `untilDate` comes
                only with `bannedRights`, and only when the restriction or ban ends
                (absent means forever).
            migrated_to_chat_id (int | Unset): The supergroup a basic group became
            about (str | Unset): The description of a group or channel, the bio of a user
            blocked (bool | Unset): `user` and `bot`, full view: the account blocked this user
            noforwards_by_me (bool | Unset): `user`, full view: this account protected the private chat
            noforwards_by_peer (bool | Unset): `user`, full view: the other user protected the private chat
            linked_chat_id (int | Unset): The discussion group of a channel, or the channel of a discussion group
            slowmode_seconds (int | Unset):
            slowmode_next_send_date (int | Unset): Full view, Unix time when slow mode lets this account send again; absent
                for the creator, admins and an account that boosted the group enough, whom slow mode does not hold
            migrated_from_chat_id (int | Unset): Full view, the basic group this supergroup was
            default_send_as (int | Unset): Full view, the chat this account sends as by default here; present means the chat
                lets the account choose whom to send as
            boosts_applied (int | Unset): Full view, boosts this account gave the supergroup
            boosts_unrestrict (int | Unset): Full view, boosts after which the group's default restrictions and slow mode no
                longer hold for the account
    """

    chat_id: int
    type_: str
    title: str
    can_write: bool
    unread_count: int
    pinned: bool
    muted: bool
    archived: bool
    username: str | Unset = UNSET
    user_id: int | Unset = UNSET
    members_count: int | Unset = UNSET
    cant_write_reason: str | Unset = UNSET
    last_message: Message | Unset = UNSET
    forum: bool | Unset = UNSET
    monoforum: bool | Unset = UNSET
    linked_monoforum_id: int | Unset = UNSET
    broadcast_messages_allowed: bool | Unset = UNSET
    gigagroup: bool | Unset = UNSET
    has_link: bool | Unset = UNSET
    slowmode_enabled: bool | Unset = UNSET
    join_to_send: bool | Unset = UNSET
    join_request: bool | Unset = UNSET
    noforwards: bool | Unset = UNSET
    send_paid_messages_stars: int | Unset = UNSET
    default_banned_rights: ChatBannedRights | Unset = UNSET
    banned_rights: ChatBannedRights | Unset = UNSET
    migrated_to_chat_id: int | Unset = UNSET
    about: str | Unset = UNSET
    blocked: bool | Unset = UNSET
    noforwards_by_me: bool | Unset = UNSET
    noforwards_by_peer: bool | Unset = UNSET
    linked_chat_id: int | Unset = UNSET
    slowmode_seconds: int | Unset = UNSET
    slowmode_next_send_date: int | Unset = UNSET
    migrated_from_chat_id: int | Unset = UNSET
    default_send_as: int | Unset = UNSET
    boosts_applied: int | Unset = UNSET
    boosts_unrestrict: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        type_ = self.type_

        title = self.title

        can_write = self.can_write

        unread_count = self.unread_count

        pinned = self.pinned

        muted = self.muted

        archived = self.archived

        username = self.username

        user_id = self.user_id

        members_count = self.members_count

        cant_write_reason = self.cant_write_reason

        last_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_message, Unset):
            last_message = self.last_message.to_dict()

        forum = self.forum

        monoforum = self.monoforum

        linked_monoforum_id = self.linked_monoforum_id

        broadcast_messages_allowed = self.broadcast_messages_allowed

        gigagroup = self.gigagroup

        has_link = self.has_link

        slowmode_enabled = self.slowmode_enabled

        join_to_send = self.join_to_send

        join_request = self.join_request

        noforwards = self.noforwards

        send_paid_messages_stars = self.send_paid_messages_stars

        default_banned_rights: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_banned_rights, Unset):
            default_banned_rights = self.default_banned_rights.to_dict()

        banned_rights: dict[str, Any] | Unset = UNSET
        if not isinstance(self.banned_rights, Unset):
            banned_rights = self.banned_rights.to_dict()

        migrated_to_chat_id = self.migrated_to_chat_id

        about = self.about

        blocked = self.blocked

        noforwards_by_me = self.noforwards_by_me

        noforwards_by_peer = self.noforwards_by_peer

        linked_chat_id = self.linked_chat_id

        slowmode_seconds = self.slowmode_seconds

        slowmode_next_send_date = self.slowmode_next_send_date

        migrated_from_chat_id = self.migrated_from_chat_id

        default_send_as = self.default_send_as

        boosts_applied = self.boosts_applied

        boosts_unrestrict = self.boosts_unrestrict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "type": type_,
                "title": title,
                "canWrite": can_write,
                "unreadCount": unread_count,
                "pinned": pinned,
                "muted": muted,
                "archived": archived,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if members_count is not UNSET:
            field_dict["membersCount"] = members_count
        if cant_write_reason is not UNSET:
            field_dict["cantWriteReason"] = cant_write_reason
        if last_message is not UNSET:
            field_dict["lastMessage"] = last_message
        if forum is not UNSET:
            field_dict["forum"] = forum
        if monoforum is not UNSET:
            field_dict["monoforum"] = monoforum
        if linked_monoforum_id is not UNSET:
            field_dict["linkedMonoforumId"] = linked_monoforum_id
        if broadcast_messages_allowed is not UNSET:
            field_dict["broadcastMessagesAllowed"] = broadcast_messages_allowed
        if gigagroup is not UNSET:
            field_dict["gigagroup"] = gigagroup
        if has_link is not UNSET:
            field_dict["hasLink"] = has_link
        if slowmode_enabled is not UNSET:
            field_dict["slowmodeEnabled"] = slowmode_enabled
        if join_to_send is not UNSET:
            field_dict["joinToSend"] = join_to_send
        if join_request is not UNSET:
            field_dict["joinRequest"] = join_request
        if noforwards is not UNSET:
            field_dict["noforwards"] = noforwards
        if send_paid_messages_stars is not UNSET:
            field_dict["sendPaidMessagesStars"] = send_paid_messages_stars
        if default_banned_rights is not UNSET:
            field_dict["defaultBannedRights"] = default_banned_rights
        if banned_rights is not UNSET:
            field_dict["bannedRights"] = banned_rights
        if migrated_to_chat_id is not UNSET:
            field_dict["migratedToChatId"] = migrated_to_chat_id
        if about is not UNSET:
            field_dict["about"] = about
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if noforwards_by_me is not UNSET:
            field_dict["noforwardsByMe"] = noforwards_by_me
        if noforwards_by_peer is not UNSET:
            field_dict["noforwardsByPeer"] = noforwards_by_peer
        if linked_chat_id is not UNSET:
            field_dict["linkedChatId"] = linked_chat_id
        if slowmode_seconds is not UNSET:
            field_dict["slowmodeSeconds"] = slowmode_seconds
        if slowmode_next_send_date is not UNSET:
            field_dict["slowmodeNextSendDate"] = slowmode_next_send_date
        if migrated_from_chat_id is not UNSET:
            field_dict["migratedFromChatId"] = migrated_from_chat_id
        if default_send_as is not UNSET:
            field_dict["defaultSendAs"] = default_send_as
        if boosts_applied is not UNSET:
            field_dict["boostsApplied"] = boosts_applied
        if boosts_unrestrict is not UNSET:
            field_dict["boostsUnrestrict"] = boosts_unrestrict

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_banned_rights import ChatBannedRights
        from ..models.message import Message

        d = dict(src_dict)
        chat_id = d.pop("chatId")

        type_ = d.pop("type")

        title = d.pop("title")

        can_write = d.pop("canWrite")

        unread_count = d.pop("unreadCount")

        pinned = d.pop("pinned")

        muted = d.pop("muted")

        archived = d.pop("archived")

        username = d.pop("username", UNSET)

        user_id = d.pop("userId", UNSET)

        members_count = d.pop("membersCount", UNSET)

        cant_write_reason = d.pop("cantWriteReason", UNSET)

        _last_message = d.pop("lastMessage", UNSET)
        last_message: Message | Unset
        if isinstance(_last_message, Unset):
            last_message = UNSET
        else:
            last_message = Message.from_dict(_last_message)

        forum = d.pop("forum", UNSET)

        monoforum = d.pop("monoforum", UNSET)

        linked_monoforum_id = d.pop("linkedMonoforumId", UNSET)

        broadcast_messages_allowed = d.pop("broadcastMessagesAllowed", UNSET)

        gigagroup = d.pop("gigagroup", UNSET)

        has_link = d.pop("hasLink", UNSET)

        slowmode_enabled = d.pop("slowmodeEnabled", UNSET)

        join_to_send = d.pop("joinToSend", UNSET)

        join_request = d.pop("joinRequest", UNSET)

        noforwards = d.pop("noforwards", UNSET)

        send_paid_messages_stars = d.pop("sendPaidMessagesStars", UNSET)

        _default_banned_rights = d.pop("defaultBannedRights", UNSET)
        default_banned_rights: ChatBannedRights | Unset
        if isinstance(_default_banned_rights, Unset):
            default_banned_rights = UNSET
        else:
            default_banned_rights = ChatBannedRights.from_dict(_default_banned_rights)

        _banned_rights = d.pop("bannedRights", UNSET)
        banned_rights: ChatBannedRights | Unset
        if isinstance(_banned_rights, Unset):
            banned_rights = UNSET
        else:
            banned_rights = ChatBannedRights.from_dict(_banned_rights)

        migrated_to_chat_id = d.pop("migratedToChatId", UNSET)

        about = d.pop("about", UNSET)

        blocked = d.pop("blocked", UNSET)

        noforwards_by_me = d.pop("noforwardsByMe", UNSET)

        noforwards_by_peer = d.pop("noforwardsByPeer", UNSET)

        linked_chat_id = d.pop("linkedChatId", UNSET)

        slowmode_seconds = d.pop("slowmodeSeconds", UNSET)

        slowmode_next_send_date = d.pop("slowmodeNextSendDate", UNSET)

        migrated_from_chat_id = d.pop("migratedFromChatId", UNSET)

        default_send_as = d.pop("defaultSendAs", UNSET)

        boosts_applied = d.pop("boostsApplied", UNSET)

        boosts_unrestrict = d.pop("boostsUnrestrict", UNSET)

        chat = cls(
            chat_id=chat_id,
            type_=type_,
            title=title,
            can_write=can_write,
            unread_count=unread_count,
            pinned=pinned,
            muted=muted,
            archived=archived,
            username=username,
            user_id=user_id,
            members_count=members_count,
            cant_write_reason=cant_write_reason,
            last_message=last_message,
            forum=forum,
            monoforum=monoforum,
            linked_monoforum_id=linked_monoforum_id,
            broadcast_messages_allowed=broadcast_messages_allowed,
            gigagroup=gigagroup,
            has_link=has_link,
            slowmode_enabled=slowmode_enabled,
            join_to_send=join_to_send,
            join_request=join_request,
            noforwards=noforwards,
            send_paid_messages_stars=send_paid_messages_stars,
            default_banned_rights=default_banned_rights,
            banned_rights=banned_rights,
            migrated_to_chat_id=migrated_to_chat_id,
            about=about,
            blocked=blocked,
            noforwards_by_me=noforwards_by_me,
            noforwards_by_peer=noforwards_by_peer,
            linked_chat_id=linked_chat_id,
            slowmode_seconds=slowmode_seconds,
            slowmode_next_send_date=slowmode_next_send_date,
            migrated_from_chat_id=migrated_from_chat_id,
            default_send_as=default_send_as,
            boosts_applied=boosts_applied,
            boosts_unrestrict=boosts_unrestrict,
        )

        chat.additional_properties = d
        return chat

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
