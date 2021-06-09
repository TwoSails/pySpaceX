"""
Program: A www.spacexdata.com API Wrapper
Author: TwoSails
Description: A simple python API Wrapper made for use with the www.spacexdata.com
Version: 1.0.1
"""

import requests
from pySpaceX.methods.capsule import Capsule
from pySpaceX.methods.crew import Crew
from pySpaceX.methods.cores import Cores
from pySpaceX.methods.dragons import Dragons
from pySpaceX.methods.history import History
from pySpaceX.methods.landing import Landing
from pySpaceX.methods.launches import Launches
from pySpaceX.methods.launchpad import Launchpad
from pySpaceX.methods.missions import Missions
from pySpaceX.methods.payloads import Payloads
from pySpaceX.methods.fairings import Fairings
from pySpaceX.methods.roadster import Roadster
from pySpaceX.methods.rockets import Rockets
from pySpaceX.methods.ships import Ships
from pySpaceX.methods.starlink import Starlink
from pySpaceX.methods.info import Info


class Space:
    """
    Represents SpaceAPI object with general methods
    """

    __version__ = '1.2.0'

    def __init__(self):
        self.APIver = 'v4'
        self.url = f'https://api.spacexdata.com/{self.APIver}'

    def _get_data(self, params):
        """
        Executes HTTP request with base url and given endpoints

        Args:
            params: dictionary
        Returns:
             response: JSON data
        """
        response = requests.get(self.url, params=params).json()

        return response

    def get_capsule(self) -> Capsule:
        """
        Gets information about SpaceX capsules

        :return: Capsule object
        """
        return Capsule(self.url)

    def get_crew(self) -> Crew:
        """
        Gets information about SpaceX crew members

        :return: Crew Object
        """
        return Crew(self.url)

    def get_core(self) -> Cores:
        """
        Gets information about SpaceX core stages

        :return: Cores Object
        """
        return Cores(self.url)

    def get_dragon(self) -> Dragons:
        """
        Gets information about SpaceX dragon capsules

        :return: Dragons Object
        """
        return Dragons(self.url)

    def get_history(self) -> History:
        """
        Gets information about SpaceX historical events

        :return: History Object
        """
        return History(self.url)

    def get_landing_pads(self) -> Landing:
        """
        Gets information about SpaceX landing pads

        :return: Landing Object
        """
        return Landing(self.url)

    def get_launches(self) -> Launches:
        """
        Gets information about SpaceX launches

        :return: Launches Object
        """
        return Launches(self.url)

    def get_launchpad(self) -> Launchpad:
        """
        Gets information about SpaceX launchpad

        :return: Launchpad Object
        """
        return Launchpad(self.url)

    def get_missions(self) -> Missions:
        """
        Gets information about SpaceX missions

        :return: Missions Object
        """
        return Missions(self.url)

    def get_payloads(self) -> Payloads:
        """
        Gets information about SpaceX payloads

        :return: Payloads Object
        """
        return Payloads(self.url)

    def get_fairings(self) -> Fairings:
        """
        Gets information about SpaceX fairings

        :return: Fairings Object
        """
        return Fairings(self.url)

    def get_rockets(self) -> Rockets:
        """
        Gets information about SpaceX rockets

        :return: Rockets Object
        """
        return Rockets(self.url)

    def get_roadster(self) -> Roadster:
        """
        Gets information about SpaceX roadster

        :return: Roadster Object
        """
        return Roadster(self.url)

    def get_ships(self) -> Ships:
        """
        Gets information about SpaceX ships

        :return: Ships Object
        """
        return Ships(self.url)

    def get_starlink(self) -> Starlink:
        """
        Gets information about SpaceX Starlink sats

        :return: Starlink Object
        """
        return Starlink(self.url)

    def get_info(self) -> Info:
        """
        Gets information about SpaceX and the API

        :return: Info Object
        """
        return Info(self.url)
