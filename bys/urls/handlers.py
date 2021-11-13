import store
import url_code
from bys.routes_helper import get_short_url


def handle_create(url):
    short_url = store.find_short_url(url)
    if short_url:
        return short_url

    unique_code = url_code.get_unique_url_code(url)
    return get_short_url(unique_code)
