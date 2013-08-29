try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

import sys

class TestCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        '''
        Finds all the tests modules in tests/, and runs them.
        '''
        from mykaze import tests
        import unittest
        unittest.main(tests, argv=sys.argv[:1])

version_tuple = __import__('mykaze').VERSION

if version_tuple[2] is not None:
    version = "%d.%d_%s" % version_tuple
else:
    version = "%d.%d" % version_tuple[:2]

setup(
    name = "MyKaze",
    version = version,
    url = 'https://github.com/methane/MyKaze/',
    author = 'yutaka.matsubara',
    author_email = 'yutaka.matsubara@gmail.com',
    maintainer = 'INADA Naoki',
    maintainer_email = 'songofacandy@gmail.com',
    description = 'Pure Python MySQL Driver for Torando',
    license = "MIT",
    packages = ['mykaze', 'mykaze.constants', 'mykaze.tests'],
    cmdclass = {'test': TestCommand},
)
