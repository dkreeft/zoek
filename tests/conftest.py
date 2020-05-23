import pytest
from pathlib import Path


def make_list_of_test_file_names(depth: int = 1) -> list:
    if depth == 1:
        return ['file_b_depth_1.txt', 'file_a_depth_1.txt', 'another_file.txt']
    elif depth == 2:
        return ['file_c_depth_2.txt', 'file_d_depth_2.txt']
    elif depth == 3:
        return ['another_file_depth_3.txt']


@pytest.fixture(name='input_files_at_depth_1')
def input_files_at_depth_1() -> list:
    return make_list_of_test_file_names(depth = 1)


@pytest.fixture(name='input_files_at_depth_2')
def input_files_at_depth_2() -> list:
    return make_list_of_test_file_names(depth = 2)


@pytest.fixture(name='input_files_at_depth_3')
def input_files_at_depth_3() -> list:
    return make_list_of_test_file_names(depth = 3)


@pytest.fixture(scope='session')
def create_file_system(tmp_path_factory):
    """Creates a temporary file system with directories and files"""
    dir_1 = tmp_path_factory.mktemp('depth_1')
    for file_name in make_list_of_test_file_names(depth = 1):
        Path(dir_1 / file_name).touch()

    dir_2 = Path(dir_1 / 'depth_2')
    dir_2.mkdir()
    for file_name in make_list_of_test_file_names(depth = 2):
        Path(dir_2 / file_name).touch()

    dir_3 = Path(dir_2 / 'depth_3')
    dir_3.mkdir()
    for file_name in make_list_of_test_file_names(depth = 3):
        Path(dir_3 / file_name).touch()
    return dir_1
