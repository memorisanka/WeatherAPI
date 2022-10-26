from flask import Blueprint, render_template
import json
from .forms import EntryForm
import urllib.request


index_blueprint = Blueprint("index", __name__)
# data_blueprint = Blueprint("data", __name__)


@index_blueprint.route('/', methods=["POST", "GET"])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        localization = form.localization.data
        localization_format = localization.replace(" ", "_")
        url = f'http://api.weatherapi.com/v1/current.json?key=542f7d3a3b87476f8a7160752222110&q={localization_format}'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return render_template('data.html', data=data)
    return render_template('entry.html', title='Welcome', form=form)


# @data_blueprint.route('/data', methods=["POST", "GET"])
# def data():
#     return render_template('data.html', localization=localization)
