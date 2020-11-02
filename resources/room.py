from flask_restful import Resource, reqparse
from sqlalchemy.orm.exc import NoResultFound

from models.room import RoomModel
from models.estate import EstateModel


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
                        help="Every room needs a valid name")

    parser.add_argument('characteristic',
                        type=valid_string,
                        required=required,
                        help="Every room needs a valid characteristic")

    return parser


class Room(Resource):
    parser_add = create_request_parser(True)

    # Add room by user id and estate id using HTTP POST request
    def post(self, id_user, id_estate):
        data = Room.parser_add.parse_args()
        try:
            estate = EstateModel.find_by_id(id_estate)

            # We handle the case of an owner can only modify the characteristics of his property
            #  without having access to the edition of the other owners
            if id_user != estate.id_user:
                raise PermissionError

            room = RoomModel(id_estate, **data)
            room.save_to_db()

            return room.json(), 201

        except NoResultFound:
            return {'message': 'Please make sure the estate id is correct'}, 400
        except PermissionError:
            return {'message': 'Access denied'}, 403
        except:
            return {'message': 'An error occurred while inserting the room'}, 500


class EditRoom(Resource):
    parser_edit = create_request_parser(False)

    # Update room by user id, room id and estate id using HTTP PUT request
    def put(self, id_user, id_estate, id_room):
        data = EditRoom.parser_edit.parse_args()

        try:
            room = RoomModel.find_by_id(id_room, id_estate)
            estate = EstateModel.find_by_id(id_estate)

            # We handle the case of an owner can only modify the characteristics of his property
            #  without having access to the edition of the other owners
            if id_user != estate.id_user:
                raise PermissionError

            # Filling data
            room.name = room.name if data.name is None else data.name
            room.characteristic = room.characteristic if data.characteristic is None else data.characteristic

            room.save_to_db()
            return room.json(), 200
        except NoResultFound:
            return {'message': 'Please make sure the id is correct'}, 400
        except PermissionError:
            return {'message': 'Access denied'}, 403
        except:
            return {'message': 'An error occurred while inserting the room'}, 500
