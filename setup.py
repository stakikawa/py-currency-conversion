import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyCurrencyConversion",
    version="1.0.0",
    author="Suzuran Takikawa",
    author_email="suzuran.takikawa@gmail.com",
    description="A small Python currency conversion library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stakikawa/PyCurrencyConversion",
    packages=setuptools.find_packages(exclude=['test', 'test.*']),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)