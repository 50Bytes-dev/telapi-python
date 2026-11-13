from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="CreateAccountResponse")


@_attrs_define
class CreateAccountResponse:
    """
    Attributes:
        success (bool):
        account (Account): An account of the gateway as the admin sees it; never its token or webhook secret.
        token (str): The account token, shown only here
        webhook_secret (str): The secret that signs the webhook, shown only here
    """

    success: bool
    account: Account
    token: str = _attrs_field(repr=False)
    webhook_secret: str = _attrs_field(repr=False)
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        account = self.account.to_dict()

        token = self.token

        webhook_secret = self.webhook_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "account": account,
                "token": token,
                "webhookSecret": webhook_secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account

        d = dict(src_dict)
        success = d.pop("success")

        account = Account.from_dict(d.pop("account"))

        token = d.pop("token")

        webhook_secret = d.pop("webhookSecret")

        create_account_response = cls(
            success=success,
            account=account,
            token=token,
            webhook_secret=webhook_secret,
        )

        create_account_response.additional_properties = d
        return create_account_response

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
