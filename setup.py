#!/usr/bin/env python3
"""
Setup script for Crop Recommendation System
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("crop_app3/requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="crop-recommendation-system",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A machine learning-based crop recommendation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/crop-recommendation-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "crop-recommendation=run:main",
        ],
    },
    include_package_data=True,
    package_data={
        "crop_app3": [
            "templates/*.html",
            "static/images/*.jpg",
            "static/style/*.css",
            "crop_app",
        ],
    },
    keywords="machine-learning, agriculture, crop-recommendation, flask, python",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/crop-recommendation-system/issues",
        "Source": "https://github.com/yourusername/crop-recommendation-system",
        "Documentation": "https://github.com/yourusername/crop-recommendation-system#readme",
    },
) 