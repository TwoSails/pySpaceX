import requests


class Cores:
    """
    Represents SpaceX Cores Object
    """

    def __init__(self, url):
        self.url = f'{url}/cores'

    def get_data(self, url, params):
        response = requests.get(self.url + url, params=params)

        return response.json()

    def cores(self):
        """
        Returns information on all cores
        """
        data = self.get_data('', params=None)

        return data

    def one_core(self, serial):
        """
        Returns information on a single core
        """

        params = {'core_serial': serial}
        data = self.get_data('', params=params)

        return data[0]

    def upcoming_cores(self, core_serial: str = None, block: int = None, status: str = None, original_launch=None,
                       mission: str = None, reuse_count: int = None, rtls_attempts: int = None,
                       rtls_landings: int = None, asds_attempts: int = None, asds_landings: int = None,
                       water_landing: bool = None):
        """
        Returns list of cores which haven't launched yet
        """
        params = {'core_serial': core_serial,
                  'block': block,
                  'status': status,
                  'original_launch': original_launch,
                  'mission': mission,
                  'reuse_count': reuse_count,
                  'rtls_attempts': rtls_attempts,
                  'rtls_landings': rtls_landings,
                  'asds_attempts': asds_attempts,
                  'asds_landings': asds_landings,
                  'water_landing': water_landing
                  }
        data = self.get_data('/upcoming', params=params)

        return data

    def past_cores(self, core_serial: str = None, block: int = None, status: str = None, original_launch=None,
                   mission: str = None, reuse_count: int = None, rtls_attempts: int = None,
                   rtls_landings: int = None, asds_attempts: int = None, asds_landings: int = None,
                   water_landing: bool = None):
        """
        Returns list of cores which have been launched before
        """
        params = {'core_serial': core_serial,
                  'block': block,
                  'status': status,
                  'original_launch': original_launch,
                  'mission': mission,
                  'reuse_count': reuse_count,
                  'rtls_attempts': rtls_attempts,
                  'rtls_landings': rtls_landings,
                  'asds_attempts': asds_attempts,
                  'asds_landings': asds_landings,
                  'water_landing': water_landing
                  }
        data = self.get_data('/past', params=params)

        return data
