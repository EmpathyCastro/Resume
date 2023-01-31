from receiver import app
import flask


@app.route("/")
def home():
    return flask.render_template("home.html", no_header=True, no_container=True)
