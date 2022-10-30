from flask import Blueprint, render_template
from app.forms import EntryForm
from app.classes import FileMixin, ConnectionMixin, WeatherForecast


index_blueprint = Blueprint("index", __name__)
data_blueprint = Blueprint("data", __name__)


@index_blueprint.route('/', methods=["POST", "GET"])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        localization = form.localization.data
        fm = FileMixin(localization)
        forecast = WeatherForecast(localization)
        file_exist = fm.check_file()
        if file_exist:
            weather_data = fm.read_json()
            check_date = forecast.check_date(weather_data)
            if check_date:
                forecast.write_forecast()
                return render_template('data.html', data="Date OK")
            else:
                conn = ConnectionMixin(localization)
                connection = conn.connect_to_api()
                if connection:
                    data = conn.get_data_to_dict()
                    fm = FileMixin(localization)
                    fm.write_json(data)
                    forecast.write_forecast()
                    return render_template('data.html', data="Date not OK")
        else:
            conn = ConnectionMixin(localization)
            connection = conn.connect_to_api()
            if connection:
                data = conn.get_data_to_dict()
                fm = FileMixin(localization)
                fm.write_json(data)
                forecast.write_forecast()
                return render_template('data.html', data="File does not exist.")

    return render_template('entry.html', form=form)


@data_blueprint.route('/data', methods=["POST", "GET"])
def show_data():
    return render_template('data.html')
