import requests
from pySpaceX.exceptions import ApiNoSuccess


class Fairings:
    """
    Represents SpaceX Fairing Object
    """

    def __init__(self, url):
        self.url = f'{url}/fairings'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def fairings(self) -> list:
        """
        Returns information about all fairings
        """
        data = self._get_data(None)

        return data

    def one_fairing(self, id: str) -> dict:
        """Gets information about one fairing

        :param id: Fairing serial number
        """
        data = self._get_data(id)

        return data
