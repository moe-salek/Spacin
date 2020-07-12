from setuptools import setup

setup(name='Spacin',
      version='0.1',
      packages=['spacin'],
      entry_points={
          'console_scripts': [
              'spacin = spacin.__main__:main'
          ]
      },
      )
