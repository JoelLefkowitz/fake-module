# Mock file tree

Globally replace a module with a configurable fake.

## Status

| Source     | Shields                                                                                                                                       |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Project    | ![release][release_shield] ![license][license_shield] ![lines][lines_shield] ![languages][languages_shield]                                   |
| Health     | ![codacy][codacy_shield] ![readthedocs][readthedocs_shield] ![github_review][github_review_shield] ![codacy_coverage][codacy_coverage_shield] |
| Repository | ![issues][issues_shield] ![issues_closed][issues_closed_shield] ![pulls][pulls_shield] ![pulls_closed][pulls_closed_shield]                   |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]                                      |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield]                            |

## Installing

```bash
pip install fake-module
```

## Usage

You can purge all of a module's members inside a context manager:

```python
from fake_module import FakeModule

with FakeModule("colorsys"):
     colorsys.rgb_to_hls()
     
... AttributeError
```

Or create a fake globally:

```python
import colorsys
from fake_module import FakeModule

fake = FakeModule("colorsys")
fake.purge()
setattr(fake, "rgb_to_hls", 1)

colorsys.rgb_to_hls

1
```

## Tests

To run unit tests and generate a coverage report:

```bash
grunt test
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

## Continuous integration

This repository uses github actions to lint and test each commit. Formatting tasks and writing/generating documentation must be done before committing new code.

## Versioning

This repository adheres to semantic versioning standards.
For more information on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][author]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Public links -->

[semver]: http://semver.org/

<!-- External links -->

[readthedocs]: https://fake-module.readthedocs.io/en/latest/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->

[author]: https://github.com/joellefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/fake-module
[license_shield]: https://img.shields.io/github/license/joellefkowitz/fake-module
[lines_shield]: https://img.shields.io/tokei/lines/github/joellefkowitz/fake-module
[languages_shield]: https://img.shields.io/github/languages/count/joellefkowitz/fake-module

<!-- Health shields -->

[codacy_shield]: https://img.shields.io/codacy/grade/5656c08e1ca94f6da488d73fd99f1dcf
[readthedocs_shield]: https://img.shields.io/readthedocs/fake-module
[github_review_shield]: https://img.shields.io/github/workflow/status/joellefkowitz/fake-module/Review
[codacy_coverage_shield]: https://img.shields.io/codacy/coverage/5656c08e1ca94f6da488d73fd99f1dcf

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/fake-module
[issues_closed_shield]: https://img.shields.io/github/issues-closed/joellefkowitz/fake-module
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/fake-module
[pulls_closed_shield]: https://img.shields.io/github/issues-pr-closed/joellefkowitz/fake-module

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/fake-module
[python_versions_shield]: https://img.shields.io/pypi/pyversions/fake-module
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/fake-module

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/fake-module
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/fake-module
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/fake-module
