# -*- coding: utf-8 -*-
def sumall(*args):
    """ Returns the sum of all elements in a tuple of any length

        args: tuple of numbers of any length

        returns: int
    """
    return sum(*args)


if __name__ == "__main__":
    
    a = [1, 2, 3, 4]

    for n in reversed(a):
        print(n)

    a.reverse()

    print(a)

    