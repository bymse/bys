import unittest
from unittest.mock import patch, PropertyMock
from bys.urls import handlers

base_url = 'https://base.com'


@patch('bys.config.get_val', return_value=base_url)
class UrlsHandlersTestCase(unittest.TestCase):

    @patch('bys.urls.store.find_alphanum_code')
    def test_handle_create_should_return_existing_url(self, store_patch, _):
        existing_url = 'https://example.com'
        alphanum_code = 'qwe123'
        store_patch.return_value = alphanum_code
        self.assertEqual(handlers.handle_create(existing_url), f'{base_url}/s/{alphanum_code}')
