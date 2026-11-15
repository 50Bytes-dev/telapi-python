from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatBannedRights")


@_attrs_define
class ChatBannedRights:
    """Telegram's rights of a group member: each right is `true` where it
    is taken away, and every right is always present. `untilDate` comes
    only with `bannedRights`, and only when the restriction or ban ends
    (absent means forever).

        Attributes:
            view_messages (bool): Banned from the chat
            send_messages (bool): No messages at all
            send_media (bool): No media (older apps' single switch)
            send_stickers (bool):
            send_gifs (bool):
            send_games (bool):
            send_inline (bool):
            embed_links (bool):
            send_polls (bool):
            change_info (bool):
            invite_users (bool):
            pin_messages (bool):
            manage_topics (bool):
            send_photos (bool):
            send_videos (bool):
            send_roundvideos (bool):
            send_audios (bool):
            send_voices (bool):
            send_docs (bool):
            send_plain (bool): No text messages
            send_reactions (bool):
            edit_rank (bool):
            manage_linked_peers (bool):
            until_date (int | Unset): `bannedRights` only: Unix time when the restriction or ban ends; absent means forever
    """

    view_messages: bool
    send_messages: bool
    send_media: bool
    send_stickers: bool
    send_gifs: bool
    send_games: bool
    send_inline: bool
    embed_links: bool
    send_polls: bool
    change_info: bool
    invite_users: bool
    pin_messages: bool
    manage_topics: bool
    send_photos: bool
    send_videos: bool
    send_roundvideos: bool
    send_audios: bool
    send_voices: bool
    send_docs: bool
    send_plain: bool
    send_reactions: bool
    edit_rank: bool
    manage_linked_peers: bool
    until_date: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        view_messages = self.view_messages

        send_messages = self.send_messages

        send_media = self.send_media

        send_stickers = self.send_stickers

        send_gifs = self.send_gifs

        send_games = self.send_games

        send_inline = self.send_inline

        embed_links = self.embed_links

        send_polls = self.send_polls

        change_info = self.change_info

        invite_users = self.invite_users

        pin_messages = self.pin_messages

        manage_topics = self.manage_topics

        send_photos = self.send_photos

        send_videos = self.send_videos

        send_roundvideos = self.send_roundvideos

        send_audios = self.send_audios

        send_voices = self.send_voices

        send_docs = self.send_docs

        send_plain = self.send_plain

        send_reactions = self.send_reactions

        edit_rank = self.edit_rank

        manage_linked_peers = self.manage_linked_peers

        until_date = self.until_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "viewMessages": view_messages,
                "sendMessages": send_messages,
                "sendMedia": send_media,
                "sendStickers": send_stickers,
                "sendGifs": send_gifs,
                "sendGames": send_games,
                "sendInline": send_inline,
                "embedLinks": embed_links,
                "sendPolls": send_polls,
                "changeInfo": change_info,
                "inviteUsers": invite_users,
                "pinMessages": pin_messages,
                "manageTopics": manage_topics,
                "sendPhotos": send_photos,
                "sendVideos": send_videos,
                "sendRoundvideos": send_roundvideos,
                "sendAudios": send_audios,
                "sendVoices": send_voices,
                "sendDocs": send_docs,
                "sendPlain": send_plain,
                "sendReactions": send_reactions,
                "editRank": edit_rank,
                "manageLinkedPeers": manage_linked_peers,
            }
        )
        if until_date is not UNSET:
            field_dict["untilDate"] = until_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        view_messages = d.pop("viewMessages")

        send_messages = d.pop("sendMessages")

        send_media = d.pop("sendMedia")

        send_stickers = d.pop("sendStickers")

        send_gifs = d.pop("sendGifs")

        send_games = d.pop("sendGames")

        send_inline = d.pop("sendInline")

        embed_links = d.pop("embedLinks")

        send_polls = d.pop("sendPolls")

        change_info = d.pop("changeInfo")

        invite_users = d.pop("inviteUsers")

        pin_messages = d.pop("pinMessages")

        manage_topics = d.pop("manageTopics")

        send_photos = d.pop("sendPhotos")

        send_videos = d.pop("sendVideos")

        send_roundvideos = d.pop("sendRoundvideos")

        send_audios = d.pop("sendAudios")

        send_voices = d.pop("sendVoices")

        send_docs = d.pop("sendDocs")

        send_plain = d.pop("sendPlain")

        send_reactions = d.pop("sendReactions")

        edit_rank = d.pop("editRank")

        manage_linked_peers = d.pop("manageLinkedPeers")

        until_date = d.pop("untilDate", UNSET)

        chat_banned_rights = cls(
            view_messages=view_messages,
            send_messages=send_messages,
            send_media=send_media,
            send_stickers=send_stickers,
            send_gifs=send_gifs,
            send_games=send_games,
            send_inline=send_inline,
            embed_links=embed_links,
            send_polls=send_polls,
            change_info=change_info,
            invite_users=invite_users,
            pin_messages=pin_messages,
            manage_topics=manage_topics,
            send_photos=send_photos,
            send_videos=send_videos,
            send_roundvideos=send_roundvideos,
            send_audios=send_audios,
            send_voices=send_voices,
            send_docs=send_docs,
            send_plain=send_plain,
            send_reactions=send_reactions,
            edit_rank=edit_rank,
            manage_linked_peers=manage_linked_peers,
            until_date=until_date,
        )

        chat_banned_rights.additional_properties = d
        return chat_banned_rights

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
