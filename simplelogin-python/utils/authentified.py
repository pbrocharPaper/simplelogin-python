from functools import wraps
from utils.environment import get_token

def authentified(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = get_token()
        if token is None or token == '':
            print(f'You need to set a token first')
        else:
            return func(*args, **kwargs)
    return wrapper