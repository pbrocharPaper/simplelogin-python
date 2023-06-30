import asyncio
import pickle

from simplelogin.settings import BASE_URL
from simplelogin.exceptions import SimpleLoginError
import requests
import aiohttp


async def async_get_aliases_from_sl(session, token: str, page_id: int):
    async with session.get(
        url=f"{BASE_URL}/api/v2/aliases",
        headers={"Authentication": token},
        params={"page_id": page_id}
    ) as response:
        return await response.json()


async def async_get_range_pages(token: str, range_pages: int = 1, from_page: int = 0):
    async with aiohttp.ClientSession() as session:
        tasks = []
        if from_page >= range_pages:
            range_pages = from_page + 1
        for page_number in range(from_page, range_pages):
            task = asyncio.create_task(async_get_aliases_from_sl(session, token, page_number))
            tasks.append(task)

        pages = await asyncio.gather(*tasks)

        return [page.get("aliases") for page in pages]



def get_aliases_from_sl(token: str, page_id: int):
    response = requests.get(
        url=f"{BASE_URL}/api/v2/aliases",
        headers={"Authentication": token},
        params={"page_id": page_id},
    )
    response.raise_for_status()
    return response.json().get("aliases")


def new_random_from_sl(token: str, hostname: str | None = None, mode: str = "word"):
    response = requests.post(
        url=f"{BASE_URL}/api/alias/random/new",
        headers={"Authentication": token},
        params={"hostname": hostname, "mode": mode},
    )
    try:
        response.raise_for_status()
    except requests.HTTPError:
        raise SimpleLoginError(response.json().get("error"))
    return response.json()


def remove_alias_from_sl(token: str, alias_id: int):
    response = requests.delete(
        url=f"{BASE_URL}/api/aliases/{alias_id}",
        headers={"Authentication": token},
    )
    try:
        response.raise_for_status()
    except requests.HTTPError:
        raise SimpleLoginError(response.json().get("error"))
    return response.json()


def login_to_sl(email: str, password: str, device: str | None = None):
    response = requests.post(
        url=f"{BASE_URL}/api/auth/login",
        json={
            "email": email,
            "password": password,
            "device": device,
        }
    )
    try:
        response.raise_for_status()
    except requests.HTTPError:
        raise SimpleLoginError(response.json().get("error"))
    return response.json()


def get_cookie_token(token: str):
    response = requests.get(
        url=f"{BASE_URL}/api/user/cookie_token",
        headers={"Authentication": token}
    )
    response.raise_for_status()
    return response

