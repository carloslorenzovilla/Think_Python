# -*- coding: utf-8 -*-
def sumall(*args):
    """ Returns the sum of all elements in a tuple of any length

        args: tuple of numbers of any length

        returns: int
    """
    return sum(*args)

#12-1

def most_frequent(string_):
    """ Returns letters in descending order of 
        frequency.

        string_: string of characters

    """
    count = {}
    for char in string_:
        count[char] = count.get(char, 0) + 1
    
    temp = []
    for char, freq in count.items():
        temp.append((freq, char))

    temp.sort(reverse=True)

    result = []
    for freq, char in temp:
        result.append(char)

    print(*result)
    


#12-2

if __name__ == "__main__":
    
    most_frequent('zaanbnb asdkjfhaksdf aqwieur!')

    