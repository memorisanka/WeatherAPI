from flask import Blueprint, render_template, redirect
from .forms import EntryForm


index_blueprint = Blueprint("index", __name__)
# data_blueprint = Blueprint("data", __name__)


@index_blueprint.route('/', methods=["POST", "GET"])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        localization = form.localization.data
        return render_template('data.html', localization=localization)
    return render_template('entry.html', title='Welcome', form=form)


# @data_blueprint.route('/data', methods=["POST", "GET"])
# def data():
#     return render_template('data.html', localization=localization)
