import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='pySpaceX',
    author='TwoSails',
    version='1.0.1',
    description='An unofficial python3 SpaceX API wrapper',
    long_description=long_description,
    packages=setuptools.find_packages(),
    long_description_content_type='text/markdown',
    url='https://github.com/TwoSails/pySpaceX',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3) ",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    requires=['requests']
)