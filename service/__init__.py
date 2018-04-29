from flask import Flask
from flasgger import Swagger


app = Flask(__name__)

swag = Swagger(app)

from service.todoRest import blueprint
app.register_blueprint(blueprint)
