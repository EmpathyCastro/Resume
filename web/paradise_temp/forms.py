from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, HiddenField, FileField,\
    IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange


class AddInventoryItemForm(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired()])
    image = FileField("Product Image", validators=[DataRequired()])
    amount = IntegerField("Starting Amount", validators=[InputRequired(), NumberRange(min=0)], default=0)
    submit = SubmitField("Add Product")


class EditInventoryItemForm(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired()])
    image = FileField("Change Product Image (optional)")
    submit = SubmitField("Edit Product")

    @classmethod
    def from_item(cls, item):
        form = cls(data={
            "name": item["name"]
        })
        return form


class InventoryBoxItemForm(FlaskForm):
    item_name = HiddenField()
    item_id = HiddenField()
    item_image_id = HiddenField()
    item_amount = IntegerField("", validators=[InputRequired(), NumberRange(min=0)], default=0)

    def set_item(self):
        self.item_amount.label.text = self.item_name.data


class AddInventoryBoxForm(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired()])
    image = FileField("Product Image", validators=[DataRequired()])
    items = FieldList(FormField(InventoryBoxItemForm))
    submit = SubmitField("Add Product")

    @classmethod
    def from_items(cls, available_items):
        available_items = list(available_items)
        field_data = []
        for item in available_items:
            field_data.append({"item_name": item["name"], "item_id": str(item["_id"]),
                               "item_image_id": str(item["image_id"])})
        form = cls(data={"items": field_data})
        for item_field in form.items:
            item_field.set_item()
        return form

    def get_items(self):
        items = []
        for item in self.items:
            if item.item_amount.data <= 0:
                continue
            items.append({"item_id": item.item_id.data, "amount": item.item_amount.data})
        return items


class EditInventoryBoxForm(AddInventoryBoxForm):
    image = FileField("Change Product Image (optional)")
    submit = SubmitField("Edit Product")

    def update_data(self, box):
        self.name.data = box["name"]
        for item_field in self.items:
            for box_item in box["items"]:
                if box_item["item_id"] == item_field.item_id.data:
                    item_field.item_amount.data = box_item["amount"]