import requests


class Roadster:
    """
    Represents SpaceX Roadster Object
    """

    def __init__(self, url):
        self.url = f'{url}/roadster'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def missions(self):
        """Gets information about SpaceX Roadster

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data
