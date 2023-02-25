from web import app
import flask


@app.route("/")
def home():
    return flask.redirect(flask.url_for("resume"))


@app.route("/resume")
def resume():
    return flask.render_template("resume.html", no_container=True, portfolio_btn=True)


@app.route("/portfolio")
def portfolio():
    return flask.render_template("portfolio.html", no_container=True, resume_btn=True)
