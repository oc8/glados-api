from glados import create_app
from glados.models import Entity

app = create_app()


print(Entity.to_json_filter)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
