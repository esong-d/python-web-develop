from flask_redis import FlaskRedis
from app import app

class Redis():
    def __init__(self) -> None:
        self.redis_client = FlaskRedis()
        self.redis_client.init_app(app)
        self.redis_pipeline = self.redis_client.pipeline()
    
    def set(self, key, value):
        self.redis_pipeline.set(key, value)
    
    def get(self, key):
        value = self.redis_pipeline.get(key)
        if value:
            return value.decode()
        else:
            return None
    
    def delete(self, key):
        return self.redis_pipeline.delete(key)

redis = Redis()