"""Feature computation pipeline."""
from typing import List, Dict, Callable
from dataclasses import dataclass
import time

@dataclass
class FeatureDefinition:
    name: str
    entity_key: str
    compute_fn: Callable
    ttl_seconds: int = 3600
    description: str = ""

class FeaturePipeline:
    def __init__(self):
        self.features: Dict[str, FeatureDefinition] = {}
        self.computation_log = []
        
    def register(self, feature: FeatureDefinition):
        self.features[feature.name] = feature
        
    def compute(self, name: str, entity_data: Dict):
        if name not in self.features:
            raise ValueError(f"Unknown feature: {name}")
        fd = self.features[name]
        start = time.time()
        value = fd.compute_fn(entity_data)
        elapsed = time.time() - start
        self.computation_log.append({"feature": name, "time_ms": elapsed * 1000})
        return value
        
    def compute_all(self, entity_data: Dict):
        results = {}
        for name in self.features:
            results[name] = self.compute(name, entity_data)
        return results
        
    def list_features(self):
        return [{"name": f.name, "ttl": f.ttl_seconds, "desc": f.description} 
                for f in self.features.values()]
