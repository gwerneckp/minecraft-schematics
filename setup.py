from setuptools import setup, find_packages

setup(
    name="pyschematic",
    packages=find_packages(include=["pyschematic"]),
    version="0.1.0",
    description="A library for working with Minecraft Schematics in Python with numpy",
    author="Gabriel Werneck Paiva",
    license="MIT",
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
    install_requires=[
        'numpy',
        'nbtlib',
    ],
)
