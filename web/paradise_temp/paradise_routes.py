import flask
from web import app
from web.paradise_temp.models import Sale, Product
from web.paradise_temp.db import get_obj_id
from datetime import datetime


@app.route("/paradise")
def paradise():
    products = list(Product.find())
    total_earned = sum([product.get_total_earned() for product in products])
    return flask.render_template("paradise_temp/paradise.html", products=products, total_earned=total_earned)


@app.route("/paradise/modify_sale", methods=["POST"])
def modify_sale():
    product_name = flask.request.json["product_name"]
    product_id = flask.request.json["product_id"]
    amount = flask.request.json["amount"]
    date = datetime.now()
    Sale({
        "date": date,
        "product_name": product_name,
        "product_id": get_obj_id(product_id),
        "amount": amount
    }).push()
    product = Product.find({"_id": get_obj_id(product_id)}, one=True)
    product["amount_sold"] += amount
    product.push()
    total_change = product["price"] * amount
    return flask.jsonify({"amount_sold": product["amount_sold"],
                          "pretty_total_earned": product.get_pretty_total_earned(),
                          "total_change": total_change})
