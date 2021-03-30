import requests


class Launches:
    """
    Represents SpaceX Launches
    """

    def __init__(self, url):
        self.url = f'{url}/launches'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def launches(self):
        """Gets general launch information about SpaceX Launches

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_launch(self, id):
        """Gets information on one Launch

        Args:
            id: launch id

        Returns:
            data: JSON String
        """

        params = {'id': id}

        data = self.get_data("", params=params)

        return data

    def past_launches(self):
        """Gets past launch information about SpaceX Launches

        Returns:
            data: JSON String
        """
        data = self.get_data('/past', params=None)

        return data

    def upcoming_launch(self):
        """Gets upcoming launch information about SpaceX Launches

        Returns:
            data: JSON String
        """
        data = self.get_data('/upcoming', params=None)

        return data

    def latest_launch(self):
        """Gets latest launch information about SpaceX Launch

        Returns:
            data: JSON String
        """
        data = self.get_data('/latest', params=None)

        return data

    def next_launch(self):
        """Gets next launch information about SpaceX Launch

        Returns:
            data: JSON String
        """
        data = self.get_data('/next', params=None)

        return data
