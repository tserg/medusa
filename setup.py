from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


extras_require = {
    "test": ["pytest>=7.2.0"],
    "lint": ["black==22.12.0", "flake8==6.0.0", "isort==5.11.4", "mypy==0.991"],
    "dev": ["pre-commit"],
}

extras_require["dev"] = extras_require["test"] + extras_require["lint"] + extras_require["dev"]

setup(
    name="medusa",
    version="0.1.0",
    description="Experimental Vyper code analyzer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gary Tse",
    author_email="",
    url="https://github.com/tserg/medusa",
    keywords=["ethereum", "vyper", "analyzer"],
    python_requires=">=3.10,<3.12",
    packages=find_packages(where=".", include=["medusa*"]),
    install_requires=["vyper==0.3.9"],
    extras_require=extras_require,
    entry_points={"console_scripts": ["medusa=medusa._cli.__main__:main"]},
)
