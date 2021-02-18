import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyCMLutil-Hossein_pypi", # Replace with your own username
    version="0.0.1",
    author="Hossein Sharifi",
    author_email="hossein.sharifi@uky.edu",
    description="A usefule python package for creating sientific figures ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Campbell-Muscle-Lab/PyCMLutilities",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
