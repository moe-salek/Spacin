from setuptools import setup

setup(
    name='spacin',
    version='0.1',
    description='puts space in!',
    author='Mohammad Salek',
    url='https://gitlab.com/mohammadsalek/spacin',
    packages=['spacin'],
    entry_points={'console_scripts': ['spacin = spacin.__main__:main']},
)
