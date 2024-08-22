from capitalize_package.capitalize import capitalize

def main():
    if capitalize('hello') != 'Hello':
        raise Exception('Function does not work correctly!')

    if capitalize('') != '':
        raise Exception('Function does not work correctly!')

    print('All tests passed')


if __name__ == '__main__':
    main()
