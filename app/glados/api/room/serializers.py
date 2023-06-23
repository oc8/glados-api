from marshmallow import fields, validate

from glados import ma, constants
from glados.models import Entity

class RoomResponseSerializer(ma.Schema):
		id = fields.UUID()
		name = fields.String()

class RoomsResponseSerializer(ma.Schema):
		rooms = fields.List(fields.Nested(RoomResponseSerializer))
