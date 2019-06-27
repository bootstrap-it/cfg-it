from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

# REQUIREMENTS=open("requirements.txt").read().splitlines()

setup(
    name="cfg_it",

    packages=find_packages("src", exclude=("tests",)),
    package_dir={"": "src"},

    version="0.0.1",
    description="Config module insiper by 'spring boot'",
    author="Mikalai Davydzenka",
    author_email="mikalai.davydzenka@gmail.com",
    # url="",
    # download_url="",
    long_description=readme,
    long_description_content_type="text/markdown; charset=UTF-8",
    install_requires=[
        "pyyaml",
    ],
    license="MIT license",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)