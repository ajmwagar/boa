from setuptools import setup
setup(
    name = 'cobra',
    version = '0.1.0',
    packages = ['cobra'],
    entry_points = {
        'console_scripts': [
            'cobra = cobra.__main__:main'
        ]
    })
