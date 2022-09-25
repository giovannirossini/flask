from flask import Blueprint
from flask_restx import Api

from app.main.scripts.heroku import api as Heroku

blueprint = Blueprint('api', __name__)
api = Api(blueprint, doc="/",
            title="Swagger using Flask",
            description="https://github.com/giovannirossini/flask",
            version="1.0"
            )

api.add_namespace(Heroku)