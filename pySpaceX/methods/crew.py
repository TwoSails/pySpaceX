import requests
from pySpaceX.exceptions import ApiNoSuccess


class Crew:
    """
    Represents SpaceX Capsule Object
    """

    def __init__(self, url):
        self.url = f'{url}/crew'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def members(self) -> list:
        """
        Returns information about all crew members
        """
        data = self._get_data(None)

        return data

    def one_crew_member(self, id: str) -> dict:
        """
        Returns information about one crew member

        :param id: ID of crew member
        """
        data = self._get_data(id)

        return data
