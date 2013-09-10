
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'MVX-2013-Emkt-Scaffolds',
    'author': 'Jonas Trevisan',
    'url': 'https://github.com/mobvox/MVX-2013-Emkt-Scaffolds',
    'download_url': 'git@github.com:mobvox/MVX-2013-Emkt-Scaffolds.git',
    'author_email': 'jonas@mobvox.com.br',
    'version': '0.1',
    'install_requires': ['nose','argparse'],
    'packages': ['MVX2013EmktScaffolds'],
    'scripts': [],
    'name': 'MVX2013EmktScaffolds',
    'entry_points': {
        'console_scripts': [
            'emktscaffold = MVX2013EmktScaffolds.__main__:main'
        ]
    }
}

setup(**config)
