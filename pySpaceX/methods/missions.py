import requests
from pySpaceX.exceptions import ApiNoSuccess


class Missions:
    """
    Represents SpaceX Missions Object
    """

    def __init__(self, url):
        self.url = f'{url}/missions'

    def _get_data(self, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def missions(self) -> list:
        """
        Returns information about all SpaceX missions
        """
        data = self._get_data(None)

        return data

    def one_mission(self, id: str) -> dict:
        """
        Returns information about a single SpaceX landing pad
        :param id: mission id
        """

        data = self._get_data(id)

        return data
