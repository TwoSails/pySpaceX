import requests
from pySpaceX.exceptions import ApiNoSuccess


class Info:
    """
    Represents SpaceX Company Info and API info Object
    """

    def __init__(self, url):
        self.url = f'{url}/'

    def _get_data(self, url, params):
        if params is not None:
            response = requests.get(self.url + url + f"/{params}")
        else:
            response = requests.get(self.url + url)

        if response.status_code == 404:
            raise ApiNoSuccess
        else:
            return response.json()

    def company(self) -> dict:
        """
        Returns general company information about SpaceX
        """
        data = self._get_data('company', params=None)

        return data

    def get_api(self) -> dict:
        """
        Returns information on the API
        """

        data = self._get_data('', params=None)

        return data
