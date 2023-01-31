import os
from flask import Flask
import flask


app = Flask(__name__, static_url_path="/static", static_folder="web/static", template_folder="web/templates")

app.config.from_object(os.environ.get("APP_SETTINGS", "config.DevelopmentConfig"))
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "secret")

from web.routes import base_routes


@app.before_request
def before_request():
    if app.config["SSL_REDIRECT"] and not flask.request.is_secure:
        url = flask.request.url
        if url.startswith("http://"):
            url = url.replace('http://', '', 1)
        url = "https://" + url
        code = 301
        return flask.redirect(url, code=code)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
