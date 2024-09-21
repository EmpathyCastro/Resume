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
# app.config["MONGO_DATABASE_URI"] = ENV.get("mongo_database_uri")
# app.config["MONGO_DEV_DB_URI"] = ENV.get("mongo_dev_db_uri")
# app.config["MONGO_USE_DEV_DB"] = ENV.get("mongo_use_dev_db")

from web.routes import base_routes


def start():
    app.run(debug=app.config["DEBUG"])


if __name__ == "__main__":
    start()

