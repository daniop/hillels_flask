from flask import Flask, render_template, request
from faker import Faker
import pandas as pd
import requests


app = Flask(__name__)


@app.route('/requirements/')
def requirements():
    with open('requirements.txt') as req:
        lines = req.readlines()
    return render_template('requirements.html',
                           lines=lines)


@app.route('/generate-users/')
def generate_users():
    count = request.args.get('count', default=100, type=int)
    fake = Faker()
    return render_template('generate_users.html',
                           fake=fake,
                           count=count)


@app.route('/mean/')
def mean():
    with open('hw.csv') as csvfile:
        hw = pd.read_csv(csvfile)
        average_height = round(hw[' "Height(Inches)"'].mean() * 2.54, 2)
        average_weight = round(hw[' "Weight(Pounds)"'].mean() / 2.205, 2)
    return f'<h1>Средняя высота = {average_height} см., а средний вес = {average_weight} кг.</h1>'


@app.route('/space/')
def space():
    rec = requests.get("http://api.open-notify.org/astros.json")
    response = rec.json()
    return f"<h1>В настоящий момент в космосе есть {response['number']} космонавтов.<h1>"


if __name__ == '__main__':
    app.run()
