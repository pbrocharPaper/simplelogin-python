from simplelogin.models import SimpleLoginAlias
from simplelogin.connector import new_random_from_sl, remove_alias_from_sl, login_to_sl, get_aliases_from_sl, \
    async_get_range_pages, get_cookie_token
from simplelogin.exceptions import SimpleLoginError
from simplelogin import settings
import asyncio

class SimpleLogin:
    def __init__(self, token: str | None = None):
        self.token = token
        self._aliases = None

    @property
    def aliases(self):
        self._aliases = [SimpleLoginAlias(alias) for alias in get_aliases_from_sl(self.token, 0)]
        return self._aliases

    def async_get_aliases(self, max_page: int = 1, from_page: int = 0):
        aliases = []
        loop = asyncio.get_event_loop()
        pages = loop.run_until_complete(async_get_range_pages(self.token, max_page, from_page))
        for page in pages:
            aliases.extend(SimpleLoginAlias(alias) for alias in page)
        return aliases

    def get_aliases(self, max_page: int = 1, from_page: int = 0):
        for current_page in range(max_page):
            raw_aliases = get_aliases_from_sl(self.token, current_page)
            alias_count = len(raw_aliases)
            if alias_count == 0:
                break
            else:
                aliases = [SimpleLoginAlias(alias) for alias in raw_aliases]
                yield aliases
            aliases.extend(SimpleLoginAlias(alias) for alias in raw_aliases)
            if alias_count < 20:
                break
        return aliases

    def new_random_alias(self, hostname: str | None = None, mode: str = "word"):
        try:
            alias = new_random_from_sl(self.token, hostname, mode)
        except SimpleLoginError:
            raise
        else:
            return SimpleLoginAlias(alias)

    def remove_alias(self, alias_id: int):
        try:
            response = remove_alias_from_sl(self.token, alias_id)
        except SimpleLoginError:
            raise
        return response.get("deleted")

    def remove_aliases(self):
        for alias in self.aliases:
            is_deleted = self.remove_alias(alias.id)
            yield alias, is_deleted

    @staticmethod
    def get_token(email: str, password: str, device: str | None = None):
        if not device:
            device = "terminal"
        try:
            user_info = login_to_sl(email, password, device)
            return user_info.get("api_key")
        except SimpleLoginError:
            raise

    def set_token(self, email: str, password: str, device: str | None = None, set_settings_token: bool = False):
        token = self.get_token(email, password, device)
        self.token = token
        if set_settings_token:
            settings.TOKEN = token

    def get_cookie_token(self):
        return get_cookie_token(self.token)



