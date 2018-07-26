import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

requires = [
    "requests"
]

packages = [
    "bpl_api"
]

setuptools.setup(
    name="bpl-api",
    version="0.0.1",
    author="Alistair O'Brien",
    author_email="alistair.o'brien@ellesmere.com",
    description="An API for the Blockpool Blockchain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DuneRoot/bpl-api",
    packages=packages,
    install_requires=requires
)
