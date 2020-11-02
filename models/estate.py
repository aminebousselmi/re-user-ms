from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound
from db import db


class EstateModel(db.Model):
    __tablename__ = 'estates'

    id = db.Column(db.Integer, primary_key=True)  # primary key
    name = db.Column(db.String(80))  # limited to 80 Char
    description = db.Column(db.String(100))  # limited to 100 Char
    es_type = db.Column(db.String(80))  # limited to 80 Char
    city = db.Column(db.String(80))  # limited to 80 Char

    # Estate has One To Many rooms
    rooms = db.relationship('RoomModel', lazy='dynamic')
    # estate match only one user
    id_user = db.Column(db.Integer, db.ForeignKey(
        'users.id'))  # linking user id row with an estate's id_user, many to one relationship
    user = db.relationship('UserModel')  # join

    def __init__(self, name, description, es_type, city, id_user):
        self.name = name
        self.description = description
        self.es_type = es_type
        self.city = city
        self.id_user = id_user

    # Displaying data in a correct format
    def json(self):
        return {'id': self.id, 'name': self.name, 'description': self.description, 'type': self.es_type,
                'city': self.city, 'id_user': self.id_user, 'rooms': [room.json() for room in self.rooms.all()]}

    # Save estate in database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_city(cls, city):
        # SELECT * FROM estates WHERE city=city
        data = cls.query.filter(func.lower(EstateModel.city) == func.lower(city)).all()

        if not data:
            raise NoResultFound
        else:
            return data

    @classmethod
    def find_by_id(cls, id_estate):
        # SELECT * FROM estates WHERE id=id_estate
        data = cls.query.filter_by(id=id_estate).first()
        if data is None:
            raise NoResultFound
        else:
            return data
