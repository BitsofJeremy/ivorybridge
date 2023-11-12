import logging
import os

from ivorybridge import create_app

config_name = os.getenv('FLASK_CONFIG')
application = create_app(config_name)


if __name__ == '__main__':
    application.run()
