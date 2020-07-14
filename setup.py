from setuptools import setup

setup(
    name='spacin',
    description='puts space in!',
    version='0.1',
    author='Mohammad Salek',
    url='https://gitlab.com/mohammadsalek/spacin',
    packages=['spacin'],
    entry_points={'console_scripts': ['spacin = spacin.__main__:main']},
)
