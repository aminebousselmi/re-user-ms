from sqlalchemy.orm.exc import NoResultFound
from db import db


class RoomModel(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)  # primary key
    name = db.Column(db.String(80))  # limited to 80 Char
    characteristic = db.Column(db.String(100))  # limited to 100 Char
    # room match only one real estate
    id_estate = db.Column(db.Integer, db.ForeignKey(
        'estates.id'))  # linking estate id row with an room's id_estate, many to one relationship
    estate = db.relationship('EstateModel')  # join

    def __init__(self, id_estate, characteristic, name):
        self.characteristic = characteristic
        self.name = name
        self.id_estate = id_estate

    # Displaying data in a correct format
    def json(self):
        return {'id': self.id, 'name': self.name, 'characteristic': self.characteristic, 'id_estate': self.id_estate}

    # Save room in database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id_room, id_estate):
        # SELECT * FROM rooms WHERE id=id_room and id_estate=current_id_estate
        data = cls.query.filter_by(id=id_room, id_estate=id_estate).first()

        if data is None:
            raise NoResultFound
        else:
            return data
