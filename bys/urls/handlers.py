from bys.urls import store
from bys.urls import url_code
from bys.routes_helper import get_short_url


def handle_create(url):
    code = store.find_alphanum_code(url)
    if code:
        return get_short_url(code)

    num_code, alphanum_code = url_code.get_url_codes()
    store.save_url(num_code, alphanum_code, url)
    return get_short_url(alphanum_code)
