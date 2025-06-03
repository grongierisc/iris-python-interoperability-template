from iop import Message
from typing import Optional
from dataclasses import dataclass
from obj import PostClass

@dataclass
class PostMessage(Message):

    post:Optional[PostClass] = None
    to_email_address:Optional[str] = None
    found:Optional[str] = None
