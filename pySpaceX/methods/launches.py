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

    def launches(self, params: dict = None):
        """Gets general launch information about SpaceX Launches

        Args:
            params (dict, optional): https://docs.spacexdata.com/#bc65ba60-decf-4289-bb04-4ca9df01b9c1

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=params)

        return data

    def one_launch(self, flight_number: int):
        """Gets information on one Launch

        Args:
            flight_number (int): flight number

        Returns:
            data: JSON String
        """

        params = {"flight_number": flight_number}

        data = self.get_data("", params=params)

        return data

    def past_launches(self, params: dict):
        """Gets past launch information about SpaceX Launches

        Args:
            params (dict): https://docs.spacexdata.com/#fce450d6-e064-499a-b88d-34cc22991bcc

        Returns:
            data: JSON String
        """
        data = self.get_data('/past', params=params)

        return data

    def upcoming_launch(self, params: dict):
        """Gets upcoming launch information about SpaceX Launches

        Args:
            params (dict): https://docs.spacexdata.com/#e001c501-9c09-4703-9e29-f91fbbf8db7c

        Returns:
            data: JSON String
        """
        data = self.get_data('/upcoming', params=params)

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
