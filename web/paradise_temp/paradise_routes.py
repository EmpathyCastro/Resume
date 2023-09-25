import flask
from io import BytesIO
from web import app
from web.paradise_temp.models import Sale, Product, InventoryItem, InventoryBox, ParadiseImage
from web.paradise_temp.db import get_obj_id
from datetime import datetime
from web.paradise_temp.forms import AddInventoryItemForm, AddInventoryBoxForm


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


@app.route("/paradise/add_inventory_item", methods=["GET", "POST"])
def add_inventory_item():
    form = AddInventoryItemForm()
    if form.validate_on_submit():
        image_id = ParadiseImage.upload_image(form.image)
        InventoryItem({
            "name": form.name.data,
            "amount": form.amount.data,
            "image_id": image_id
        }).push()
        return flask.redirect(flask.url_for("paradise_inventory"))
    return flask.render_template("paradise_temp/add_inventory_item.html",
                                 title="Add Inventory Item", form=form)


@app.route("/paradise/add_inventory_box", methods=["GET", "POST"])
def add_inventory_box():
    form = AddInventoryBoxForm.from_items(list(InventoryItem.find()))
    if form.validate_on_submit():
        image = form.image
        image_id = ParadiseImage.upload_image(image)
        InventoryBox({
            "name": form.name.data,
            "image_id": image_id,
            "items": form.get_items()
        }).push()
        return flask.redirect(flask.url_for("paradise_inventory"))
    return flask.render_template("paradise_temp/add_inventory_box.html",
                                 title="Add Inventory Box", form=form)


@app.route("/paradise/image/<image_id>")
def get_paradise_image(image_id):
    image = ParadiseImage.find({"_id": get_obj_id(image_id)}, one=True)
    image_data = BytesIO(image["image"])
    image_data.seek(0)
    return flask.send_file(image_data, mimetype=f"image/{image['extension']}")


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
