from setuptools import setup

setup(
    name = "webcount",
    version = "0.1",
    license = "BSD",
    packages=['webcount', 'test'],
    install_requires=['requests'],
)
