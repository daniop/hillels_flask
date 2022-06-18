from flask import render_template, request, Blueprint
from faker import Faker
import pandas as pd
import requests


bp = Blueprint('parse', __name__)


@bp.route('/requirements/')
def requirements():
    with open('requirements.txt') as req:
        lines = req.readlines()
    return render_template('requirements.html',
                           lines=lines)


@bp.route('/generate-users/')
def generate_users():
    count = request.args.get('count', default=100, type=int)
    fake = Faker()
    return render_template('generate_users.html',
                           fake=fake,
                           count=count)


@bp.route('/mean/')
def mean():
    with open('flaskr/hw.csv') as csvfile:
        hw = pd.read_csv(csvfile)
        average_height = round(hw[' "Height(Inches)"'].mean() * 2.54, 2)
        average_weight = round(hw[' "Weight(Pounds)"'].mean() / 2.205, 2)
    return f'<h1>Средняя высота = {average_height} см., а средний вес = {average_weight} кг.</h1>'


@bp.route('/space/')
def space():
    rec = requests.get("http://api.open-notify.org/astros.json")
    response = rec.json()
    return f"<h1>В настоящий момент в космосе есть {response['number']} космонавтов.<h1>"

