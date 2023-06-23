from marshmallow import fields, validate

from glados import ma, constants
from glados.models import Entity


class EntitiesRequestSerializer(ma.Schema):
    type = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityType]))
    status = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityStatus]))
    room_id = fields.String(required=False)


class EntitySerializer(ma.Schema):
    created_at = fields.DateTime("%Y-%m-%dT%H:%M:%S")

    class Meta:
        model = Entity
        ordered = True
        fields = [
            "id",
            "name",
            "type",
						"status",
            "value",
						"room_id",
            "created_at"
        ]

class EntityResponseSerializer(EntitySerializer):
    pass

class EntityPostRequestSerializer(ma.Schema):
		name = fields.String(required=True)
		type = fields.String(required=True, validate=validate.OneOf([x.name for x in constants.EntityType]))
		status = fields.String(required=True, validate=validate.OneOf([x.name for x in constants.EntityStatus]))
		value = fields.String(required=False)
		room_id = fields.String(required=True)

class EntityPostResponseSerializer(EntitySerializer):
		pass

class EntityPatchRequestSerializer(ma.Schema):
		status = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityStatus]))
		value = fields.String(required=False)

class EntityPatchResponseSerializer(EntitySerializer):
		pass
