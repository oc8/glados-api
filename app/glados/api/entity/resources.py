from flask import request
from flask_restful import Resource

from glados.api.entity.serializers import *
from glados.repositories.entities import *


class EntitiesAPI(Resource):
    def get(self):
        request_serializer = EntitiesRequestSerializer()
        data = request_serializer.load(request.args)

        entities = get_entities(data)

        serializer = EntityResponseSerializer(many=True)
        return serializer.dump(entities), 200

    def post(self):
        request_serializer = EntityPostRequestSerializer()
        data = request_serializer.load(request.json)

        entity = create_entity(data)

        serializer = EntityPostResponseSerializer()
        return serializer.dump(entity), 201

class EntityAPI(Resource):
    def patch(self, entity_id):
        entity = Entity.query.get_or_404(entity_id)

        request_serializer = EntityPatchRequestSerializer()
        data = request_serializer.load(request.json)

        entity = update_entity(entity, data)

        serializer = EntityPatchResponseSerializer()
        return serializer.dump(entity), 200

    def delete(self, entity_id):
        entity = Entity.query.get_or_404(entity_id)

        delete_entity(entity)

        return {}, 204
