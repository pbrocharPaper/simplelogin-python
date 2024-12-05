from dotenv import get_key, load_dotenv, set_key

def save_token(token: str):
    set_key(dotenv_path=".env", key_to_set="SIMPLE_LOGIN_KEY", value_to_set=token)

def get_token():
    return get_key(dotenv_path=".env", key_to_get="SIMPLE_LOGIN_KEY")