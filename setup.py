import io

from setuptools import setup

setup(
    name="dynamic-function-loader",
    version="0.0.2",
    description="Dynamically loads a function from code represented as a string.",
    author="Joseph Wortmann",
    author_email="jwortmann@quinovas.com",
    url="https://github.com/QuiNovas/dynamic-function-loader",
    license="Apache 2.0",
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=["dynamic_function_loader"],
    package_dir={"dynamic_function_loader": "src/dynamic_function_loader"},
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
    ],
)
