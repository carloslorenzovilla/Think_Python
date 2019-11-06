# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:27:38 2019

@author: Carlos Villa
"""

from itertools import permutations

def build_list(fin):
    """ Builds a list of words in a text file.
    
        Assumption: Text file line format is <word>\r\n
        
        fin: text file
        
        returns: list    
    """
    list_of_words = []
    for line in fin:
        word = line.strip()
        list_of_words.append(word)
    return list_of_words

def in_bisect(words, target):
    """ Determines if element is present in sorted list using
        a binary search. Uses recursion.
        
        words: list
        
        returns: boolean
    """
    if len(words) == 0:
        return False
    
    middle = len(words)//2
    
    if words[middle] == target:
        return True
    
    if target < words[middle]:
        return in_bisect(words[:middle], target)
    else:
        return in_bisect(words[middle+1:], target)
    
def generate_words(dictionary, letters, size, in_bisect):
    """ Generates a list of possible words of a
        specific size given a string of letters.
        Permutations are compared with elements in
        a dictionary.
        
        dictionary: list
        letter: string
        size: int
        
        returns: list
    """
    for word in permutations(letters, size):
        delimeter = ""
        possible_words = []
        new_word = delimeter.join(word)
        if in_bisect(new_word):
            possible_words.append(new_word)         
        
    return possible_words

fin = open('words.txt')
dictionary = build_list(fin)
letters = 'aixemt'
size = 3 #create exception, if size > len(letters)

print(generate_words(dictionary, letters, size, in_bisect))
