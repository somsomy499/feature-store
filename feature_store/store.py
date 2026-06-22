"""Low-latency feature store."""
class FeatureStore:
    def __init__(self, redis_url=None):
        self.redis_url = redis_url
        self.local_cache = {}
        
    def set(self, key, features):
        self.local_cache[key] = features
        
    def get(self, key):
        return self.local_cache.get(key, {})
        
    def batch_get(self, keys):
        return {k: self.get(k) for k in keys}
