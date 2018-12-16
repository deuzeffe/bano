from pathlib import Path
from setuptools import setup, find_packages

VERSION = (2, 0, 0, 'alpha')

setup(
    name='bano',
    version=".".join(map(str, VERSION)),
    description='BANO...',
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    url="https://github.com/osm-fr/bano",
    author='VdCT',
    author_email="vdct@laposte.net",
    license='WTFPL',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='open data, OSM, geoloc',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': ['bano=bano.bin:main'],
},)
