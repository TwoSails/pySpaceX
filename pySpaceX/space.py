"""
Program: A www.spacexdata.com API Wrapper
Author: TwoSails
Description: A simple python API Wrapper made for use with the www.spacexdata.com
Version: 1.0.0 BETA
"""
import requests
from .methods.capsule import Capsule
from .methods.cores import Cores
from .methods.dragons import Dragons

__version__ = '1.0.0 BETA'


class Space:
    """
    Represents SpaceAPI object with general methods
    """

    def __init__(self):
        self.APIver = 'v3'
        self.url = f'www.api.spacexdata.com/{self.APIver}'

    def get_data(self, params):
        """
        Executes HTTP request with base url and given endpoints
        Args:
            params: dictionary
        Returns:
             response: JSON data
        """
        response = requests.get(self.url, params=params).json()

        return response

    def get_capsule(self):
        """Gets information about SpaceX capsules

        Returns:
            Capsule: Capsule Object
        """
        return Capsule(self.url)

    def get_core(self):
        """Gets information about SpaceX core stages
        Returns:
            Cores: Cores Object
        """
        return Cores(self.url)

    def get_dragon(self):
        """Gets information about SpaceX dragon capsules
        Returns:
            Dragons: Dragons Object
        """
        return Dragons(self.url)
