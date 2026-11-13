from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthResponse")


@_attrs_define
class HealthResponse:
    """
    Attributes:
        success (bool): false when the database does not answer Example: True.
        status (str): `ok`, or `degraded` when the database does not answer Example: ok.
        version (str):  Example: 1.1.0.
        uptime_seconds (int):  Example: 12345.
        db (bool): Whether the database answers a ping Example: True.
        accounts (int): Accounts of the gateway Example: 4.
        connected (int): Accounts with a connected Telegram client Example: 3.
        goroutines (int):  Example: 40.
        mem_alloc_mb (int):  Example: 24.
        code (str | Unset): 503 only: `internal_error` Example: internal_error.
        error (str | Unset): 503 only, a fixed English text Example: the database is unavailable.
    """

    success: bool
    status: str
    version: str
    uptime_seconds: int
    db: bool
    accounts: int
    connected: int
    goroutines: int
    mem_alloc_mb: int
    code: str | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        version = self.version

        uptime_seconds = self.uptime_seconds

        db = self.db

        accounts = self.accounts

        connected = self.connected

        goroutines = self.goroutines

        mem_alloc_mb = self.mem_alloc_mb

        code = self.code

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "status": status,
                "version": version,
                "uptimeSeconds": uptime_seconds,
                "db": db,
                "accounts": accounts,
                "connected": connected,
                "goroutines": goroutines,
                "memAllocMb": mem_alloc_mb,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        status = d.pop("status")

        version = d.pop("version")

        uptime_seconds = d.pop("uptimeSeconds")

        db = d.pop("db")

        accounts = d.pop("accounts")

        connected = d.pop("connected")

        goroutines = d.pop("goroutines")

        mem_alloc_mb = d.pop("memAllocMb")

        code = d.pop("code", UNSET)

        error = d.pop("error", UNSET)

        health_response = cls(
            success=success,
            status=status,
            version=version,
            uptime_seconds=uptime_seconds,
            db=db,
            accounts=accounts,
            connected=connected,
            goroutines=goroutines,
            mem_alloc_mb=mem_alloc_mb,
            code=code,
            error=error,
        )

        health_response.additional_properties = d
        return health_response

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
