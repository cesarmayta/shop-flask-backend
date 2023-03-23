from utils.db import ma
from marshmallow_sqlalchemy import SQLAlchemySchema,auto_field,SQLAlchemyAutoSchema

from .models import Producto

class ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Producto