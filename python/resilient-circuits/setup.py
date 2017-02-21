#
from __future__ import print_function
from setuptools import setup, find_packages
import io
import codecs
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README')

setup(
    name='resilient_circuits',
    version="27.1.0",  # __version__ in __init__.py
    url='https://www.resilientsystems.com/',
    license='IBM Resilient License',

    author='IBM Resilient',
    install_requires=[
        'stomp.py>=4.0.12',
        'requests>=2.6.0',
        'circuits',
        'pytz',
        'jinja2',
        'filelock>=2.0.5'
    ],
    extras_require={
        ':python_version >= "2.7"': [
            'keyring'
        ],
        ':python_version == "2.6"': [
            'keyring==5.4'
        ]
    },
    author_email='support@resilientsystems.com',
    description='Resilient Circuits Framework for Custom Apps',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    data_files = [("", ["resilient_circuits/LICENSE"]),
                  ("", ["resilient_circuits/data/app.config.base"])],
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    scripts=['bin/res-action-test',
             'bin/resilient-circuits']
)
