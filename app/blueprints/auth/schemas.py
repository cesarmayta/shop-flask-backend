from utils.db import ma
from marshmallow import fields

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id','username')