import requests
from pySpaceX.exceptions import ApiNoSuccess


class Starlink:
    """
    Represents SpaceX Starlink Object
    """

    def __init__(self, url):
        self.url = f'{url}/starlink'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def starlink(self) -> list:
        """
        Returns information about all starlink sats
        """
        data = self._get_data(None)

        return data

    def one_starlink(self, id: str) -> dict:
        """
        Returns information about one starlink sat

        :param id: ID of starlink satellite
        """
        data = self._get_data(id)

        return data
