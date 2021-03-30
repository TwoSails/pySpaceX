import requests


class Crew:
    """
    Represents SpaceX Capsule Object
    """

    def __init__(self, url):
        self.url = f'{url}/crew'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def members(self):
        """Gets information about all crew members

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_crew_member(self, id):
        """Gets information about one crew member

        Args:
            id: ID of crew member

        Returns:
            data: JSON String
        """
        params = {'id': id}
        data = self.get_data('', params=params)

        return data[0]
