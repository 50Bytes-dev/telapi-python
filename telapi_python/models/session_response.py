from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login import Login
    from ..models.pause import Pause
    from ..models.tg_user import TgUser


T = TypeVar("T", bound="SessionResponse")


@_attrs_define
class SessionResponse:
    """
    Attributes:
        success (bool):
        logged_in (bool): A Telegram login is stored
        connected (bool): The Telegram client is connected
        tg_user (TgUser | Unset): The Telegram user the account is logged into
        login (Login | Unset): The login into Telegram. `step`: `none` (no login ran), `qr` (scan
            `qr`), `code` (send the code), `password` (send the cloud password),
            `done` (`tgUser`; `Connected` follows), `failed` (`failure`). New
            steps may come.
        pause (Pause | Unset): The pause of the Telegram user. `reason`: `spam` (PEER_FLOOD,
            USER_RESTRICTED, or USER_BANNED_IN_CHANNEL in 3 different chats
            within 24 hours), `flood` (a long FLOOD_WAIT, or the third on sends
            within 10 minutes), `frozen` (FROZEN_*: only Telegram's appeal lifts
            it); new reasons may come. Lifted only by `POST /session/resume`.
    """

    success: bool
    logged_in: bool
    connected: bool
    tg_user: TgUser | Unset = UNSET
    login: Login | Unset = UNSET
    pause: Pause | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        logged_in = self.logged_in

        connected = self.connected

        tg_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tg_user, Unset):
            tg_user = self.tg_user.to_dict()

        login: dict[str, Any] | Unset = UNSET
        if not isinstance(self.login, Unset):
            login = self.login.to_dict()

        pause: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pause, Unset):
            pause = self.pause.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "loggedIn": logged_in,
                "connected": connected,
            }
        )
        if tg_user is not UNSET:
            field_dict["tgUser"] = tg_user
        if login is not UNSET:
            field_dict["login"] = login
        if pause is not UNSET:
            field_dict["pause"] = pause

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login import Login
        from ..models.pause import Pause
        from ..models.tg_user import TgUser

        d = dict(src_dict)
        success = d.pop("success")

        logged_in = d.pop("loggedIn")

        connected = d.pop("connected")

        _tg_user = d.pop("tgUser", UNSET)
        tg_user: TgUser | Unset
        if isinstance(_tg_user, Unset):
            tg_user = UNSET
        else:
            tg_user = TgUser.from_dict(_tg_user)

        _login = d.pop("login", UNSET)
        login: Login | Unset
        if isinstance(_login, Unset):
            login = UNSET
        else:
            login = Login.from_dict(_login)

        _pause = d.pop("pause", UNSET)
        pause: Pause | Unset
        if isinstance(_pause, Unset):
            pause = UNSET
        else:
            pause = Pause.from_dict(_pause)

        session_response = cls(
            success=success,
            logged_in=logged_in,
            connected=connected,
            tg_user=tg_user,
            login=login,
            pause=pause,
        )

        session_response.additional_properties = d
        return session_response

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
