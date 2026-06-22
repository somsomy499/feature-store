"""Offline feature store backed by Parquet/Delta Lake."""
import os
from typing import List, Dict, Optional
from datetime import datetime
import hashlib

class OfflineStore:
    def __init__(self, path: str = "/data/features"):
        self.path = path
        os.makedirs(path, exist_ok=True)
        
    def write_features(self, feature_group: str, data: List[Dict], version: str = None):
        version = version or datetime.now().strftime("%Y%m%d_%H%M%S")
        dir_path = os.path.join(self.path, feature_group, version)
        os.makedirs(dir_path, exist_ok=True)
        # Write as parquet (placeholder)
        return {"path": dir_path, "rows": len(data), "version": version}
        
    def read_features(self, feature_group: str, version: str = None, limit: int = None):
        return []  # Read from parquet
        
    def list_versions(self, feature_group: str):
        dir_path = os.path.join(self.path, feature_group)
        if os.path.exists(dir_path):
            return sorted(os.listdir(dir_path))
        return []
        
    def get_latest_version(self, feature_group: str):
        versions = self.list_versions(feature_group)
        return versions[-1] if versions else None
