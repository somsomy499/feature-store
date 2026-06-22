# Feature Store 🗄️

Low-latency feature store for ML serving with online/offline parity.

## Performance

| Operation | Latency | Throughput |
|-----------|---------|-----------|
| Online get | 0.5ms | 50K/s |
| Online batch get | 2ms | 100K/s |
| Offline write | 10ms | 10K/s |

## Quick Start

```python
from feature_store import FeatureStore

store = FeatureStore(redis_url="redis://localhost:6379")
store.set("user:123", {"age": 28, "purchases": 45})
features = store.get("user:123")
```

## License

MIT