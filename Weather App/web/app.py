from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
import sys
import requests
import json
import datetime

app = Flask(__name__)
# db = create_engine('sqlite:///weather.db?check_same_thread=False')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
db = SQLAlchemy(app)
api_key = '80d2dcec03133dc269c9a17fea6df313'
app.secret_key = 'secret_key'


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)


db.create_all()


@app.route('/')
def index():
    def get_date(timezone):
        tz = datetime.timezone(datetime.timedelta(seconds=int(timezone)))
        return datetime.datetime.now(tz=tz).time().hour
    weather = []
    cities = City.query.all()
    for city in cities:
        city_name = city.name
        data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
        dict_with_weather_info = {
            "name": json.loads(data.content)["name"],
            "state": {k: v for e in json.loads(data.content)["weather"] for (k, v) in e.items()}.get("main"),
            "temp": int(json.loads(data.content)["main"].get("temp") - 273.15),
            "time": get_date(json.loads(data.content)['timezone']),
            "id": f"{city.id}"
        }
        weather.append(dict_with_weather_info)
    return render_template('index.html', weather=weather)


@app.route('/add', methods=['GET', 'POST'])
def add_city():
    city_name = request.form.get('city_name')
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
    if response.status_code == 404:
        flash("The city doesn't exist!")
        return redirect('/')
    cities = City.query.all()
    for city in cities:
        if city.name == city_name:
            flash("The city has already been added to the list!")
            return redirect('/')
    else:
        city = City(name=city_name)
        db.session.add(city)
        db.session.commit()

        return redirect('/')


@app.route('/delete/<city_id>', methods=['GET', 'POST'])
def delete(city_id):
    city = City.query.filter_by(id=city_id).first()
    db.session.delete(city)
    db.session.commit()
    return redirect('/')


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
