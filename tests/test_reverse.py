from capitalize_package.reverse import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''
