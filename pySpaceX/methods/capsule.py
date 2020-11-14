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

    def one_capsule(self, serial):
        """Gets information about one capsule

        Args:
            serial: Capsule serial number

        Returns:
            data: JSON String
        """
        params = {'capsule_serial': serial}
        data = self.get_data('', params=params)

        return data[0]

    def past_capsule(self, capsule_serial: str = None, capsule_id=None, status=None, original_launch=None, mission=None,
                     landings=None, type=None, reuse_count=None):
        """Gets information about capsules which have flown before

        Args:
            capsule_serial (str, optional): capsule serial

        Returns:
            data: JSON String
        """
        params = {'capsule_serial': capsule_serial,
                  'capsule_id': capsule_id,
                  'status': status,
                  'original_launch': original_launch,
                  'mission': mission,
                  'landings': landings,
                  'type': type,
                  'reuse_count': reuse_count
                  }

        data = self.get_data('/past', params=params)

        return data

    def upcoming_capsule(self, capsule_serial=None, capsule_id=None, status=None, original_launch=None, mission=None,
                         landings=None, type=None, reuse_count=None):
        """Gets information about capsules which haven't launched yet

        Returns:
            data: JSON String
            """
        params = {'capsule_serial': capsule_serial,
                  'capsule_id': capsule_id,
                  'status': status,
                  'original_launch': original_launch,
                  'mission': mission,
                  'landings': landings,
                  'type': type,
                  'reuse_count': reuse_count
                  }

        data = self.get_data('/upcoming', params=params)

        return data
