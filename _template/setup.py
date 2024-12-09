try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Мой проект',
        'author': 'Evgeny Shashkov',
        'url': 'URL-address',
        'download_url': 'download_url',
        'author_email': 'shashkow@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname',
}

setup(**config)

