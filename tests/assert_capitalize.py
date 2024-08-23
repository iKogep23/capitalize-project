from capitalize_package.capitalize import capitalize


def main():
    assert capitalize('hello') == 'Hello'

    assert capitalize('') == ''

    print('All tests passed')


if __name__ == '__main__':
    main()
