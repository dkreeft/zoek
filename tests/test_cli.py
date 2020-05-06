import pytest
from click.testing import CliRunner
import zoek.cli as zk


def test_main(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    result = runner.invoke(zk.main, [path])
    exp = '\n'.join(return_files_1) + '\n'
    assert result.exit_code == 0
    assert result.output == exp


def test_depth_2(create_file_system, return_files_1, return_files_2):
    path = str(create_file_system)
    runner = CliRunner()
    result = runner.invoke(zk.main, [path, '--depth', '2'])
    exp = '\n'.join(return_files_2) + '\n' + '\n'.join(return_files_1) + '\n'
    assert result.exit_code == 0
    assert result.output == exp


def test_startswith(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    startswith_filter = 'a'
    result = runner.invoke(zk.main, [path, '--startswith', startswith_filter])
    filtered = [k for k in return_files_1 if k.startswith(startswith_filter)]
    exp = '\n'.join(filtered) + '\n'
    assert result.exit_code == 0
    assert result.output == exp


def test_contains(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    contains_filter = 'file'
    result = runner.invoke(zk.main, [path, '--contains', contains_filter])
    filtered = [k for k in return_files_1 if contains_filter in k]
    exp = '\n'.join(filtered) + '\n'
    assert result.exit_code == 0
    assert result.output == exp


def test_minsize(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    minsize = -1
    result = runner.invoke(zk.main, [path, '--minsize', minsize])
    exp = '\n'.join(return_files_1) + '\n'
    assert result.exit_code == 0
    assert result.output == exp


def test_datecreated(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    datecreated = -2
    result = runner.invoke(zk.main, [path, '--datecreated', datecreated])
    exp = '\n'.join(return_files_1) + '\n'
    assert result.exit_code == 0
    assert result.output == exp


def test_datecreated_wrong(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    datecreated = 2
    result = runner.invoke(zk.main, [path, '--datecreated', datecreated])
    exp = '\n'.join(return_files_1) + '\n'
    assert result.exit_code == 0
    assert result.output != exp


def test_datemodified(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    datemodified = -2
    result = runner.invoke(zk.main, [path, '--datemodified', datemodified])
    exp = '\n'.join(return_files_1) + '\n'
    assert result.exit_code == 0
    assert result.output == exp


def test_datemodified_wrong(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    datemodified = 2
    result = runner.invoke(zk.main, [path, '--datemodified', datemodified])
    exp = '\n'.join(return_files_1) + '\n'
    assert result.exit_code == 0
    assert result.output != exp
