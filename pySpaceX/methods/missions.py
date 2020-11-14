import requests


class Missions:
    """
    Represents SpaceX Missions Object
    """

    def __init__(self, url):
        self.url = f'{url}/missions'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def missions(self):
        """Gets information about all SpaceX missions

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_landing_pad(self, mission_id):
        """Gets information about a single SpaceX landing pad

        Args:
            mission_id (str): mission id

        Returns:
            data: JSON String
        """

        data = self.get_data(f'/{mission_id}', params=None)

        return data
