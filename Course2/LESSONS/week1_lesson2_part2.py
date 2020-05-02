import doctest

def func1(seq : str) -> bool:
    """
    Проверка правильности аргументов и вывода
    >>> func1("()(())")
    True
    >>> func1("()[()]")
    True
    >>> func1(")")
    False
    >>> func1("[()")
    False
    >>> func1("[(])")
    False
    :param seq:
    :return:
    """
    return True

if __name__ == '__main__':
    doctest.testmod()