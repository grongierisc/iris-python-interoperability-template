from bp import KeywordRouterProcess
from messages import RedditThread


def test_keyword_router_sends_cat_and_dog_messages(monkeypatch):
    router = KeywordRouterProcess()
    dispatched = []

    def fake_send_request_async(_target, request):
        dispatched.append(request)

    monkeypatch.setattr(router, "send_request_async", fake_send_request_async)

    router.on_message(RedditThread(title="My cat and dog are friends", permalink="/x"))

    assert len(dispatched) == 2
    assert sorted(msg.destination_file for msg in dispatched) == ["cat.txt", "dog.txt"]


def test_keyword_router_ignores_non_matching_title(monkeypatch):
    router = KeywordRouterProcess()
    dispatched = []

    def fake_send_request_async(_target, request):
        dispatched.append(request)

    monkeypatch.setattr(router, "send_request_async", fake_send_request_async)

    router.on_message(RedditThread(title="No animal keyword here", permalink="/none"))

    assert dispatched == []
