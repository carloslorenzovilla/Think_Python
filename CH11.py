# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:27:38 2019

@author: Carlos Villa
"""

#Fibonacci by dictionary. WOW! It it FAST!!
known = {0:1, 1:1}
def fibonacci(n):
    """ Calculates the fibonacci series using a dictionary
        to improve performance. Employs recursion.

        n: int

        returns: int 
    """
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n -2)
    known[n] = res
    
    return res

#histogram
def histogram(s):
    """ Creates a histogram of a string using dictionary
    
        s: string
    
        returns: dictionary
    """
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

#11-1
def build_dict(fin):
    """ Reads words in a docoment and stores
        them in a dictionary.
        
        fin: txt file
    
        returns: dictionary
    """
    dict_of_words = {}
    for line in fin:
        word = line.strip()
        dict_of_words[word] = 1
    
    return dict_of_words

#11-2
def invert_dict(d):
    """ Inverts a dictionary, mapping values to keys in
        a list.

        d: dictionary

        returns: dictionary
    """
    inverse = {}
    for key in d:
        val = d[key]
        #if val is not in inverse, start a singleton value
        #otherwise append the key to list value
        inverse.setdefault(val, []).append(key)
    
    return inverse

#11-3
ack_dict = {}
def ack(m, n):
    """ Memoized Ackermann function
    
        m: positive int
        n: positive int
        
        returns: dictionary value
        
    """   
    if m == 0:
        return n + 1
    
    if n == 0:
        return ack(m - 1, 1)

    if (m, n) in ack_dict:
        return ack_dict[m, n]
        
    else:
        ack_dict[m, n] = ack(m - 1, ack(m, n - 1))
        return ack_dict[m, n]

#11-4
def has_duplicates(d):
    """ Determines if dictionary has duplicates
    
        d: dictionary
        
        returns: boolean
    """
    for key in d:
        if d[key] > 1:
            return True
    return False

#11-5
def rotate_pairs(d):
    """ Finds all word rotate pairs in wordlist
    
        d: dictionary
        
        returns: list
    """
    pairs = []
    for key in d:
        rotate = key[::-1]
        if rotate in d and rotate != key:
            pairs.append(key)
    return pairs
    

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

def read_dictionary(filename='c06d.txt'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

#11-6
def homophones(w, p):
    """ Checks whether two words are homophones
    
        w: dictionary of words
        p: dictionary of word procunciation (key: word, value: pronunciation)
        
    """
    for key in w:
        key_min_1 = key[1:]
        key_min_2 = key[0] + key[2:]
        if key in p and key_min_1 in p and key_min_2 in p:
            if p[key] == p[key_min_1] == p[key_min_2]:
                print(f'{key}, {key_min_1}, {key_min_2}.')
                
if __name__ == '__main__':

    fin = open('words.txt')

#    hist = histogram('parot')
#    invert = invert_dict(hist)
#    ack(3,4)
#    
#    pairs = rotate_pairs(words)
#    
#    print(has_duplicates(hist))
    
    words = build_dict(fin)
    
    pronounce = read_dictionary()
    
    homophones(words, pronounce)
    
    
    