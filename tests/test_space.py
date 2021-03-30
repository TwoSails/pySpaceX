from pySpaceX import space

api = space.Space()

roadster = api.get_roadster()

print(roadster.missions())

