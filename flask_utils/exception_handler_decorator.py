from functools import wraps

from flask import Response


def flask_return_err_if_exception(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            return Response(str(ex), status=500)

    return wrapped
