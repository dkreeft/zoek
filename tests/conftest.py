import pytest
from pathlib import Path


def return_files(depth: int = 1) -> list:
    if depth == 1:
        return ['file_b_depth_1.txt', 'file_a_depth_1.txt', 'another_file.txt']
    elif depth == 2:
        return ['file_c_depth_2.txt', 'file_d_depth_2.txt']
    elif depth == 3:
        return ['another_file_depth_3.txt']


@pytest.fixture(name='return_files_1')
def return_files_1() -> list:
    return return_files(1)


@pytest.fixture(name='return_files_2')
def return_files_2() -> list:
    return return_files(2)


@pytest.fixture(name='return_files_3')
def return_files_3() -> list:
    return return_files(3)


@pytest.fixture(scope='session')
def create_file_system(tmp_path_factory):
    """Creates a temporary file system with directories and files"""
    fn = tmp_path_factory.mktemp('depth_1')
    for _ in return_files(1):
        Path(fn / _).touch()
    dir_2 = Path(fn / 'depth_2')
    dir_2.mkdir()
    for _ in return_files(2):
        Path(dir_2 / _).touch()
    dir_3 = Path(dir_2 / 'depth_3')
    dir_3.mkdir()
    for _ in return_files(3):
        Path(dir_3 / _).touch()
    return fn
