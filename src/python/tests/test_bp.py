import pytest
from unittest.mock import Mock

from bp import FilterPostRoutingRule
from message import PostMessage
from obj import PostClass

@pytest.fixture
def mock_send_request_sync():
    return Mock()

def test_on_python_message(mock_send_request_sync):
    rule = FilterPostRoutingRule()
    # fix the target to avoid the error
    target = 'Python.FileOperation'
    rule.target = target
    rule.send_request_sync = mock_send_request_sync

    post = PostClass(title='Test Post', selftext='This is a test post about dogs.', author='Test Author', url='http://test.com', created_utc=1234567890, original_json='{}')
    message = PostMessage(post=post)

    rule.on_python_message(message)

    # assert that the send_request_sync has been called once
    excepted = message
    excepted.to_email_address = 'dog@company.com'
    excepted.found = 'Dog'

    mock_send_request_sync.assert_called_once_with(target, excepted)