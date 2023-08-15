from web import app
import flask
from web.routes.dynamicode import get_dynamicode_demo_data


@app.errorhandler(404)
def page_not_found(_):
    return flask.render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(_):
    return flask.render_template("500.html"), 500


@app.route("/")
def home():
    # return flask.render_template("home.html", no_container=True)
    return flask.redirect(flask.url_for("portfolio"))


@app.route("/status")
def status():
    return "OK"


@app.route("/linkedin")
@app.route("/LinkedIn")
def linkedin():
    return flask.redirect("https://www.linkedin.com/in/empathy-castro/")


@app.route("/resume")
def resume():
    return flask.render_template("resume.html", no_container=True, splash_text="Resume")


@app.route("/portfolio")
def portfolio():
    return flask.render_template("portfolio.html", no_container=True, splash_text="Portfolio")


@app.route("/projects/<project>")
def projects(project):
    project_pages = {
        "dynamicode": "project_pages/dynamicode.html",
        "get_indigenous": "project_pages/get_indigenous.html",
        "ideal_etl": "project_pages/ideal_etl.html",
        "paradise_box": "project_pages/paradise_box.html",
        "psp_attendance": "project_pages/psp_attendance.html",
        "site_management": "project_pages/site_management.html",
        "cve_dashboard": "project_pages/cve_dashboard.html"
    }
    if project in project_pages:
        return flask.render_template(project_pages[project], demo=get_dynamicode_demo_data(),
                                     images=get_project_images(project))
    else:
        return flask.abort(404)


def get_project_images(project):
    data = {
        "get_indigenous": [
            {"src": flask.url_for("static", filename="img/projects/get_indigenous/img1.png"),
             "alt": "Get Indigenous Home Page"},
            {"src": flask.url_for("static", filename="img/projects/get_indigenous/img2.png"),
             "alt": "Get Indigenous Shopping Cart Page"},
            {"src": flask.url_for("static", filename="img/projects/get_indigenous/img3.png"),
             "alt": "Get Indigenous Checkout Page"},
            {"src": flask.url_for("static", filename="img/projects/get_indigenous/img4.png"),
             "alt": "Get Indigenous Order Payment Page"}
        ],
        "psp_attendance": [
            {"src": flask.url_for("static", filename="img/projects/psp_attendance/img1.png"),
             "alt": "PSP Home Page"},
            {"src": flask.url_for("static", filename="img/projects/psp_attendance/img2.png"),
             "alt": "PSP Admin Home Page"},
            {"src": flask.url_for("static", filename="img/projects/psp_attendance/img3.png"),
             "alt": "PSP Admin Events Page"},
            {"src": flask.url_for("static", filename="img/projects/psp_attendance/img4.png"),
             "alt": "PSP Admin Attendance Reports Page"}
        ],
        "paradise_box": [
            {"src": flask.url_for("static", filename="img/projects/paradise_box/img1.png"),
             "alt": "Paradise Box Home Page 1"},
            {"src": flask.url_for("static", filename="img/projects/paradise_box/img2.png"),
             "alt": "Paradise Box Home Page 2"}
        ],
        "ideal_etl": [
            {"src": flask.url_for("static", filename="img/projects/ideal_etl/img1.png"),
             "alt": "Ideal ETL Dashboard"},
            {"src": flask.url_for("static", filename="img/projects/ideal_etl/img2.png"),
             "alt": "Ideal ETL Settings Page"},
            {"src": flask.url_for("static", filename="img/projects/ideal_etl/img3.png"),
             "alt": "Ideal ETL Advanced Search Page"}
        ],
        "site_management": [
            {"src": flask.url_for("static", filename="img/projects/site_management/img1.png"),
             "alt": "Site Management Projects View"},
            {"src": flask.url_for("static", filename="img/projects/site_management/img2.png"),
             "alt": "Site Management Project 1"},
            {"src": flask.url_for("static", filename="img/projects/site_management/img3.png"),
             "alt": "Site Management Project 2"}
        ],
        "cve_dashboard": [
            {"src": flask.url_for("static", filename="img/projects/cve_dashboard/img1.png"),
             "alt": "CVE Dashboard Sign In/Sign Up Page"},
            {"src": flask.url_for("static", filename="img/projects/cve_dashboard/thumbnail.jpeg"),
             "alt": "CVE Dashboard Vulnerability Types Page"},
            {"src": flask.url_for("static", filename="img/projects/cve_dashboard/img2.jpeg"),
             "alt": "CVE Dashboard Top Vulnerabilities Page"},
            {"src": flask.url_for("static", filename="img/projects/cve_dashboard/img3.jpeg"),
             "alt": "CVE Dashboard Products Page"}
        ]
    }
    return data.get(project)
