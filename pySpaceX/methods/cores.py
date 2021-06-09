import requests
from pySpaceX.exceptions import ApiNoSuccess


class Cores:
    """
    Represents SpaceX Cores Object
    """

    def __init__(self, url):
        self.url = f'{url}/cores'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def cores(self) -> list:
        """
        Returns information on all cores
        """
        data = self._get_data(params=None)

        return data

    def one_core(self, id: str) -> dict:
        """
        Returns information on a single core

        :param id: ID of the core
        """
        data = self._get_data(params=id)

        return data
