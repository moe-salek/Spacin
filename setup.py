from setuptools import setup

setup(
    name='spacin',
    version='0.1.0',
    description='Spacin, puts space between!',
    long_description='Spacin is a word-separator that distinguishes each word in a given string.',
    long_description_content_type="text/markdown",
    author='Mohammad Salek',
    url='https://gitlab.com/mohammadsalek/spacin',
    license="MIT",
    include_package_data=True,
    packages=['spacin', 'data'],
    entry_points={'console_scripts': ['spacin = spacin.__main__:main']},
)
