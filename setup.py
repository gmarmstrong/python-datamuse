from setuptools import setup

setup(
    name="python-datamuse",
    version="1.1.0",
    keywords="datamuse, linguistics, language, wrapper",
    packages=["datamuse"],
    url="https://github.com/gmarmstrong/python-datamuse",
    license="MIT",
    author="Guthrie McAfee Armstrong",
    author_email="guthrie.armstrong@gmail.com",
    description="Python wrapper for the Datamuse API",
    long_description="Fork of Margaret Sy's Python wrapper for the Datamuse API",
    python_requires=">=3",
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
