import json

class Encoder(json.JSONEncoder):
    """
    JSONEncoder subclass that leverages an object's `__json__()` method,
    if available, to obtain its default JSON representation.
    """
    def default(obj):
        if hasattr(obj, 'json'):
            return obj.json();
        return super().default(self, obj)

