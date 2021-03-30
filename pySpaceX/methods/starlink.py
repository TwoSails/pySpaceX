import requests


class Starlink:
    """
    Represents SpaceX Capsule Object
    """

    def __init__(self, url):
        self.url = f'{url}/starlink'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def starlink(self):
        """Gets information about all starlink sats

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_starlink(self, id):
        """Gets information about one starlink sat

        Args:
            id: Capsule serial number

        Returns:
            data: JSON String
        """
        params = {'id': id}
        data = self.get_data('', params=params)

        return data[0]
