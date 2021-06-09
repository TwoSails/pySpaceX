import requests
from pySpaceX.exceptions import ApiNoSuccess


class Dragons:
    """
    Represents SpaceX Dragons Object
    """

    def __init__(self, url):
        self.url = f'{url}/dragons'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def dragons(self) -> list:
        """
        Returns information on all dragon capsules
        """
        data = self._get_data(None)

        return data

    def one_dragon(self, id: str) -> dict:
        """
        Returns information on a single dragon capsule

        :param id: ID of the dragon
        """
        data = self._get_data(id)

        return data
