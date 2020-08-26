import os

from flask import Flask
from redminelib import Redmine


redmine_url = os.getenv('REDMINE_URL')
user = os.getenv('REDMINE_USER')
pwd = os.getenv('REDMINE_PASSWORD')

app = Flask(__name__)

redmine = Redmine(redmine_url, username=username, password=pwd)

@app.route("/metrics")
def index():
    return("numero_progetti {}".format(len(redmine.project.all())))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
