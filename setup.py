from functools import reduce
from typing import Any, Dict, List, cast

from setuptools import setup

configuration = {
    "packages": ["fake_module"],
    "package_dir": {"fake_module": "src"},
    "install_requires": [
        "dataclasses",
        "types-dataclasses",
    ],
    "extras_require": {
        "linters": [
            "mypy",
            "pylint",
            "bandit",
        ],
        "formatters": [
            "autoflake",
            "black",
            "isort",
        ],
        "tests": [
            "tox",
            "pytest-mocha",
            "pytest-sugar",
            "pytest",
            "coverage",
        ],
        "docs": ["quickdocs"],
        "publishers": [
            "twine",
            "wheel",
            "bump2version",
        ],
    },
}

if __name__ == "__main__":
    extras_require = cast(Dict[Any, List[Any]], configuration["extras_require"])

    merge_lists = lambda acc, x: list(set(acc) | (set(x)))

    configuration["extras_require"] = dict(
        **extras_require, **{"all": reduce(merge_lists, extras_require.values())}
    )

    setup(**configuration)
