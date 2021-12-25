import bys.config


def get_short_url(url_code):
    base_url = bys.config.get_val("BaseUrl")
    return base_url.strip("/") + f'/s/{url_code}'
