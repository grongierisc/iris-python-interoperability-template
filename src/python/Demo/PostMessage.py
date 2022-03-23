from Post import PostClass

import grongier.pex
from dataclasses import dataclass

@dataclass
class PostMessage(grongier.pex.Message):

    Post:PostClass = None
    ToEmailAddress:str = None
    Found:str = None
    