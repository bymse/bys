import bys.config


def get_short_url(url_code):
    base_url = bys.config.get_val("BASE_URL")
    return base_url.strip("/") + f'/{url_code}'
