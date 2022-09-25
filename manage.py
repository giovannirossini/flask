import os
from app.main.base_service import service

env = os.environ.get('FLASK_ENV')
host = os.environ.get('HOST')
port = os.environ.get('PORT')

if env == "development":
  service.run(host=host,port=port,debug=True)
else:
  service.run(host=host,port=port)