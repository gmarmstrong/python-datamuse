from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="python-datamuse",
    version="1.2.1",
    keywords="datamuse, linguistics, language, wrapper",
    packages=["datamuse"],
    url="https://github.com/gmarmstrong/python-datamuse",
    license="MIT",
    author="Guthrie McAfee Armstrong",
    author_email="guthrie.armstrong@gmail.com",
    description="Python wrapper for the Datamuse API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
        ],
    install_requires=[
        "requests"
        ]
)
