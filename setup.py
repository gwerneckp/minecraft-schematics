from setuptools import setup, find_packages

NAME = "minecraftschematics"
VERSION = "0.1.1"
DESCRIPTION = "A library for working with Minecraft Schematics in Python with numpy"
with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name=NAME,
    packages=find_packages(include=["minecraftschematics"]),
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Gabriel Werneck Paiva",
    author_email="gwerneckpaiva@gmail.com",
    license="MIT",
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
    install_requires=[
        'numpy',
        'nbtlib',
    ],
    keywords=['python', 'minecraft', 'schematic', 'numpy', 'nbtlib'],
)
