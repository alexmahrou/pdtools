import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdtools", # Replace with your own username
    version="0.0.1",
    author="Alex Mahrou",
    author_email="alexmahrou@gmail.com",
    description="Some useful pandas tools for ETL Processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexmahrou/pdtools",
    packages=setuptools.find_packages(include=['re','pandas']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pandas'],
)