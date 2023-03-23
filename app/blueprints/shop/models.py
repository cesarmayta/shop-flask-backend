from utils.db import db

class Producto(db.Model):
    __tablename__ = "tbl_producto"

    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(200),nullable=False)
    imagen = db.Column(db.String(254),default='https://ingoodcompany.asia/images/products_attr_img/matrix/default.png')
    precio = db.Column(db.Double,default=0)

    def __init__(self,nombre):
        self.nombre = nombre
        
    @staticmethod
    def get_all():
        return Producto.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Producto.query.get(id)
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()