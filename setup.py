from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

version = '0.0.1'


class PyTest(TestCommand):

    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        # pylint: disable=W0201
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

# put all install requirements into this list:
requires = [
    'matplotlib',
]

setup(name='probe-plotting2',
      version=version,
      scripts=[],
      description='Helper functions to deal with matplotlib.',
      long_description='',
      classifiers=[],
      keywords='',
      author='Petr Zikan',
      author_email='zikan.p@gmail.com',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=requires,
      entry_points='''
        # -*- Entry points: -*-
      ''',
      tests_require=['pytest'],
      cmdclass={'test': PyTest}
      )
