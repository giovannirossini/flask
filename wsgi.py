import os
from app.app import app

env = os.environ.get('FLASK_ENV')
host = os.environ.get('HOST')
port = os.environ.get('PORT')

if __name__ == "__main__":
    if env == "development":
        app.run(host=host,port=port,debug=True)
    else:
        app.run(host=host,port=port)