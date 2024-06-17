from flask_redis import FlaskRedis
from app import app

class Redis():
    def __init__(self) -> None:
        self.redis_client = FlaskRedis()
        self.redis_client.init_app(app)
    
    def set(self, key, value):
        self.redis_client.set(key, value)
    
    def lpush(self, key, value):
        self.redis_client.lpush(key, value)

    def lrange(self, key, start, end):
        return self.redis_client.lrange(key, start, end)
    
    def get(self, key):
        value = self.redis_client.get(key)
        if value:
            return value.decode()
        else:
            return None
    
    def delete(self, key):
        return self.redis_client.delete(key)

redis = Redis()