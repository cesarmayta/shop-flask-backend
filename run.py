from app import create_app
from utils.db import db,migrate

app = create_app() #Esto retorna el objeto app creado en el archivo __init__.py de APP

with app.app_context():
    db.init_app(app)
    migrate.init_app(app,db)