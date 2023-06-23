from flask import request
from flask_restful import Resource

from glados.api.room.serializers import *
from glados.repositories.rooms import *

class RoomsAPI(Resource):
		def get(self):
				rooms = get_rooms()

				serializer = RoomResponseSerializer(many=True)
				return serializer.dump(rooms), 200
