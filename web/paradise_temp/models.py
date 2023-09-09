from web.paradise_temp.db import BaseDocument, DB, DataType, ReferenceType
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
