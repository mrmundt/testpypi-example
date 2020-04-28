import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TestPyPi-Sample-Package-mmundt",
    version="0.0.1",
    author="Miranda Mundt",
    author_email="mmundt@sandia.gov",
    description="A small example package for uploading to TestPyPi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrmundt/testpypi-example",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)

