import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **keys):
        return json.dumps(func(*args, **keys))
    return wrapped 