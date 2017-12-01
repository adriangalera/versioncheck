"""Setup.py"""
from setuptools import setup, find_packages

name = "versioncheck"
version = "0.0.1"
author = "Adrian Galera"
author_email = "agalera@sensefields.com"
description = "Tool to check the current version reported in tagged commit vs the " \
              "version in the project"
license = "Private"
keywords = "devops versioning"
url = ""
packages = find_packages()
classifiers = [
    "Development Status :: 1 - Planning",
    "Development Status :: 2 - Pre-Alpha",
    "Development Status :: 3 - Alpha",
    "Development Status :: 4 - Beta",
    # "Development Status :: 5 - Production/Stable",
    # "Development Status :: 6 - Mature",
    # "Development Status :: 7 - Inactive"
]
dependencies = []
test_dependencies = []
setup(name=name
      , version=version
      , author=author
      , author_email=author_email
      , description=description
      , license=license
      , keywords=keywords
      , url=url, packages=packages
      , long_description=description
      , classifiers=classifiers
      , install_requires=dependencies
      , extras_require={"test": test_dependencies}
      )
