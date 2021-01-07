import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="etsy-scraper-pkg-dahmer96",
    version="0.0.1",
    author="Dominic Fournier",
    author_email="me@dominicfournier.com",
    description="Retrieves info from Etsy using UrlLib and Beautiful Soup and returns the data in JSON.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dahmer-Open/etsy-scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "beautifulsoup4===4.9.3"
    ]
    python_requires='>=3.6',
)