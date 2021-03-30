import requests


class Ships:
    """
    Represents SpaceX Payloads Object
    """

    def __init__(self, url):
        self.url = f'{url}/ships'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def payloads(self, params: dict = None):
        """Gets information about all SpaceX Ships

        Args:
            params (dict, optional): https://docs.spacexdata.com/#e520e500-0421-4774-8bcb-8d07b7dfa222

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=params)

        return data

    def one_payload(self, id):
        """Gets information about a single SpaceX ship

        Args:
            id: ship id

        Returns:
            data: JSON String
        """

        data = self.get_data('', params={'id': id})

        return data
