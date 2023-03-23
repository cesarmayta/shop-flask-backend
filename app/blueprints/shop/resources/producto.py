import os
import werkzeug

from flask_restful import Resource,Api,reqparse
from flask import request
from flask_jwt_extended import jwt_required



from .. import shop

from ..models import Producto
from ..schemas import ProductoSchema



api = Api(shop)

class UploadImage(Resource):
    @jwt_required
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file',type=werkzeug.datastructures.FileStorage,location='files')
        args = parse.parse_args()
        
        image_file = args['file']
        image_file.save(os.path.join(os.getcwd(),'app','static','uploads',image_file.filename))
        
        url_path = request.host_url +  "static/uploads/" + str(image_file.filename)
        
        context = {
            "status":True,
            "content":url_path
        }
        
        return context
    


class ProductoResource(Resource):
    
    #@jwt_required()
    def get(self):

        data = Producto.get_all()

        data_schema = ProductoSchema(many=True)

        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context

    @jwt_required()
    def post(self):
        data = request.get_json()
        nombre = data["nombre"]
        precio = data["precio"]

        objProducto = Producto(nombre)
        objProducto.precio = precio
        objProducto.save()

        data_schema = ProductoSchema()

        context = {
            'status':True,
            'content':data_schema.dump(objProducto)
        }

        return context

    @jwt_required()
    def put(self,id):
        data = request.get_json()
        nombre = data["nombre"]
        precio = data["precio"]
        imagen = data["imagen"]

        objProducto = Producto.get_by_id(id)
        objProducto.nombre = nombre
        objProducto.precio = precio
        objProducto.imagen = imagen
        objProducto.save()

        data_schema = ProductoSchema()

        context = {
            'status':True,
            'content':data_schema.dump(objProducto)
        }

        return context

    @jwt_required()
    def delete(self,id):

        objProducto = Producto.get_by_id(id)
        objProducto.delete()

        data_schema = ProductoSchema()

        context = {
            'status':True,
            'content':data_schema.dump(objProducto)
        }

        return context

api.add_resource(ProductoResource,'/producto')
api.add_resource(ProductoResource,'/producto/<id>',endpoint='producto')
api.add_resource(UploadImage,'/uploadimage')