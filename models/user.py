import json
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from db import db


# convert datetime to string representation
#  We can make a utility class to ensure better reuse
def date_converter(o):
    if isinstance(o, datetime):
        return o.__str__()


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # primary key
    name = db.Column(db.String(80))  # limited to 80 Char
    last_name = db.Column(db.String(80))  # limited to 80 Char
    birth_date = db.Column(db.DateTime)

    # User has One To Many real estates
    estates = db.relationship('EstateModel', lazy='dynamic')

    def __init__(self, name, last_name, birth_date):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date

    # Displaying data in a correct format
    def json(self):
        return {'id': self.id, 'name': self.name, 'last_name': self.last_name, 'birth_date': json.dumps(self.birth_date, default=date_converter),
                'estates': [estate.json() for estate in self.estates.all()]}

    # Save user in database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id_user):
        # SELECT * FROM users WHERE id=id_user
        data = cls.query.filter_by(id=id_user).first()

        if data is None:
            raise NoResultFound
        else:
            return data
