import os
import argparse
import datetime
import pandas as pn
import collections


from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


parser = argparse.ArgumentParser(description='Укажите путь к файлу')
parser.add_argument('-fp', help='Путь к файлу')
args = parser.parse_args()


now_date = datetime.datetime.now().year
release_date = 1920
age = now_date - release_date


all_drinks = collections.defaultdict(list)
excel_file_drinks = pn.read_excel(args.fp, usecols=['Категория',	'Название',	'Сорт',	'Цена',	'Картинка', 'Акция']).fillna(0).to_dict(orient='records')

for wine in excel_file_drinks:
	all_drinks[wine['Категория']].append(wine)

env = Environment(
	loader = FileSystemLoader('.'),
	autoescape = select_autoescape(['html', 'xml'])
	)

template = env.get_template('template.html')
rendered_page = template.render(
	age = age,
	all_drinks = all_drinks,
	)

with open('index.html', 'w', encoding="utf8") as file:
	file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
