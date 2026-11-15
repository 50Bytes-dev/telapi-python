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
            USER_RESTRICTED, or USER_BANNED_IN_CHANNEL in 3 different chats
            within 24 hours), `flood` (a long FLOOD_WAIT, or the third on sends
            within 10 minutes), `frozen` (FROZEN_*: only Telegram's appeal lifts
            it); new reasons may come. Lifted only by `POST /session/resume`.
        step (str | Unset): `wrong_login_step`: the step the login is at Example: password.
        attempts_left (int | Unset): `invalid_code`, `invalid_password`: tries left before the login fails Example: 4.
        rejected_attachments (list[int] | Unset): `attachment_rejected`: the indexes of the unusable attachments
            Example: [1].
        required_stars (int | Unset): `payment_required`: the Telegram Stars Telegram asked for
            (`ALLOW_PAYMENT_REQUIRED_<n>`), unchanged. Telegram's docs call it the price of one message; for a call of
            several messages it may be the call's total, so read it with `messageCount`. Absent when Telegram named no
            number. Example: 25.
        message_count (int | Unset): `payment_required` on a send: how many messages the refused call carried Example:
            1.
        migrated_to_chat_id (int | Unset): `chat_migrated`: the chat id of the supergroup the basic group became; absent
            when Telegram did not name it. This account may not be a member there. Example: -1001234567890.
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
    required_stars: int | Unset = UNSET
    message_count: int | Unset = UNSET
    migrated_to_chat_id: int | Unset = UNSET
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

        required_stars = self.required_stars

        message_count = self.message_count

        migrated_to_chat_id = self.migrated_to_chat_id

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
        if required_stars is not UNSET:
            field_dict["requiredStars"] = required_stars
        if message_count is not UNSET:
            field_dict["messageCount"] = message_count
        if migrated_to_chat_id is not UNSET:
            field_dict["migratedToChatId"] = migrated_to_chat_id
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

        required_stars = d.pop("requiredStars", UNSET)

        message_count = d.pop("messageCount", UNSET)

        migrated_to_chat_id = d.pop("migratedToChatId", UNSET)

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
            required_stars=required_stars,
            message_count=message_count,
            migrated_to_chat_id=migrated_to_chat_id,
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
