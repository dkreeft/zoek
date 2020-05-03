<p align="center">
<a href="https://gitlab.com/dkreeft/zoek">
<img align="center" src="https://gitlab.com/dkreeft/zoek/-/raw/master/logo.png"/>
</a>
</p>

# zoek - find files and directories

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
pyfind <dir>
```

zoek currently supports the following flags:

* `--depth` or `-d` to indicate the depth of directories and files to return (default: 1):
```bash
pyfind <dir> -d <int>
```

* `--startswith` or `-s` to return files and directories starting with the provided string:
```bash
pyfind <dir> -s <str>
```

* `--contains` or `-c` to return files and directories that contain the provided string:
```bash
pyfind <dir> -c <str>
```

* `--minsize` or `-m` to filter output on size, a positive int returns files equal or larger, a negative int returns files smaller than input:
```bash
pyfind <dir> -m <int>
```

* `--datecreated` or `-dc` to filter output on time created, a positive int returns files created more than int minutes ago, a negative int return files less than int minutes ago:
```bash
pyfind <dir> -dc <int>
```

* `--datemodified` or `-dm` similar to `--datecreated`, but then for filtering date modified:
```bash
pyfind <dir> -dc <int>
```

As filters stack, multiple flags can be used simultaneously.

## Contributing
Please refer to [CONTRIBUTING.md](https://gitlab.com/dkreeft/zoek/-/blob/master/CONTRIBUTING.md)

## License
[BSD-3](https://gitlab.com/dkreeft/zoek/-/blob/master/LICENSE)

