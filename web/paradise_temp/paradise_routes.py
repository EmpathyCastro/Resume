import flask
from web import app
from web.paradise_temp.models import Sale, Product, InventoryItem, InventoryBox
from web.paradise_temp.db import get_obj_id
from datetime import datetime


@app.route("/paradise")
def paradise_inventory():
    inventory_boxes = list(InventoryBox.find())
    inventory_items = list(InventoryItem.find())
    return flask.render_template("paradise_temp/inventory.html", inventory_boxes=inventory_boxes,
                                 inventory_items=inventory_items)


@app.route("/paradise/modify_inventory", methods=["POST"])
def modify_inventory():
    item_id = flask.request.json["item_id"]
    amount_change = flask.request.json["amount_change"]
    item = InventoryItem.find({"_id": get_obj_id(item_id)}, one=True)
    item["amount"] += amount_change
    item.push()
    return flask.jsonify({"amount": item["amount"]})


@app.route("/paradise_pos")
def paradise_pos():
    products = list(Product.find())
    total_earned = sum([product.get_total_earned() for product in products])
    return flask.render_template("paradise_temp/paradise_pos.html", products=products, total_earned=total_earned)


@app.route("/paradise_pos/modify_sale", methods=["POST"])
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
