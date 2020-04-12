import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quadratic_equation_jparve_pkg",
    version="0.0.4",
    author="Jan Joonas Parve",
    author_email="jparve@taltech.ee",
    description="Module for quadratic equation solving",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Parvetaja/quadratic_equation_jparve_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
