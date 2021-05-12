import os
import json
from flask import Flask, render_template, make_response, request


app = Flask(__name__)


def to_pretty_json(value):
    return json.dumps(value, sort_keys=True,
                      indent=4, separators=(',', ': '))

app.jinja_env.filters['tojson_pretty'] = to_pretty_json

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        headerz = dict(request.headers)
        with open('headers', 'w') as fp:
         json.dump(headerz, fp)
        body = request.get_json()
        with open('request', 'w') as fp:
            json.dump(body, fp)
        return ('', 204)

    if request.method == 'GET':
        output= ''
        with open('headers', 'r') as fp:
            headerz = json.load(fp)
        for k in headerz:
            output += f'{k} = {headerz[k]}\n'
        with open('request', 'r') as fp:
            body = json.load(fp)
        resp = make_response(render_template("index.html", struct=output, body=body))
        resp.headers['Content-Type'] = 'text/plain'
        return (resp, 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
