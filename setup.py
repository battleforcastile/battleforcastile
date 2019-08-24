import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class NoseTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import nose
        errcode = nose.main(self.test_args)
        sys.exit(errcode)


setup(name='battleforcastile',
      version='0.0.2',
      description='Play a fantasy cards game on your terminal',
      maintainer='José Vidal',
      maintainer_email='contact@josevidal.me',
      author='José Vidal',
      author_email='contact@josevidal.me',
      url='https://github.com/battleforcastile/battleforcastile',
      license='MIT',
      long_description=open('README.md').read(),
      platforms='any',
      keywords=[
          'fantasy',
          'game',
      ],
      packages=find_packages(),
      install_requires=[
          'click==7.0'
      ],
      entry_points={
          "console_scripts": [
              "battleforcastile = battleforcastile.main:cli",
          ],
      },
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: OS Independent'
      ],
      tests_require=['nose'],
      cmdclass={'test': NoseTest}
      )