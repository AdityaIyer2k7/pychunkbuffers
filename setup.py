import setuptools
import sys

_, version, url, *_ = sys.argv
print(version, url)
with open("README.md") as fl: ldesc = fl.read()
setuptools.setup(
    name="pychunkbuffers",
    version=version,
    author="AdityaIyer2k7",
    author_email="adityaiyer2007@gmail.com",
    description="An open-source python library for writing large amounts of data to buffers via chunks.",
    long_description=ldesc,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
    keywords=[
        "python 3",
        "threading",
        "thread",
        "chunking",
        "buffers",
        "pychunk",
        "pybuffer"
    ],
    python_requires='>=3.6'
)