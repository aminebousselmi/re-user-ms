from datetime import datetime
from flask_restful import Resource, reqparse
from sqlalchemy.orm.exc import NoResultFound
from models.user import UserModel


# check if the type is string and is not empty
#  We can make a utility class to ensure better reuse
def valid_string(s):
    if not s or not isinstance(s, str):
        raise ValueError("Must be a valid string")
    return s


# create generic request parser for user in order to handle requirement for update and create
def create_request_parser(required):
    parser = reqparse.RequestParser()

    # Handle constraints of the input
    parser.add_argument('name',
                        type=valid_string,
                        required=required,
                        help="Every user needs a valid name")

    parser.add_argument('last_name',
                        type=valid_string,
                        required=required,
                        help="Every user needs a valid last name")

    # Date must be int the format of dd-MM-YYYY example : 19-08-1996
    parser.add_argument('birth_date',
                        type=lambda x: datetime.strptime(x, '%d-%m-%Y'),
                        required=required,
                        help="Every user needs a valid birth date")
    return parser


class UserAdd(Resource):
    parser_add = create_request_parser(True)

    # Add new user using HTTP POST request
    def post(self):
        data = UserAdd.parser_add.parse_args()
        try:
            user = UserModel(**data)
            user.save_to_db()

            return user.json(), 201
        except:
            return {'message': 'An error occurred while inserting the user'}, 500


class UserEdit(Resource):
    parser_edit = create_request_parser(False)

    # Update user by id_user using HTTP PUT request
    def put(self, id_user):
        data = UserEdit.parser_edit.parse_args()

        try:
            # Get current user by id
            user = UserModel.find_by_id(id_user)
            # filling new data
            user.name = user.name if data.name is None else data.name
            user.last_name = user.last_name if data.last_name is None else data.last_name
            user.birth_date = user.birth_date if data.birth_date is None else data.birth_date

            user.save_to_db()

            return user.json(), 200

        except NoResultFound:
            return {'message': 'Please make sure the user id is correct'}, 400
        except:
            return {'message': 'An error occurred while updating the user'}, 500
