from flask_restful import Resource,Api
from flask import request
from .. import auth

from flask_jwt_extended import create_access_token,jwt_required

from ..models import Usuario
from ..schemas import UsuarioSchema

from werkzeug.security import generate_password_hash,check_password_hash

api = Api(auth)

class UsuarioResource(Resource):
    
    @jwt_required()
    def get(self):
        
        data = Usuario.get_all()
        
        data_schema = UsuarioSchema(many=True)
        
        context = {
            'status':True,
            'content': data_schema.dump(data)
        }
        
        return context
    
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        
        password_hash = generate_password_hash(password)
        
        objUsuario = Usuario(username,password_hash)
        objUsuario.save()
        
        data_schema = UsuarioSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(objUsuario)
        }
        
        return context
    
class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        
        try:
            objUsuario = Usuario.query.filter_by(username=username).first()
            print(objUsuario)
            if objUsuario is not None:
                if check_password_hash(objUsuario.password,password):
                    payload = {
                        'id': objUsuario.id,
                        'username':objUsuario.username
                    }
                    status = True
                    access_token = create_access_token(payload)
                else:
                    status = False
                    access_token = "credenciales no validas"
            else:
                status = False
                access_token = "usuario no existe"
            
            context = {
                'status':status,
                'content':access_token
            }
        except Exception as err:
            context = {
                'status':false,
                'content':str(err)
            }
            
        return context
        
            
        
        
api.add_resource(UsuarioResource,'/usuario')
api.add_resource(LoginResource,'/login')
