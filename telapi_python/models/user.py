from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_status import UserStatus


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """A Telegram user

    Attributes:
        id (int):  Example: 123456789.
        first_name (str):
        last_name (str):
        name (str): First and last name together
        bot (bool):
        premium (bool):
        verified (bool):
        deleted (bool):
        contact (bool): In this account's contacts
        username (str | Unset):
        phone (str | Unset): Digits with the country code, when the user shows it to this account
        status (UserStatus | Unset): The user's online status, as far as their privacy shows it
    """

    id: int
    first_name: str
    last_name: str
    name: str
    bot: bool
    premium: bool
    verified: bool
    deleted: bool
    contact: bool
    username: str | Unset = UNSET
    phone: str | Unset = UNSET
    status: UserStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        name = self.name

        bot = self.bot

        premium = self.premium

        verified = self.verified

        deleted = self.deleted

        contact = self.contact

        username = self.username

        phone = self.phone

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "firstName": first_name,
                "lastName": last_name,
                "name": name,
                "bot": bot,
                "premium": premium,
                "verified": verified,
                "deleted": deleted,
                "contact": contact,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if phone is not UNSET:
            field_dict["phone"] = phone
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_status import UserStatus

        d = dict(src_dict)
        id = d.pop("id")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        name = d.pop("name")

        bot = d.pop("bot")

        premium = d.pop("premium")

        verified = d.pop("verified")

        deleted = d.pop("deleted")

        contact = d.pop("contact")

        username = d.pop("username", UNSET)

        phone = d.pop("phone", UNSET)

        _status = d.pop("status", UNSET)
        status: UserStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UserStatus.from_dict(_status)

        user = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            name=name,
            bot=bot,
            premium=premium,
            verified=verified,
            deleted=deleted,
            contact=contact,
            username=username,
            phone=phone,
            status=status,
        )

        user.additional_properties = d
        return user

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
