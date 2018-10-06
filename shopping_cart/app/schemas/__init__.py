from flask_marshmallow import Marshmallow

from app.models.shopper_model import Shoppers
from app.models.product_model import Products
from app.models.order_model import Orders
from app.models.order_item_model import OrderItems

# Insantiate an object from the Marshmallow
# serialization/ deserialization library
marshmallow = Marshmallow()


class ShopperSchema(marshmallow.ModelSchema):
    class Meta:
        # Fields to show
        fields = ('uid', 'username', 'email')

        model = Shoppers
        ordered = True


class ProductSchema(marshmallow.ModelSchema):
    class Meta:
        # Fields to show
        fields = (
            'code',
            'product_name',
            'description',
            'unit_price',
            'unitsInStock',
        )

        model = Products
        ordered = True


class OrderSchema(marshmallow.ModelSchema):
    class Meta:
        # Fields to show
        fields = (
            'oid',
            'cid',
            'order_date',
        )

        model = Orders
        ordered = True


class OrderItemsSchema(marshmallow.ModelSchema):
    class Meta:
        # Fields to show
        fields = (
            'oid',
            'cid',
            'pid',
            'qty',
        )

        model = OrderItems
        ordered = True
