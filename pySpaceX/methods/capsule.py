import requests


class Capsule:
    """
    Represents SpaceX Capsule Object
    """

    def __init__(self, url):
        self.url = f'{url}/capsules'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def capsules(self):
        """Gets information about all capsules

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_capsule(self, id):
        """Gets information about one capsule

        Args:
            id: Capsule serial number

        Returns:
            data: JSON String
        """
        params = {'id': id}
        data = self.get_data('', params=params)

        return data[0]
