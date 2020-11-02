from flask_restful import Resource, reqparse
from sqlalchemy.orm.exc import NoResultFound

from models.estate import EstateModel
from models.user import UserModel


# check if the type is string and is not empty
#  We can make a utility class to ensure better reuse
def valid_string(s):
    if not s or not isinstance(s, str):
        raise ValueError("Must be a valid string")
    return s


# create generic request parser for estate in order to handle requirement for update and create
def create_request_parser(required):
    parser = reqparse.RequestParser()

    # Handle constraints of the input
    parser.add_argument('name',
                        type=valid_string,
                        required=required,
                        help="Every estate needs a valid name")

    parser.add_argument('description',
                        type=valid_string,
                        required=required,
                        help="Every estate needs a valid description")

    parser.add_argument('es_type',
                        type=valid_string,
                        required=required,
                        help="Every estate needs a valid type")

    parser.add_argument('city',
                        type=valid_string,
                        required=required,
                        help="Every estate needs a valid city")

    parser.add_argument('id_user',
                        type=int,
                        required=required,
                        help="Every estate needs a user id")
    return parser


class Estate(Resource):
    # Get estate by city using HTTP GET request
    def get(self, city):
        try:
            estates = EstateModel.find_by_city(city)
            return {'estates': [estate.json() for estate in estates]}, 200
        except NoResultFound:
            return {'message': 'Estates not found'}, 404
        except:
            return {'message': 'An error occurred while getting estates'}, 500


class AddEstate(Resource):

    # create request parser with required id_user
    parser_add = create_request_parser(True)

    # Add estate by user using HTTP POST request
    def post(self, id_user):
        data = AddEstate.parser_add.parse_args()
        try:
            estate = EstateModel(**data)

            # check if the owner and current user who add the estate exists, else raise exception
            if UserModel.find_by_id(data.id_user) and UserModel.find_by_id(id_user):
                estate.save_to_db()

            return estate.json(), 201
        except NoResultFound:
            return {'message': 'Please insert a correct user id'}, 400
        except:
            return {'message': 'An error occurred while saving your estate'}, 500


class EditEstate(Resource):

    # create request parser with non required id_user
    parser_edit = create_request_parser(False)

    # Update estate by user id and estate id using HTTP PUT request
    def put(self, id_user, id_estate):
        data = EditEstate.parser_edit.parse_args()
        try:
            estate = EstateModel.find_by_id(id_estate)

            # We handle the case of an owner can only modify the characteristics of his property
            #  without having access to the edition of the other owners
            if id_user != estate.id_user:
                raise PermissionError

            # Filling new updated data
            estate.name = estate.name if data.name is None else data.name
            estate.description = estate.description if data.description is None else data.description
            estate.es_type = estate.es_type if data.es_type is None else data.es_type
            estate.city = estate.city if data.city is None else data.city

            # Save and commit changes
            estate.save_to_db()

            return estate.json(), 200

        except NoResultFound:
            return {'message': 'Please make sure the estate id is correct'}, 400
        except PermissionError:
            return {'message': 'Access denied'}, 403
        except:
            return {'message': 'An error occurred while updating the estate'}, 500
