import requests
from pySpaceX.exceptions import ApiNoSuccess


class Rockets:
    """
    Represents SpaceX Rockets Object
    """

    def __init__(self, url):
        self.url = f'{url}/rockets'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def rockets(self) -> list:
        """
        Returns information about all SpaceX rockets
        """
        data = self._get_data(None)

        return data

    def one_rocket(self, id: str) -> dict:
        """
        Returns information about a single SpaceX rocket
        :param id: rocket id
        """
        data = self._get_data(id)

        return data
