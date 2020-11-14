import requests


class Info:
    """
    Represents SpaceX Info and API info Object
    """

    def __init__(self, url):
        self.url = f'{url}/'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def company(self):
        """Gets general company information about SpaceX

        Returns:
            data: JSON String
        """
        data = self.get_data('info', params=None)

        return data

    def get_api(self):
        """Gets information on the API

        Returns:
            data: JSON String
        """

        data = self.get_data('', params=None)

        return data
