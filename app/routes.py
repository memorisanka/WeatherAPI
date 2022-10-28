from flask import Blueprint, render_template
from app.forms import EntryForm
from app.classes import FileMixin, ConnectionMixin, WeatherForecast


index_blueprint = Blueprint("index", __name__)
# data_blueprint = Blueprint("data", __name__)


@index_blueprint.route('/', methods=["POST", "GET"])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        localization = form.localization.data
        conn = ConnectionMixin(localization)
        connection = conn.connect_to_api()
        if connection:
            data = conn.get_data_to_dict()
            fm = FileMixin(localization)
            fm.write_json(data)
            return render_template('data.html', data=data)
    return render_template('entry.html', title='WeatherAPI', form=form)


# @data_blueprint.route('/data', methods=["POST", "GET"])
# def data():
#     return render_template('data.html', localization=localization)
