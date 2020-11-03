import requests


class Dragons:
    """
    Represents SpaceX Dragons Object
    """

    def __init__(self, url):
        self.url = f'{url}/dragons'

    def get_data(self, params):
        response = requests.get(self.url, params=params)

        return response.json()

    def dragons(self):
        """
        Returns information on all dragon capsules
        """
        data = self.get_data(params=None)

        return data

    def one_dragon(self, serial):
        """
        Returns information on a single dragon capsule
        """

        params = {'core_serial': serial}
        data = self.get_data(params=params)

        return data[0]
