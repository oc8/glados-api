from glados.models import Entity, Room
import uuid
from datetime import datetime

def get_entities(filters):
    query = Entity.query

    type = filters.get("type")
    status = filters.get("status")
    room_id = filters.get("room_id")

    if type:
      query = query.filter(Entity.type == type)
    if status:
      query = query.filter(Entity.status == status)
    if room_id:
      query = query.filter(Entity.room_id == room_id)

    return query

def create_entity(item):
		entity = Entity(
				name=item["name"],
				type=item["type"],
				status=item["status"],
				value=item.get("value")
		)

		if "room_id" in item:
				entity.room_id = item["room_id"]

		entity.save()

		return entity

def update_entity(entity, item):
		if "status" in item:
				entity.status = item["status"]
		if "value" in item:
				entity.value = item["value"]

		entity.save()

		return entity

def delete_entity(entity):
		entity.delete()

		return entity
