from pySpaceX import space

api = space.Space()

capsule = api.get_capsule()

print(capsule.one_capsule('C103'))

