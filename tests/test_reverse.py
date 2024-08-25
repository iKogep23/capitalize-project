from capitalize_package.reverse import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''

def test_fixture():
    with_input_path = 'tests/fixtures/input.txt'
    with_output_path = 'tests/fixtures/output.txt'
    with open(with_input_path, encoding='utf8') as input_file:
        result = reverse(input_file.read().strip())
    with open(with_output_path, encoding='utf8') as output_file:
        assert result == output_file.read().strip()
