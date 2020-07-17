from setuptools import setup


LONG_DESC = "Spacin is a word-separator that \
 distinguishes each word in a given string."

setup(
    name="spacin",
    version="0.1.0",
    description="Spacin, puts space between!",
    long_description=LONG_DESC,
    long_description_content_type="text/plain",
    author="Mohammad Salek",
    url="https://gitlab.com/mohammadsalek/spacin",
    license="MIT",
    include_package_data=True,
    packages=["spacin", "data", ],
    entry_points={"console_scripts": ["spacin = spacin.__main__:main"]},
)
