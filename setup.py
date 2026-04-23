#!/usr/bin/env python
"""Setup script for Time Travel v1.3"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="time-travel-v1.3",
    version="1.3.0",
    author="Sander Klausen",
    description="A surreal dream brought to life. A time travel interface application.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanderklausen/time-travel-v1.3",
    py_modules=["timetravel"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Pillow>=9.0.0",
    ],
    extras_require={
        "dev": ["pytest", "black", "flake8"],
    },
    entry_points={
        "console_scripts": [
            "timetravel=timetravel:main",
        ],
    },
)
