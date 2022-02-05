<h1 align="center">
    PySpaceX
</h1>
<hr>
<h3 align="center">
  Easily access SpaceX's API
</h3>
<p align="center">
  pySpaceX is an open-source API wrapper to make it easier to access data from the unofficial <a href="https://github.com/r-spacex/SpaceX-API">v4 SpaceX API</a> 
</p>

<p align="center">
  <a href="https://pypi.org/project/pySpaceX/">
    <img alt="GitHub all releases" src="https://pepy.tech/badge/pyspacex">
  </a>
  <a href="https://github.com/TwoSails/pySpaceX/releases">
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/TwoSails/pySpaceX">
  </a>
</p>

<h3 align="center">
  <a href="https://pySpaceX.readthedocs.org">Docs</a>
  <span> · </span>
  <a href="https://github.com/TwoSails/pySpaceX/issues">Report a bug</a>
  <span> · </span>
  <a href="https://pypi.org/project/pySpaceX/">PyPi</a>
</h3>

<hr>

## Installation

To install you can simply install the package by using:
`python3 -m pip install pySpaceX`

The code can also be directly downloaded from the latest release:

https://github.com/TwoSails/pySpaceX/releases 

## Usage
To get started with using this wrapper we need to start with the creation of an api instance:
```python
from pySpaceX import Space

api = Space()
```

To get information about the API use:
```python
info = api.get_info()  # Returns the info object

print(info.company())  # Returns data about the SpaceX company
```
You can also get information about a dragon capsule by using:
```python
dragon = api.get_dragon()  # Returns the dragon object

print(dragon.one_dragon('5e9d058859b1ffd8e2ad5f90'))
```

## Documentation
Available at https://pypi.org/project/pySpaceX

## Contributing
Feel free to contribute by opening an [issue](https://github.com/TwoSails/pySpaceX/issues) or a [pull request](https://github.com/TwoSails/pySpaceX/pulls).

Any help is greatly appreciated.

All contributors will be listed on this repository.
