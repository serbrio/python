import json

def to_json(func_to_decorate):
    def wrapper(*args, **kwargs):
        result = json.dumps(func_to_decorate(*args, **kwargs))
        return result
    wrapper.__name__ = func_to_decorate.__name__
    return wrapper