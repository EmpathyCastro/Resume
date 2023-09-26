from web.paradise_temp.db import BaseDocument, DB, DataType, ReferenceType, DictType, ListType
from datetime import datetime
from io import BytesIO
from PIL import Image


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

    @classmethod
    def upload_image(cls, image):
        image_data = BytesIO()
        image.data.save(image_data)
        image_data.seek(0)
        image_data = cls.get_compressed_image(image_data.read(), image.data.filename.split(".")[-1])
        img = ParadiseImage({
            "extension": image.data.filename.split(".")[-1],
            "image": image_data.read()
        })
        img.push()
        return img["_id"]

    @staticmethod
    def get_compressed_image(image_data, extension):
        img = Image.open(BytesIO(image_data))
        x = 300
        y = int(x * img.size[1] / img.size[0])
        img.thumbnail((x, y))
        img_data = BytesIO()
        img.save(img_data, "JPEG" if extension.lower() == "jpg" else extension.upper())
        img_data.seek(0)
        return img_data


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
