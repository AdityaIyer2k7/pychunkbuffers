import setuptools

with open("README.md") as fl: ldesc = fl.read()
setuptools.setup(
    name="pychunkbuffers",
    version="1.0.3",
    author="AdityaIyer2k7",
    author_email="adityaiyer2007@gmail.com",
    description="An open-source python library for writing large amounts of data to buffers via chunks",
    long_description=ldesc,
    long_description_content_type="text/markdown",
    url="https://github.com/AdityaIyer2k7/pychunkbuffers",
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
