.. pySpaceX documentation master file, created by
   sphinx-quickstart on Tue Jun  8 23:24:27 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pySpaceX's documentation!
====================================

Github: https://github.com/TwoSails/pySpaceX

PyPi: https://pypi.org/project/pySpaceX/


This is an unofficial Python3 `SpaceX API <https://docs.spacexdata.com>`_ wrapper

Installation
------------

To install you can simply install the package by using:

.. code-block:: bash

   python3 -m pip install pySpaceX

The code can also be directly downloaded from the latest release:

https://github.com/TwoSails/pySpaceX/releases

Usage
-----
To get started with using this wrapper we need to start with the creation of an api instance:

.. code-block:: python

   from pySpaceX import Space

   api = Space()

To get information about the API use:

.. code-block:: python
   info = api.get_info()  # Returns the info object

   print(info.company())  # Returns data about the SpaceX company

You can also get information about a dragon capsule by using:

.. code-block:: python

   dragon = api.get_dragon() # Returns the dragon object

   print(dragon.one_dragon('5e9d058859b1ffd8e2ad5f90'))

Contributing
------------
Feel free to contribute by opening an `issue <https://github.com/TwoSails/pySpaceX/issues>`_ or a `pull request <https://github.com/TwoSails/pySpaceX/pulls>`_.

Any help is greatly appreciated.

All contributors will be listed on this repository.


Guide
^^^^^

.. toctree::
   :maxdepth: 2

   pySpaceX
   pySpaceX.methods


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
