import logging
from typing import Any

import requests
from iop import PollingBusinessService, target

from messages import RedditThread


class RedditFetchService(PollingBusinessService):
    """Polling service fetching the latest Reddit threads."""

    Router = target()

    REDDIT_URL = "https://www.reddit.com/r/all/new.json?limit=3"
    USER_AGENT = "iris-python-interoperability-template/1.0"

    def _fetch_reddit_threads(self) -> list[dict[str, str]]:
        headers = {"User-Agent": self.USER_AGENT}
        response = requests.get(self.REDDIT_URL, headers=headers, timeout=10)
        response.raise_for_status()

        payload: dict[str, Any] = response.json()
        children = payload.get("data", {}).get("children", [])
        threads: list[dict[str, str]] = []
        for child in children[:3]:
            data = child.get("data", {})
            title = str(data.get("title", "")).strip()
            permalink = str(data.get("permalink", "")).strip()
            if title:
                threads.append({"title": title, "permalink": permalink})
        return threads

    def _mock_threads(self) -> list[dict[str, str]]:
        return [
            {
                "title": "Funny cat jumps over a box",
                "permalink": "/r/mock/comments/1/cat-story",
            },
            {
                "title": "Dog enjoys a walk in the park",
                "permalink": "/r/mock/comments/2/dog-story",
            },
            {
                "title": "General discussion thread",
                "permalink": "/r/mock/comments/3/general",
            },
        ]

    def on_poll(self):
        try:
            threads = self._fetch_reddit_threads()
        except Exception as exc:
            logging.warning("Reddit fetch failed, using mocks: %s", exc)
            threads = self._mock_threads()

        for thread in threads:
            self.send_request_async(
                self.Router,
                RedditThread(
                    title=thread["title"],
                    permalink=thread.get("permalink", ""),
                ),
            )

        return None
