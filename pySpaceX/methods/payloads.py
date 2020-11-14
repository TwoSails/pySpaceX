import requests


class Payload:
    """
    Represents SpaceX Payloads Object
    """

    def __init__(self, url):
        self.url = f'{url}/payloads'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def payloads(self, params: dict = None):
        """Gets information about all SpaceX missions

        Args:
            params (dict, optional): https://docs.spacexdata.com/#81150545-5ab3-4552-b1f5-865b7f542033

        Returns:
            data: JSON String
        """
        data = self.get_data('', params=params)

        return data

    def one_payload(self, payload_id):
        """Gets information about a single SpaceX landing pad

        Args:
            payload_id (str): payload id

        Returns:
            data: JSON String
        """

        data = self.get_data(f'/{payload_id}', params=None)

        return data
