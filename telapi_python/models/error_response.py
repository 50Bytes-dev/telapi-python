from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pause import Pause


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """The body of every error. Branch on `code`; the details below come with the codes that name them.

    Attributes:
        success (bool):
        code (str): The machine code (see "Codes" above). New codes may come; treat an unknown one by the HTTP status.
            Example: flood_wait.
        error (str): A fixed English text per case; never Telegram's text. Do not branch on it. Example: Telegram asked
            to wait.
        retry_after_ms (int | Unset): `flood_wait`, `slowmode_wait`, and `paused` when Telegram named a wait: in how
            many milliseconds the call may come again (rounded up) Example: 37000.
        upstream_code (str | Unset): Telegram's RPC error type without its number (`FLOOD_WAIT_37` is `FLOOD_WAIT`)
            Example: FLOOD_WAIT.
        pause (Pause | Unset): The pause of the Telegram user. `reason`: `spam` (PEER_FLOOD,
            USER_RESTRICTED), `flood` (a long FLOOD_WAIT, or the third on sends
            within 10 minutes), `frozen` (FROZEN_*: only Telegram's appeal lifts
            it); new reasons may come. Lifted only by `POST /session/resume`.
        step (str | Unset): `wrong_login_step`: the step the login is at Example: password.
        attempts_left (int | Unset): `invalid_code`, `invalid_password`: tries left before the login fails Example: 4.
        rejected_attachments (list[int] | Unset): `attachment_rejected`: the indexes of the unusable attachments
            Example: [1].
        saved_messages_left (list[int] | Unset): `POST /messages/relay`: the ids of the copy left in Saved Messages when
            deleting it failed
    """

    success: bool
    code: str
    error: str
    retry_after_ms: int | Unset = UNSET
    upstream_code: str | Unset = UNSET
    pause: Pause | Unset = UNSET
    step: str | Unset = UNSET
    attempts_left: int | Unset = UNSET
    rejected_attachments: list[int] | Unset = UNSET
    saved_messages_left: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        code = self.code

        error = self.error

        retry_after_ms = self.retry_after_ms

        upstream_code = self.upstream_code

        pause: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pause, Unset):
            pause = self.pause.to_dict()

        step = self.step

        attempts_left = self.attempts_left

        rejected_attachments: list[int] | Unset = UNSET
        if not isinstance(self.rejected_attachments, Unset):
            rejected_attachments = self.rejected_attachments

        saved_messages_left: list[int] | Unset = UNSET
        if not isinstance(self.saved_messages_left, Unset):
            saved_messages_left = self.saved_messages_left

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "code": code,
                "error": error,
            }
        )
        if retry_after_ms is not UNSET:
            field_dict["retryAfterMs"] = retry_after_ms
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code
        if pause is not UNSET:
            field_dict["pause"] = pause
        if step is not UNSET:
            field_dict["step"] = step
        if attempts_left is not UNSET:
            field_dict["attemptsLeft"] = attempts_left
        if rejected_attachments is not UNSET:
            field_dict["rejectedAttachments"] = rejected_attachments
        if saved_messages_left is not UNSET:
            field_dict["savedMessagesLeft"] = saved_messages_left

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pause import Pause

        d = dict(src_dict)
        success = d.pop("success")

        code = d.pop("code")

        error = d.pop("error")

        retry_after_ms = d.pop("retryAfterMs", UNSET)

        upstream_code = d.pop("upstreamCode", UNSET)

        _pause = d.pop("pause", UNSET)
        pause: Pause | Unset
        if isinstance(_pause, Unset):
            pause = UNSET
        else:
            pause = Pause.from_dict(_pause)

        step = d.pop("step", UNSET)

        attempts_left = d.pop("attemptsLeft", UNSET)

        rejected_attachments = cast(list[int], d.pop("rejectedAttachments", UNSET))

        saved_messages_left = cast(list[int], d.pop("savedMessagesLeft", UNSET))

        error_response = cls(
            success=success,
            code=code,
            error=error,
            retry_after_ms=retry_after_ms,
            upstream_code=upstream_code,
            pause=pause,
            step=step,
            attempts_left=attempts_left,
            rejected_attachments=rejected_attachments,
            saved_messages_left=saved_messages_left,
        )

        error_response.additional_properties = d
        return error_response

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
