from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import url_form
import handlers

bp = Blueprint('urls', __name__)


@bp.route('/', methods=('GET', 'POST'))
def create():
    form = url_form.UrlForm()
    if form.validate_on_submit():
        short_url = handlers.handle_create(form.url)
