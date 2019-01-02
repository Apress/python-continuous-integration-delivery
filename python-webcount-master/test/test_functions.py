from unittest.mock import Mock, patch

from webcount import most_common_word_in_web_page

def test_with_patch():
    mock_requests = Mock()
    mock_requests.get.return_value.text = 'aa bbb c'
    with patch('webcount.functions.requests', mock_requests):
        result = most_common_word_in_web_page(
            ['a', 'b', 'c'],
            'https://python.org/',
        )
    assert result == 'b', \
        'most_common_word_in_web_page tested with test double'
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0] \
            == 'https://python.org/', 'called with right URL'

