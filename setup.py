try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'name': 'Repeated Text Scanner',
	'version': '0.1',
	'url': 'https://github.com/parnellj/repeated_text_scanner',
	'download_url': 'https://github.com/parnellj/repeated_text_scanner',
	'author': 'Justin Parnell',
	'author_email': 'parnell.justin@gmail.com',
	'maintainer': 'Justin Parnell',
	'maintainer_email': 'parnell.justin@gmail.com',
	'classifiers': [],
	'license': 'GNU GPL v3.0',
	'description': 'Searches a given plaintext document for repeated n-length sequences of words.',
	'long_description': 'Searches a given plaintext document for repeated n-length sequences of words.',
	'keywords': '',
	'install_requires': ['nose'],
	'packages': ['repeated_text_scanner'],
	'scripts': []
}
	
setup(**config)
