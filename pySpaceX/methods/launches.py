import requests
from pySpaceX.exceptions import ApiNoSuccess


class Launches:
    """
    Represents SpaceX Launches
    """

    def __init__(self, url):
        self.url = f'{url}/launches'

    def _get_data(self, url, params):
        if params is not None:
            response = requests.get(self.url + f"/{params}")
        else:
            response = requests.get(self.url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def launches(self) -> list:
        """
        Returns general launch information about all SpaceX Launches
        """
        data = self._get_data('', params=None)

        return data

    def one_launch(self, id: str) -> dict:
        """
        Returns information on one Launch
        :param id: ID of Launch
        """
        data = self._get_data("", params=id)

        return data

    def past_launches(self) -> list:
        """
        Returns past launch information about SpaceX Launches
        """
        data = self._get_data('/past', params=None)

        return data

    def upcoming_launches(self) -> list:
        """
        Returns upcoming launch information about SpaceX Launches
        """
        data = self._get_data('/upcoming', params=None)

        return data

    def latest_launch(self) -> dict:
        """
        Returns latest launch information about SpaceX Launch
        """
        data = self._get_data('/latest', params=None)

        return data

    def next_launch(self) -> dict:
        """Returns next launch information about SpaceX Launch
        """
        data = self._get_data('/next', params=None)

        return data
