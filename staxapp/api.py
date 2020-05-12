import requests

from staxapp.config import Config
from staxapp.exceptions import ApiException


class Api:
    _requests_auth = None

    @classmethod
    def _auth(cls, **kwargs):
        if not cls._requests_auth:
            cls._requests_auth = Config.get_auth_class().requests_auth(
                Config.access_key, Config.secret_key, **kwargs
            )
        return cls._requests_auth

    @staticmethod
    def handle_api_response(response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise ApiException(str(e), response)

    @classmethod
    def get(cls, url_frag, params={}, **kwargs):
        url_frag = url_frag.replace(f"/{Config.API_VERSION}", "")
        url = f"{Config.api_base_url()}/{url_frag.lstrip('/')}"

        response = requests.get(url, auth=cls._auth(), params=params, **kwargs)
        cls.handle_api_response(response)
        return response.json()

    @classmethod
    def post(cls, url_frag, payload={}, **kwargs):
        url_frag = url_frag.replace(f"/{Config.API_VERSION}", "")
        url = f"{Config.api_base_url()}/{url_frag.lstrip('/')}"

        response = requests.post(url, json=payload, auth=cls._auth(), **kwargs)
        cls.handle_api_response(response)
        return response.json()

    @classmethod
    def put(cls, url_frag, payload={}, **kwargs):
        url_frag = url_frag.replace(f"/{Config.API_VERSION}", "")
        url = f"{Config.api_base_url()}/{url_frag.lstrip('/')}"

        response = requests.put(url, json=payload, auth=cls._auth(), **kwargs)
        cls.handle_api_response(response)
        return response.json()

    @classmethod
    def delete(cls, url_frag, params={}, **kwargs):
        url_frag = url_frag.replace(f"/{Config.API_VERSION}", "")
        url = f"{Config.api_base_url()}/{url_frag.lstrip('/')}"

        response = requests.delete(url, auth=cls._auth(), params=params, **kwargs)
        cls.handle_api_response(response)
        return response.json()
