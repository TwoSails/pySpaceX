import requests
from pySpaceX.exceptions import ApiNoSuccess


class Capsule:
    """
    Represents SpaceX Capsule Object
    """

    def __init__(self, url):
        self.url = f'{url}/capsules'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def capsules(self) -> list:
        """
        Returns information about all capsules
        """
        data = self._get_data(params=None)

        return data

    def one_capsule(self, id: str) -> dict:
        """
        Returns information about one capsule

        :param id: Capsule serial number
        """
        data = self._get_data(params=id)

        return data
