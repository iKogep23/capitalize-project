def capitalize(text):
    '''Capitalizing first letter of given string.

    Usage examples:
    >>> capitalize('hello')
    'Hello'
    >>> capitalize('')
    ''
    '''
    if text == '':
        return ''
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'


def main():
    text = input('Пожалуйста, ведите текст: ')
    print(capitalize(text))


if __name__ == '__main__':
    main()
