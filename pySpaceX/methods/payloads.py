import requests


class Payloads:
    """
    Represents SpaceX Payloads Object
    """

    def __init__(self, url):
        self.url = f'{url}/payloads'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def payloads(self):
        """Gets information about all SpaceX missions

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_payload(self, id):
        """Gets information about a single SpaceX landing pad

        Args:
            id: payload id

        Returns:
            data: JSON String
        """

        data = self.get_data('', params={'id': id})

        return data
