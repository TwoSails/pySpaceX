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
        """Gets information on all dragon capsules

        Returns:
            data: JSON String
        """
        data = self.get_data(params=None)

        return data

    def one_dragon(self, id):
        """Gets information on a single dragon capsule

        Returns:
            data: JSON String
        """

        params = {'id': id}
        data = self.get_data(params=params)

        return data[0]
