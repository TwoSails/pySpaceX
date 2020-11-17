"""
Program: A www.spacexdata.com API Wrapper
Author: TwoSails
Description: A simple python API Wrapper made for use with the www.spacexdata.com
Version: 1.0.1
"""

import requests
from pySpaceX.methods.capsule import Capsule
from pySpaceX.methods.cores import Cores
from pySpaceX.methods.dragons import Dragons
from pySpaceX.methods.history import History
from pySpaceX.methods.landing import Landing
from pySpaceX.methods.launches import Launches
from pySpaceX.methods.launchpad import Launchpad
from pySpaceX.methods.missions import Missions
from pySpaceX.methods.payloads import Payload
from pySpaceX.methods.roadster import Roadster
from pySpaceX.methods.rockets import Rockets
from pySpaceX.methods.ships import Ships
from pySpaceX.methods.info import Info


class Space:
    """
    Represents SpaceAPI object with general methods
    """

    __version__ = '1.0.1'

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




