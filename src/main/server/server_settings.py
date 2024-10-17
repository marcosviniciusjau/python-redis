from flask import Flask

from src.models.redis.settings.connection import RedisConnHandler
from src.models.sqlite.settings.connection import SQLiteConnection

redis_connection= RedisConnHandler()
sqlite_connection= SQLiteConnection()

redis_connection.connect()
sqlite_connection.connect()

app = Flask(__name__)

from src.main.routes.products_routes import products_routes_bp
app.register_blueprint(products_routes_bp)