# Fake module

Globally replace a module with a configurable fake.

![Review](https://img.shields.io/github/actions/workflow/status/JoelLefkowitz/fake-module/review.yml)
![Version](https://img.shields.io/pypi/v/fake-module)
![Downloads](https://img.shields.io/pypi/dw/fake-module)
![Quality](https://img.shields.io/codacy/grade/5656c08e1ca94f6da488d73fd99f1dcf)
![Coverage](https://img.shields.io/codacy/coverage/5656c08e1ca94f6da488d73fd99f1dcf)

## Installation

```bash
pip install fake-module
```

## Documentation

Documentation and more detailed examples are hosted on [Github Pages](https://joellefkowitz.github.io/fake-module).

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

## Tooling

### Dependencies

To install dependencies:

```bash
yarn install
pip install .[all]
```

### Tests

To run tests:

```bash
thx test
```

### Documentation

To generate the documentation locally:

```bash
thx docs
```

### Linters

To run linters:

```bash
thx lint
```

### Formatters

To run formatters:

```bash
thx format
```

## Contributing

Please read this repository's [Code of Conduct](CODE_OF_CONDUCT.md) which outlines our collaboration standards and the [Changelog](CHANGELOG.md) for details on breaking changes that have been made.

This repository adheres to semantic versioning standards. For more information on semantic versioning visit [SemVer](https://semver.org).

Bump2version is used to version and tag changes. For example:

```bash
bump2version patch
```

### Contributors

- [Joel Lefkowitz](https://github.com/joellefkowitz) - Initial work

## Remarks

Lots of love to the open source community!

<div align='center'>
    <img width=200 height=200 src='https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif' alt='Be kind to your mind' />
    <img width=200 height=200 src='https://media.giphy.com/media/KEAAbQ5clGWJwuJuZB/giphy.gif' alt='Love each other' />
    <img width=200 height=200 src='https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif' alt="It's ok to have a bad day" />
</div>
