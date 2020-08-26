from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/metrics")
def index():
    return("numero_progetti {}".format(randint(0, 10)))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
