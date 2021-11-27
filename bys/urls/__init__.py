from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from bys.urls import url_form
from bys.urls import handlers

bp = Blueprint('urls', __name__)


@bp.route('/', methods=('GET', 'POST'))
def create():
    form = url_form.UrlForm()
    if form.validate_on_submit():
        short_url = handlers.handle_create(form.url)
