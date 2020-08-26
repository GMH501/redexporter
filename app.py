from flask import Flask
from redminelib import Redmine
import os

redmine_url = os.getenv('REDMINE_URL')
redmine_username = os.getenv('REDMINE_USER')
redmine_password = os.getenv('REDMINE_PASSWORD')

app = Flask(__name__)

redmine = Redmine("http://redmine-devops-test.apps.ocp.ocp-lab.serverlr.local/", redmine_username="admin", redmine_password="password")

@app.route("/metrics")
def index():
    return("numero_progetti {}".format(len(redmine.project.all())))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
