import os
from app.server import create_app
from app.config import ConfigFactory

app_home = os.path.dirname(os.path.realpath(__file__))
os.chdir(app_home)

app = create_app(ConfigFactory.get_config())

if __name__ == '__main__':
    app.run(debug=True)
