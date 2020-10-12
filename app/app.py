import os

from flask import Flask, render_template, redirect, url_for, make_response
from redminelib import Redmine


redmine_url = os.getenv('REDMINE_URL')
user = os.getenv('REDMINE_USER')
pwd = os.getenv('REDMINE_PASSWORD')

app = Flask(__name__)
redmine = Redmine(redmine_url, username=user, password=pwd)

def query_metrics():
    text = ""
    text += 'rdm_project_all {}'.format(len(redmine.project.all()))
    for project in redmine.project.all():
        text += "\nrdm_project_issues_all{project=" + project.identifier + "} " + str(len(project.issues)) 
    return text

@app.route('/')
def index():
    return redirect(url_for('metrics'))

@app.route("/metrics")
def metrics():
    values = query_metrics()
    resp = make_response(render_template("metrics.html", struct=values)) 
    resp.headers['Content-Type'] = 'text/plain'
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
