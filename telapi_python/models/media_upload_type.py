from enum import Enum


class MediaUploadType(str, Enum):
    ANIMATION = "animation"
    AUDIO = "audio"
    DOCUMENT = "document"
    PHOTO = "photo"
    VIDEO = "video"
    VOICE = "voice"

    def __str__(self) -> str:
        return str(self.value)
