from web import app
import flask
from web.routes.dynamicode import get_dynamicode_demo_data


@app.route("/")
def home():
    return flask.redirect(flask.url_for("resume"))


@app.route("/resume")
def resume():
    return flask.render_template("resume.html", no_container=True, portfolio_btn=True)


@app.route("/portfolio")
def portfolio():
    return flask.render_template("portfolio.html", no_container=True, resume_btn=True)


@app.route("/projects/<project>")
def projects(project):
    project_pages = {
        "dynamicode": "project_pages/dynamicode.html",
    }
    if project in project_pages:
        return flask.render_template(project_pages[project], demo=get_dynamicode_demo_data())
    else:
        return flask.abort(404)
