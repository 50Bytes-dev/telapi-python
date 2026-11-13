from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_code import LoginCode
    from ..models.login_failure import LoginFailure
    from ..models.login_password import LoginPassword
    from ..models.login_qr import LoginQr
    from ..models.tg_user import TgUser


T = TypeVar("T", bound="Login")


@_attrs_define
class Login:
    """The login into Telegram. `step`: `none` (no login ran), `qr` (scan
    `qr`), `code` (send the code), `password` (send the cloud password),
    `done` (`tgUser`; `Connected` follows), `failed` (`failure`). New
    steps may come.

        Attributes:
            step (str):  Example: qr.
            method (str | Unset): `qr` or `phone` Example: qr.
            started_at (int | Unset): Unix time in seconds
            expires_at (int | Unset): Unix time in seconds when the login fails `expired` (`TELAPI_QR_LOGIN_TIMEOUT` after
                the start)
            qr (LoginQr | Unset): Step `qr`: the account's own QR code, renewed about every 30 s. Scan it in Telegram:
                Settings → Devices → Link Desktop Device.
            code (LoginCode | Unset): Step `code`: how Telegram sent the code.
            password (LoginPassword | Unset): Step `password`: two-step verification is on.
            tg_user (TgUser | Unset): The Telegram user the account is logged into
            failure (LoginFailure | Unset): Step `failed`. `reason`: `expired` (timed out, the code expired, or
                five wrong codes or passwords), `cancelled` (a new login or
                `DELETE /session/login`), `rejected` (banned or unregistered number),
                `unavailable` (Telegram refuses the app), `limited` (FLOOD_WAIT on
                login calls; `retryAfterMs`), `failed` (anything else;
                `upstreamCode`), `unsupported` (Telegram asked for a step the gateway
                does not do; `step`). New reasons may come.
    """

    step: str
    method: str | Unset = UNSET
    started_at: int | Unset = UNSET
    expires_at: int | Unset = UNSET
    qr: LoginQr | Unset = UNSET
    code: LoginCode | Unset = UNSET
    password: LoginPassword | Unset = UNSET
    tg_user: TgUser | Unset = UNSET
    failure: LoginFailure | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step

        method = self.method

        started_at = self.started_at

        expires_at = self.expires_at

        qr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qr, Unset):
            qr = self.qr.to_dict()

        code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.to_dict()

        password: dict[str, Any] | Unset = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        tg_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tg_user, Unset):
            tg_user = self.tg_user.to_dict()

        failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure, Unset):
            failure = self.failure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if qr is not UNSET:
            field_dict["qr"] = qr
        if code is not UNSET:
            field_dict["code"] = code
        if password is not UNSET:
            field_dict["password"] = password
        if tg_user is not UNSET:
            field_dict["tgUser"] = tg_user
        if failure is not UNSET:
            field_dict["failure"] = failure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login_code import LoginCode
        from ..models.login_failure import LoginFailure
        from ..models.login_password import LoginPassword
        from ..models.login_qr import LoginQr
        from ..models.tg_user import TgUser

        d = dict(src_dict)
        step = d.pop("step")

        method = d.pop("method", UNSET)

        started_at = d.pop("startedAt", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        _qr = d.pop("qr", UNSET)
        qr: LoginQr | Unset
        if isinstance(_qr, Unset):
            qr = UNSET
        else:
            qr = LoginQr.from_dict(_qr)

        _code = d.pop("code", UNSET)
        code: LoginCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = LoginCode.from_dict(_code)

        _password = d.pop("password", UNSET)
        password: LoginPassword | Unset
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = LoginPassword.from_dict(_password)

        _tg_user = d.pop("tgUser", UNSET)
        tg_user: TgUser | Unset
        if isinstance(_tg_user, Unset):
            tg_user = UNSET
        else:
            tg_user = TgUser.from_dict(_tg_user)

        _failure = d.pop("failure", UNSET)
        failure: LoginFailure | Unset
        if isinstance(_failure, Unset):
            failure = UNSET
        else:
            failure = LoginFailure.from_dict(_failure)

        login = cls(
            step=step,
            method=method,
            started_at=started_at,
            expires_at=expires_at,
            qr=qr,
            code=code,
            password=password,
            tg_user=tg_user,
            failure=failure,
        )

        login.additional_properties = d
        return login

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
