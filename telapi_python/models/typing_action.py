from enum import Enum


class TypingAction(str, Enum):
    CANCEL = "cancel"
    RECORD_AUDIO = "record_audio"
    RECORD_VIDEO = "record_video"
    TYPING = "typing"
    UPLOAD_DOCUMENT = "upload_document"
    UPLOAD_PHOTO = "upload_photo"

    def __str__(self) -> str:
        return str(self.value)
