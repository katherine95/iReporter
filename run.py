import os
from app import create_app
from instance.config import app_config

config_name = os.getenv('FLASK_ENV') # config_name = "development"
app = create_app(app_config[config_name])

if __name__ == '__main__':
    app.run()