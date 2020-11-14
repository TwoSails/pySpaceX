import requests


class Rockets:
    """
    Represents SpaceX Rockets Object
    """

    def __init__(self, url):
        self.url = f'{url}/rockets'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def rockets(self):
        """Gets information about all SpaceX rockets

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_rocket(self, rocket_id):
        """Gets information about a single SpaceX rocket

        Args:
            rocket_id (str): rocket id

        Returns:
            data: JSON String
        """

        data = self.get_data(f'/{rocket_id}', params=None)

        return data
