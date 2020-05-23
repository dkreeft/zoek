import operator
from zoek import *
# from zoek.file_iterator_from_path import file_iterator_from_path
# from zoek.print_file_iterator import print_file_iterator
# from zoek.filter_on_one_attribute import filter_on_one_attribute

def test_print_depth_1(capfd, create_file_system, input_files_at_depth_1):
    print_file_iterator(file_iterator_from_path(create_file_system), showpath=False)
    out, _ = capfd.readouterr()
    expected_return = '\n'.join(input_files_at_depth_1) + '\n'
    assert sorted(out) == sorted(expected_return)


def test_print_depth_2(capfd, create_file_system, input_files_at_depth_1, input_files_at_depth_2):
    print_file_iterator(file_iterator_from_path(create_file_system, max_depth=2), showpath=False)
    out, _ = capfd.readouterr()
    expected_return = '\n'.join(input_files_at_depth_2) + '\n' + '\n'.join(input_files_at_depth_1) + '\n'
    assert sorted(out) == sorted(expected_return)


def test_size_filter(capfd, create_file_system, input_files_at_depth_1, input_files_at_depth_2):
    generator = file_iterator_from_path(create_file_system, max_depth=2)
    filtered = filter_on_one_attribute(
        generator=generator,
        attributeType="st_size",
        condition_checker=operator.ge,
        value=0
    )
    print_file_iterator(filtered, showpath=False)
    out, _ = capfd.readouterr()
    expected_return = '\n'.join(input_files_at_depth_2) + '\n' + '\n'.join(input_files_at_depth_1) + '\n'
    assert sorted(out) == sorted(expected_return)
