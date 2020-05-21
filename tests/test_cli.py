import pytest
from click.testing import CliRunner
import zoek.cli as zk


def test_main(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    result = runner.invoke(zk.main, [path])
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert sorted(output) == sorted(return_files_1)


def test_depth_2(create_file_system, return_files_1, return_files_2):
    path = str(create_file_system)
    runner = CliRunner()
    result = runner.invoke(zk.main, [path, '--depth', '2'])
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert sorted(output) == sorted(return_files_1 + return_files_2)


def test_startswith(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    startswith_filter = 'a'
    result = runner.invoke(zk.main, [path, '--startswith', startswith_filter])
    filtered = [k for k in return_files_1 if k.startswith(startswith_filter)]
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert sorted(output) == sorted(filtered)


def test_contains(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    contains_filter = 'file'
    result = runner.invoke(zk.main, [path, '--contains', contains_filter])
    filtered = [k for k in return_files_1 if contains_filter in k]
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert sorted(output) == sorted(filtered)


def test_minsize(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    minsize = -1
    result = runner.invoke(zk.main, [path, '--minsize', minsize])
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert sorted(output) == sorted(return_files_1)


def test_datecreated(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    datecreated = -2
    result = runner.invoke(zk.main, [path, '--datecreated', datecreated])
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert sorted(output) == sorted(return_files_1)


def test_datecreated_wrong(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    datecreated = 2
    result = runner.invoke(zk.main, [path, '--datecreated', datecreated])
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert sorted(output) != sorted(return_files_1)


def test_datemodified(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    datemodified = -2
    result = runner.invoke(zk.main, [path, '--datemodified', datemodified])
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert sorted(output) == sorted(return_files_1)


def test_datemodified_wrong(create_file_system, return_files_1):
    path = str(create_file_system)
    runner = CliRunner()
    datemodified = 2
    result = runner.invoke(zk.main, [path, '--datemodified', datemodified])
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert sorted(output) != sorted(return_files_1)
