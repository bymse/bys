import unittest
from unittest.mock import patch
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

    @patch('bys.urls.store.save_url')
    @patch('bys.urls.url_code.get_url_codes')
    @patch('bys.urls.store.find_alphanum_code', return_value=None)
    def test_should_save_url_if_doesnt_exist(self, _, get_url_codes_patch, store_save_patch, __):
        input_url = 'https://example.com/test/url'
        num_code = 123
        alphanum_code = 'qwe'

        get_url_codes_patch.return_value = (num_code, alphanum_code)
        handlers.handle_create(input_url)

        store_save_patch.assert_called_once_with(num_code, alphanum_code, input_url)
