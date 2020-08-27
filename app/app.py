import os

from flask import Flask, render_template, redirect, url_for
from redminelib import Redmine


redmine_url = os.getenv('REDMINE_URL')
user = os.getenv('REDMINE_USER')
pwd = os.getenv('REDMINE_PASSWORD')

app = Flask(__name__)
redmine = Redmine(redmine_url, username=user, password=pwd)

def query_metrics():
    values = {}
    values['rdm_project_all'] = len(redmine.project.all())
    for project in redmine.project.all():
        string = 'rdm_project_{}_issues_all'.format(project.identifier)
        values[string] = len(project.issues)
    return values

@app.route('/')
def index():
    return redirect(url_for('metrics'))

@app.route("/metrics")
def metrics():
    values = query_metrics()
    return render_template("metrics.html", struct=values)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
