import requests


class Fairings:
    """
    Represents SpaceX Fairing Object
    """

    def __init__(self, url):
        self.url = f'{url}/fairings'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def fairings(self):
        """Gets information about all fairings

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_fairing(self, id):
        """Gets information about one fairing

        Args:
            id: Fairing serial number

        Returns:
            data: JSON String
        """
        params = {'id': id}
        data = self.get_data('', params=params)

        return data[0]
