from flask import Blueprint, render_template
from app.forms import EntryForm
from app.classes import FileMixin, ConnectionMixin, WeatherForecast


index_blueprint = Blueprint("index", __name__)


@index_blueprint.route("/", methods=["POST", "GET"])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        localization: str = form.localization.data
        fm = FileMixin(localization)
        forecast = WeatherForecast(localization)
        file_exist: bool = fm.check_file()
        if file_exist:
            weather_data = fm.read_json()
            check_date: bool = forecast.check_date(weather_data)
            if check_date:
                forecast.write_forecast()
                show_data: dict = forecast.show()
                return render_template("data.html", data=show_data)
            else:
                conn = ConnectionMixin(localization)
                connection: bool = conn.connect_to_api()
                if connection:
                    data: dict = conn.get_data_to_dict()
                    fm = FileMixin(localization)
                    fm.write_json(data)
                    forecast.write_forecast()
                    show_data: list = forecast.show()
                    return render_template("data.html", data=show_data)
        else:
            conn = ConnectionMixin(localization)
            connection = conn.connect_to_api()
            if connection:
                data: dict = conn.get_data_to_dict()
                fm = FileMixin(localization)
                fm.write_json(data)
                forecast.write_forecast()
                show_data: list = forecast.show()
                return render_template("data.html", data=show_data)

    return render_template("entry.html", form=form)
