import os
import json
from flask import Flask

# System Files
VARIABLES_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, "flask_env.json")

with open(VARIABLES_FILE) as var_file:
    ENV = json.load(var_file)
app = Flask(__name__)
app.config["SECRET_KEY"] = ENV["secret_key"]
app.config["DEBUG"] = ENV.get("debug", False)

from web.routes import base_routes


def start():
    app.run(debug=app.config["DEBUG"])


if __name__ == "__main__":
    start()

