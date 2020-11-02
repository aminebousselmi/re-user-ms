from flask import Flask
from flask_restful import Api

from db import db

from resources.user import UserAdd, UserEdit
from resources.estate import Estate, AddEstate, EditEstate
from resources.room import Room, EditRoom

from flask_swagger_ui import get_swaggerui_blueprint

# config of the microservice and Database information
PORT = 5000
re_user_ms = Flask(__name__)
re_user_ms.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
re_user_ms.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(re_user_ms)


# Create tables inside database before first request
@re_user_ms.before_first_request
def create_tables():
    db.create_all()


# Swagger config
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Real Estate User microservice"
    }
)
re_user_ms.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# Endpoints List

api.add_resource(UserAdd, '/users')  # Add user
api.add_resource(UserEdit, '/users/<int:id_user>')  # Edit user

api.add_resource(AddEstate, '/users/<int:id_user>/estates')  # Add estate
api.add_resource(EditEstate, '/users/<int:id_user>/estates/<int:id_estate>')  # Edit estate of current owner
api.add_resource(Estate, '/estates/<string:city>')  # Get estates by city

api.add_resource(Room, '/users/<int:id_user>/estates/<int:id_estate>/rooms')  # Add room
api.add_resource(EditRoom, '/users/<int:id_user>/estates/<int:id_estate>/rooms/<int:id_room>')  # Edit room

db.init_app(re_user_ms)

if __name__ == "__main__":
    re_user_ms.run(port=PORT, debug=True)
