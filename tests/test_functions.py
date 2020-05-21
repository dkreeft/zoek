import operator
from zoek.generator_from_path import generator_from_path
from zoek.print_iterator import print_iterator
from zoek._filter_attr import filter_attr


def test_print_depth_1(capfd, create_file_system, return_files_1):
    print_iterator(generator_from_path(create_file_system))
    out, _ = capfd.readouterr()
    exp = '\n'.join(return_files_1) + '\n'
    assert sorted(out) == sorted(exp)


def test_print_depth_2(capfd, create_file_system, return_files_1, return_files_2):
    print_iterator(generator_from_path(create_file_system, max_depth=2))
    out, _ = capfd.readouterr()
    exp = '\n'.join(return_files_2) + '\n' + '\n'.join(return_files_1) + '\n'
    assert sorted(out) == sorted(exp)


def test_size_filter(capfd, create_file_system, return_files_1, return_files_2):
    generator = generator_from_path(create_file_system, max_depth=2)
    filtered = filter_attr(
        generator=generator,
        attr="st_size",
        op=operator.ge,
        value=0
    )
    print_iterator(filtered)
    out, _ = capfd.readouterr()
    exp = '\n'.join(return_files_2) + '\n' + '\n'.join(return_files_1) + '\n'
    assert sorted(out) == sorted(exp)
