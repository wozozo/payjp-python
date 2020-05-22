import sys

from setuptools import setup

install_requires = []

if sys.version_info < (3, 6):
    raise DeprecationWarning('Python 3.5 and older are no longer supported by PAY.JP. ')

install_requires.append('requests >= 2.7.0, < 3.0.0')

setup(
    name="payjp",
    version="2.0.0",
    description='PAY.JP python bindings',
    author="PAY.JP",
    author_email='support@pay.jp',
    packages=['payjp', 'payjp.test'],
    url='https://github.com/wozozo/payjp-python',
    install_requires=install_requires,
    tests_require=[
        'mock >= 1.3.0'
    ],
    test_suite='payjp.test.all',
)
