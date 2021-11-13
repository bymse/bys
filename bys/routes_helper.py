from flask import current_app
from urllib.parse import urljoin


def get_short_url(url_code):
    base_url = current_app.config["BaseUrl"]
    return urljoin(base_url, url_code)
