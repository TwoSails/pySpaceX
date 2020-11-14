import requests


class History:
    """
    Represents SpaceX History Object
    """

    def __init__(self, url):
        self.url = f'{url}/history'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def history(self):
        """Gets information on all historical events

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_history(self, id):
        """Gets information on one historic event

        Returns:
            data: JSON String
        """

        params = {'id': id}
        data = self.get_data('', params=params)

        return data
