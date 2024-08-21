from capitalize import capitalize


if capitalize('hello') != 'Hello':
    raise Exception('Function does not work correctly!')


if capitalize('') != '':
    raise Exception('Function does not work correctly!')


print('All tests passed')
