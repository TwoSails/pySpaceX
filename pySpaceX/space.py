"""
Program: A www.spacexdata.com API Wrapper
Author: TwoSails
Description: A simple python API Wrapper made for use with the www.spacexdata.com
Version: 1.0.0
"""
import requests
from .methods.capsule import Capsule
from .methods.cores import Cores
from .methods.dragons import Dragons
from .methods.history import History
from .methods.landing import Landing
from .methods.launches import Launches
from .methods.launchpad import Launchpad
from .methods.missions import Missions
from .methods.payloads import Payload
from .methods.roadster import Roadster
from .methods.rockets import Rockets
from .methods.ships import Ships
from .methods.info import Info

__version__ = '1.0.0'


class Space:
    """
    Represents SpaceAPI object with general methods
    """

    def __init__(self):
        self.APIver = 'v3'
        self.url = f'https://api.spacexdata.com/{self.APIver}'

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

    def get_history(self):
        """Gets information about SpaceX historical events

        Returns:
            History: History Object
        """
        return History(self.url)

    def get_landing_pads(self):
        """Gets information about SpaceX landing pads

        Returns:
            Landing: Landing Object
        """
        return Landing(self.url)

    def get_launches(self):
        """Gets information about SpaceX launches

        Returns:
            Launches: Launches Object
        """
        return Launches(self.url)

    def get_launchpad(self):
        """Gets information about SpaceX launchpad

        Returns:
            Launchpad: Launchpad Object
        """
        return Launchpad(self.url)

    def get_missions(self):
        """Gets information about SpaceX missions

        Returns:
            Missions: Missions Object
        """
        return Missions(self.url)

    def get_payloads(self):
        """Gets information about SpaceX payloads

        Returns:
            Payload: Payload Object
        """
        return Payload(self.url)

    def get_rockets(self):
        """Gets information about SpaceX rockets

        Returns:
            Rockets: Rockets Object
        """
        return Rockets(self.url)

    def get_roadster(self):
        """Gets information about SpaceX roadster

        Returns:
            Roadster: Roadster Object
        """
        return Roadster(self.url)

    def get_ships(self):
        """Gets information about SpaceX ships

        Returns:
            Ships: Ships Object
        """
        return Ships(self.url)

    def get_info(self):
        """Gets information about SpaceX and the api

        Returns:
            Info: Info Object
        """
        return Info(self.url)




