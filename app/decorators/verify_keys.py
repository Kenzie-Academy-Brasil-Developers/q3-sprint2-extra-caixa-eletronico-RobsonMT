from datetime import date
from functools import wraps
from typing import Callable
from flask import request


def verify_keys(trusted_keys: list[str]):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper():
            body_keys = request.get_json().keys()
            invalid_keys = set(trusted_keys) - body_keys

            try:
                if invalid_keys:
                    raise KeyError({
                            "error": "chave(s) incorreta(s)",
                            "expected": list(trusted_keys),
                            "received": list(body_keys),
                        })
                return func()
            except KeyError as e:
                return e.args[0], 400
                
        return wrapper   
    return decorator