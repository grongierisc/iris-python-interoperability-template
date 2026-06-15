import re

from iop import BusinessProcess, target

from messages import ClassifiedThread, RedditThread

CAT_PATTERN = re.compile(r"\bcat\b", flags=re.IGNORECASE)
DOG_PATTERN = re.compile(r"\bdog\b", flags=re.IGNORECASE)


class KeywordRouterProcess(BusinessProcess):
    """Route Reddit titles to cat or dog output operations."""

    CatTarget = target()
    DogTarget = target()

    def on_message(self, request: RedditThread):
        title = request.title.strip()
        if not title:
            return None

        if CAT_PATTERN.search(title):
            self.send_request_async(
                self.CatTarget,
                ClassifiedThread(
                    title=title,
                    destination_file="cat.txt",
                    permalink=request.permalink,
                ),
            )

        if DOG_PATTERN.search(title):
            self.send_request_async(
                self.DogTarget,
                ClassifiedThread(
                    title=title,
                    destination_file="dog.txt",
                    permalink=request.permalink,
                ),
            )

        return None
