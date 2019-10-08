import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy_pymongo",
    version="0.0.1",
    author="Mingjie Ye",
    author_email="yemj1017@gmail.com",
    description="A package for interaction with data in mongodb. Assignment 1 of Big Data Platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Matthew-Ye/easy_pymongo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)