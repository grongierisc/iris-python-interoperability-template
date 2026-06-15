from dataclasses import dataclass

from iop import Message


@dataclass
class RedditThread(Message):
    """Message carrying a Reddit thread title."""

    title: str
    permalink: str = ""


@dataclass
class ClassifiedThread(Message):
    """Message with file destination decided by routing logic."""

    title: str
    destination_file: str
    permalink: str = ""
