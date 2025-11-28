import time
from typing import Any, Optional

class SimpleCache:
    def __init__(self):
        self._store: dict[str, tuple[float, Any]] = {}

    def set(self, key: str, value: Any, ttl: int):
        expire_at = time.time() + ttl
        self._store[key] = (expire_at, value)

    def get(self, key: str) -> Optional[Any]:
        row = self._store.get(key)
        if not row:
            return None
        expire_at, value = row
        if time.time() > expire_at:
            del self._store[key]
            return None
        return value

cache = SimpleCache()
