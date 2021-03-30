import requests


class Landing:
    """
    Represents SpaceX Landing Pad Object
    """

    def __init__(self, url):
        self.url = f'{url}/landpads'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def landing_pads(self):
        """Gets information about all SpaceX landing pads

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=None)

        return data

    def one_landing_pad(self, id):
        """Gets information about a single SpaceX landing pad

        Args:
            id: Landing Pad ID

        Returns:
            data: JSON String
        """

        data = self.get_data('', params={'id': id})

        return data
