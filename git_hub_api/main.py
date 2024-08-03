import os

from dotenv import load_dotenv
import requests
import psycopg2

load_dotenv()

NAME = os.getenv('POSTGRES_DB')
USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')

# импорт данных из GitHub api

ENDPOINT = 'https://api.github.com/users/USERNAME/repos'
TOKEN = os.getenv('GITHUB_TOKEN')
USERNAME = os.getenv('GITHUB_USERNAME')
# auth = auth: 'YOUR-TOKEN'
query_params = {'X-GitHub-Api-Version': '2022-11-28'}

response = requests.get()
# Импорт полученных данных в БД
try:
    conn = psycopg2.connect(dbname=NAME, user=USER, password=PASSWORD, host=HOST)
except Exception:
    print('Can`t establish connection to database')
