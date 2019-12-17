# -*- coding: utf-8 -*-
from itertools import permutations

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

    return result
    


#12-2
    
def build_dict(fin):
    """ Reads words in a document and builds a dictionary 
        that sets a group of letters as keys and a tuple 
        of possible words as values.
        
        fin: text document
        
        returns: dictionary
    """
    dict_of_words = {}
    for line in fin:
        word = line.strip()
        sorted_word = tuple(sorted(word))
        dict_of_words.setdefault(sorted_word, []).append(word)        
    
    return dict_of_words

def anagrams(d):
    """ Finds all anagrams in dictionary
    
        d: dictionary, keys=tuple of letters, 
        values=list of possible words
        
        returns: list
    """
    anagrams = [
            val 
            for val in d.values() 
            if len(val) > 1
            ]
    
    return anagrams

def sorted_anagrams(d):
    """ Finds all anagrams in dictionary and sorts them
        by length of list of anagrams in descending order.
        
        d: dictionary, keys=tuple of letters,
        values=list of possible words
        
        returns: list
    """
    sorted_anagrams = [
            val 
            for val in sorted(d.values(), key=len, reverse=True) 
            if len(val) > 1]
    
    return sorted_anagrams

def bingo(d):
    """ Fids the collection of eight letters that form the
        most possible Scrabble bingos.
        
        d: dictionary, keys=tuple of letters,
        values=list of possible words
        
        returns: list
    """
    bingo_anagrams = [
            word_list
            for key, word_list in d.items()
            if len(key) == 8 and len(word_list) == 7
            ]
    
    return bingo_anagrams

#12-3
def metathesis_pair(list_):

    for i, item in enumerate(list_):
        print(item)
        for j, char in enumerate(item):
            print(char)
            print(list_[i][j])
                        
                

if __name__ == "__main__":
    
    f = open('words.txt')
    new_dict = build_dict(f)
    
    anagrams = anagrams(new_dict)
    sorted_anagrams = sorted_anagrams(new_dict)
    bingo = bingo(new_dict)

    new_list = metathesis_pair(anagrams)
    
    
    
    
    

    