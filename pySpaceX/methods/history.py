import requests
from pySpaceX.exceptions import ApiNoSuccess


class History:
    """
    Represents SpaceX History Object
    """

    def __init__(self, url):
        self.url = f'{url}/history'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def history(self) -> list:
        """
        Returns information on all historical events
        """
        data = self._get_data(None)

        return data

    def one_history(self, id: str) -> dict:
        """
        Returns information on one historic event

        :param id: ID of the historic event
        """
        data = self._get_data(id)

        return data
