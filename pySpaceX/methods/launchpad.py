import requests
from pySpaceX.exceptions import ApiNoSuccess


class Launchpad:
    """
    Represents SpaceX Launchpad Object
    """

    def __init__(self, url):
        self.url = f'{url}/launchpads'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def landing_pads(self) -> list:
        """
        Returns information about all SpaceX launchpads
        """
        data = self._get_data(None)

        return data

    def one_landing_pad(self, id: str) -> dict:
        """
        Returns information about a single SpaceX launchpad

        :param id: ID of a launchpad
        """

        data = self._get_data(id)

        return data
