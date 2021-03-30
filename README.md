# pySpaceX
This is an unofficial Python3 [SpaceX API](https://docs.spacexdata.com) wrapper

## Installation
Currently unavailable on PyPi

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
info = api.get_info() # Returns the info object

print(info.get_api())
```
You can also get information about a dragon capsule by using:
```python
dragon = api.get_dragon() # Returns the dragon object

print(dragon.one_dragon('C112'))
```

## Documentation
To come in a later commit.

## Contributing
Feel free to contribute by opening an [issue](https://github.com/TwoSails/pySpaceX/issues) or a [pull request](https://github.com/TwoSails/pySpaceX/pulls).

Any help is greatly appreciated.

All contributors will be listed on this repository.