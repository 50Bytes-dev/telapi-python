from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pause import Pause
    from ..models.tg_user import TgUser


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """An account of the gateway as the admin sees it; never its token or webhook secret.

    Attributes:
        id (UUID):  Example: 6f1c2d4e-8a7b-4c3d-9e2f-1a2b3c4d5e6f.
        name (str): Also shown in Telegram's device list after the login Example: sales-1.
        webhook_url (str): "" = no webhook Example: https://example.com/telegram/events.
        events (list[str]): The subscription (event types; `All` = every one) Example: ['Message', 'LoginUpdated'].
        proxy (str): The proxy of the account's Telegram traffic with its password or secret masked; "" = none of its
            own (`TELAPI_DEFAULT_PROXY` when the gateway sets one, direct otherwise) Example:
            socks5://user:***@10.0.0.5:1080.
        uses_default_proxy (bool): The account connects through the gateway's `TELAPI_DEFAULT_PROXY`, since it has no
            proxy of its own and the gateway sets one; false with `proxy` "" means direct. Only the fact is shown, never the
            default proxy itself
        logged_in (bool): A Telegram login is stored
        connected (bool): The Telegram client is connected
        created_at (int): Unix time in seconds Example: 1794500000.
        tg_user (TgUser | Unset): The Telegram user the account is logged into
        pause (Pause | Unset): The pause of the Telegram user. `reason`: `spam` (PEER_FLOOD,
            USER_RESTRICTED, or USER_BANNED_IN_CHANNEL in 3 different chats
            within 24 hours), `flood` (a long FLOOD_WAIT, or the third on sends
            within 10 minutes), `frozen` (FROZEN_*: only Telegram's appeal lifts
            it); new reasons may come. Lifted only by `POST /session/resume`.
    """

    id: UUID
    name: str
    webhook_url: str
    events: list[str]
    proxy: str
    uses_default_proxy: bool
    logged_in: bool
    connected: bool
    created_at: int
    tg_user: TgUser | Unset = UNSET
    pause: Pause | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        webhook_url = self.webhook_url

        events = self.events

        proxy = self.proxy

        uses_default_proxy = self.uses_default_proxy

        logged_in = self.logged_in

        connected = self.connected

        created_at = self.created_at

        tg_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tg_user, Unset):
            tg_user = self.tg_user.to_dict()

        pause: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pause, Unset):
            pause = self.pause.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "webhookUrl": webhook_url,
                "events": events,
                "proxy": proxy,
                "usesDefaultProxy": uses_default_proxy,
                "loggedIn": logged_in,
                "connected": connected,
                "createdAt": created_at,
            }
        )
        if tg_user is not UNSET:
            field_dict["tgUser"] = tg_user
        if pause is not UNSET:
            field_dict["pause"] = pause

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pause import Pause
        from ..models.tg_user import TgUser

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        webhook_url = d.pop("webhookUrl")

        events = cast(list[str], d.pop("events"))

        proxy = d.pop("proxy")

        uses_default_proxy = d.pop("usesDefaultProxy")

        logged_in = d.pop("loggedIn")

        connected = d.pop("connected")

        created_at = d.pop("createdAt")

        _tg_user = d.pop("tgUser", UNSET)
        tg_user: TgUser | Unset
        if isinstance(_tg_user, Unset):
            tg_user = UNSET
        else:
            tg_user = TgUser.from_dict(_tg_user)

        _pause = d.pop("pause", UNSET)
        pause: Pause | Unset
        if isinstance(_pause, Unset):
            pause = UNSET
        else:
            pause = Pause.from_dict(_pause)

        account = cls(
            id=id,
            name=name,
            webhook_url=webhook_url,
            events=events,
            proxy=proxy,
            uses_default_proxy=uses_default_proxy,
            logged_in=logged_in,
            connected=connected,
            created_at=created_at,
            tg_user=tg_user,
            pause=pause,
        )

        account.additional_properties = d
        return account

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
