import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toornament.py", # Replace with your own username
    version="0.0.0",
    author="niborus",
    author_email="niborus.management@gmail.com",
    description="An Connector to the API of toornament.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niborus/toornament",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning"
    ],
    python_requires='>=3.6',
)
