import base64
import os
import pprint
import json

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


# TOKEN = os.getenv('GITHUB_TOKEN')
USERNAME = os.getenv('GITHUB_USERNAME')
ENDPOINT = 'https://api.github.com/users/{username}/repos'.format(
    username=USERNAME
)
'/users/{username}/repos'
'/repos/{owner}/{repo}/readme'


def get_readme(repository_name):
    readme_endpoint = (
        'https://api.github.com/repos/{username}/{repo}/readme'.format(
            username=USERNAME,
            repo=repository_name
        )
    )
    headers = {'Accept': 'application/vnd.github+json'}
    # headers = {'Accept': 'application/vnd.github.raw+json'}
    # headers = {'Accept': 'application/vnd.github.html+json'}
    content = requests.get(
        readme_endpoint,
        headers=headers
    ).json()['content']
    return base64.b64decode(content).decode('utf-8')


response = requests.get(ENDPOINT)
print(response)
# print(sorted([name['homepage'] for name in response.json()]))
print(
    [
        {
            'name': name['name'],
            'description': name['description'],
            'url': name['url'],
            'topics': name['topics'],
            'homepage': name['homepage'],
            'readme': get_readme(repository_name=name['name'])
        } for name in response.json() if name['name'] == 'PocketSmartBudgetBot'
    ]
)

# получить json
# сформировать из него объекты для сохранения в бд
# 'name'
# 'description'
# 'url'

# {
#     'name':,
#     'description':,
#     'url':,
#     'topics':,
#     'homepage',
# }
# Импорт полученных данных в БД
# try:
#     conn = psycopg2.connect(dbname=NAME, user=USER, password=PASSWORD, host=HOST)
# except Exception:
#     print('Can`t establish connection to database')
