from web.paradise_temp.db import BaseDocument, DB, DataType, ReferenceType, DictType, ListType
from datetime import datetime


class Sale(BaseDocument):
    collection = DB.sales
    fields = {
        "date": DataType(datetime, nullable=False),
        "product_name": DataType(str, nullable=False),
        "product_id": ReferenceType(nullable=False),
        "amount": DataType(int, nullable=False)
    }


class Product(BaseDocument):
    collection = DB.products
    fields = {
        "product_name": DataType(str, nullable=False),
        "price": DataType(float, nullable=False),
        "amount_sold": DataType(int, nullable=False, default=0)
    }

    def get_total_earned(self):
        return self["price"] * self["amount_sold"]

    def get_pretty_total_earned(self):
        return f"${self.get_total_earned():.2f}"

    def get_pretty_price(self):
        return f"${self['price']:.2f}"


class ParadiseImage(BaseDocument):
    collection = DB.inventory_images
    fields = {
        "extension": DataType(str, nullable=False),
        "image": DataType(bytes, nullable=False)
    }


class InventoryItem(BaseDocument):
    collection = DB.inventory_items
    fields = {
        "name": DataType(str, nullable=False),
        "amount": DataType(int, nullable=False),
        "image_id": ReferenceType(nullable=True)
    }


class InventoryBox(BaseDocument):
    collection = DB.inventory_boxes
    fields = {
        "name": DataType(str, nullable=False),
        "items": ListType(DictType({
            "item_id": ReferenceType(nullable=False),
            "amount": DataType(int, nullable=False)
        }), nullable=False),
        "image_id": ReferenceType(nullable=True)
    }

    def get_item_ids(self):
        return [item["item_id"] for item in self["items"]]

    def get_amount(self, items):
        item_ids = self.get_item_ids()
        if items:
            items = [item for item in items if item["_id"] in item_ids]
        else:
            items = list(InventoryItem.find({"_id": {"$in": self["items"]}}))

        max_amount = -1
        for item in items:
            item_box_amount = self.get_item_box_amount(item, item_ids)
            if max_amount == -1 or item_box_amount < max_amount:
                max_amount = item_box_amount

        return max(max_amount, 0)

    def get_item_box_amount(self, item, item_ids):
        item_index = item_ids.index(item["_id"])
        return item["amount"] // self["items"][item_index]["amount"]
