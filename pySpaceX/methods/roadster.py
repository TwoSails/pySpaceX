import requests
from pySpaceX.exceptions import ApiNoSuccess


class Roadster:
    """
    Represents SpaceX Roadster Object
    """

    def __init__(self, url):
        self.url = f'{url}/roadster'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def roadster(self) -> dict:
        """
        Returns information about SpaceX Roadster
        """
        data = self._get_data(None)

        return data
