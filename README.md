<p align="center">
<a href="https://gitlab.com/dkreeft/pycasino">
<img align="center" src="https://gitlab.com/dkreeft/zoek/-/raw/master/logo.png" width="174" height="170" />
</a>
</p>

# zoek - find files and directories
<p align="center">
<a href="https://gitlab.com/dkreeft/zoek/"><img src="https://gitlab.com/dkreeft/zoek/badges/master/pipeline.svg?style=flat alt="pipeline status"></a>
<a href="https://gitlab.com/dkreeft/zoek/"><img src="https://gitlab.com/dkreeft/zoek/badges/master/coverage.svg?style=flat" alt="code coverage"></a>
</p>

zoek (Dutch for "search") is a Python library and command-line utility aiming to duplicate and extend the functionality of the find command-line utility.

## Installation

[pip](https://pip.pypa.io/en/stable/) can be used to install zoek:

```bash
pip install zoek
```

However, we recommend to install zoek using [pipx](https://github.com/pipxproject/pipx):

```bash
pipx install zoek
```

## Usage

zoek can be used as a command-line utility as follows:

```bash
zoek <dir>
```

zoek currently supports the following flags:

* `--depth` or `-d` to indicate the depth of directories and files to return (default: 1):
```bash
zoek <dir> -d <int>
```

* `--startswith` or `-s` to return files and directories starting with the provided string:
```bash
zoek <dir> -s <str>
```

* `--contains` or `-c` to return files and directories that contain the provided string:
```bash
zoek <dir> -c <str>
```

* `--minsize` or `-m` to filter output on size, a positive int returns files equal or larger, a negative int returns files smaller than input:
```bash
zoek <dir> -m <int>
```

* `--datecreated` or `-dc` to filter output on time created, a positive int returns files created more than int minutes ago, a negative int return files less than int minutes ago:
```bash
zoek <dir> -dc <int>
```

* `--datemodified` or `-dm` similar to `--datecreated`, but then for filtering date modified:
```bash
zoek <dir> -dc <int>
```

As filters stack, multiple flags can be used simultaneously.

## Contributing
Please refer to [CONTRIBUTING.md](https://gitlab.com/dkreeft/zoek/-/blob/master/CONTRIBUTING.md)

## License
[BSD-3](https://gitlab.com/dkreeft/zoek/-/blob/master/LICENSE)

