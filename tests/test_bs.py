from typing import Any

from bs import RedditFetchService
from messages import RedditThread


class _FakeResponse:
    def __init__(self, payload: dict[str, Any]):
        self._payload = payload
        self.status_checked = False

    def raise_for_status(self) -> None:
        self.status_checked = True

    def json(self) -> dict[str, Any]:
        return self._payload


def test_fetch_reddit_threads_parses_latest_three(monkeypatch):
    payload = {
        "data": {
            "children": [
                {"data": {"title": "First cat thread", "permalink": "/a"}},
                {"data": {"title": "Second dog thread", "permalink": "/b"}},
                {"data": {"title": "Third thread", "permalink": "/c"}},
                {"data": {"title": "Fourth should be ignored", "permalink": "/d"}},
            ]
        }
    }
    response = _FakeResponse(payload)

    def fake_get(*_args, **_kwargs):
        return response

    monkeypatch.setattr("bs.requests.get", fake_get)

    service = RedditFetchService()
    threads = service._fetch_reddit_threads()

    assert response.status_checked is True
    assert len(threads) == 3
    assert [thread["title"] for thread in threads] == [
        "First cat thread",
        "Second dog thread",
        "Third thread",
    ]


def test_on_poll_uses_mocks_when_reddit_fetch_fails(monkeypatch):
    service = RedditFetchService()

    def fake_fetch():
        raise RuntimeError("reddit unavailable")

    sent_messages = []

    def fake_send_request_async(_target, request):
        sent_messages.append(request)

    monkeypatch.setattr(service, "_fetch_reddit_threads", fake_fetch)
    monkeypatch.setattr(service, "send_request_async", fake_send_request_async)

    service.on_poll()

    assert len(sent_messages) == 3
    assert all(isinstance(msg, RedditThread) for msg in sent_messages)
    assert any("cat" in msg.title.lower() for msg in sent_messages)
    assert any("dog" in msg.title.lower() for msg in sent_messages)
