from setuptools import setup, find_packages

setup(
    name="data_structures",
    version="0.1.0",
    description="Custom data structure implementations for CS 333",
    author="Stolan Belikove",
    author_email="sbelikove@unr.edu",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)