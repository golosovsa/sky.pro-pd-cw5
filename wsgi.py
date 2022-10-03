import os
from app.server import app

app_home = os.path.dirname(os.path.realpath(__file__))
os.chdir(app_home)
