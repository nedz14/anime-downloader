#!/usr/bin/env python3

from setuptools import setup, find_packages
import re
import io

with open('README.md', 'r') as f:
    long_description = f.read()

with io.open('anime_downloader/__version__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


setup(
    name='anime-downloader',
    version=version,
    author='Vishnunarayan K.I.',
    author_email='vishnunarayan6105@gmail.com',
    description='Download your favourite anime',
    packages=find_packages(),
    url='https://github.com/vn-ki/anime-downloader',
    keywords=['anime', 'downloader', '9anime', 'download', 'kissanime'],
    install_requires=[
        'beautifulsoup4>=4.6.0',
        'requests>=2.18.4',
        'Click>=6.7',
        'fuzzywuzzy>=0.16.0',
    ],
    tests_require=[
        'pytest',
    ],
    extras_require={
        'cloudflare': ['cfscrape>=1.9.5']
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points='''
        [console_scripts]
        anime=anime_downloader.cli:cli
    '''
)
