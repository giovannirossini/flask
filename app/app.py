from flask import Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix
from app.blueprint import blueprint

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.register_blueprint(blueprint)
app.app_context().push()