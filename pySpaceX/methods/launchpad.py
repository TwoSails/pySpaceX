import requests


class Launchpad:
    """
    Represents SpaceX Launchpad Object
    """

    def __init__(self, url):
        self.url = f'{url}/launchpads'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def landing_pads(self):
        """Gets information about all SpaceX launchpads

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_landing_pad(self, site_id: str):
        """Gets information about a single SpaceX launchpad

        Args:
            site_id (str): site id of launch pad

        Returns:
            data: JSON String
        """

        data = self.get_data(f'/{site_id}', params=None)

        return data
