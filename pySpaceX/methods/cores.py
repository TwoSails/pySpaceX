import requests


class Cores:
    """
    Represents SpaceX Cores Object
    """

    def __init__(self, url):
        self.url = f'{url}/cores'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def cores(self):
        """
        Returns information on all cores
        """
        data = self.get_data('', params=None)

        return data

    def one_core(self, id):
        """
        Returns information on a single core
        """

        params = {'id': id}
        data = self.get_data('', params=params)

        return data[0]
