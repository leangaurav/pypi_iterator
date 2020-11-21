import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leangaurav",
    version="0.0.1",
    author="leangaurav",
    author_email="leangaurav.me@gmail.com",
    description="Iterator utility classes and functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leangaurav/pypi_iterator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
)