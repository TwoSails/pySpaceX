import requests
from pySpaceX.exceptions import ApiNoSuccess
from typing import Optional


class Ships:
    """
    Represents SpaceX Payloads Object
    """

    def __init__(self, url):
        self.url = f'{url}/ships'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def ships(self) -> list:
        """
        Returns information about all SpaceX Ships
        """
        data = self._get_data(None)

        return data

    def one_payload(self, id: str) -> dict:
        """
        Returns information about a single SpaceX ship
        :param id: ship id
        """
        data = self._get_data(id)

        return data
