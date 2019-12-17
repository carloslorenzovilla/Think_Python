from random import randint

#10-1
def nested_sum(t):
    """ Calculates the sum of list of lists
    
        t: list of lists
    
        returns: number
    """
    new_t = []
    for item in t:
        new_t.append(sum(item))
    return sum(new_t)

#10-2
def cumsum(t):
    """ Calculates the cummulative sum of the elements in t
    
        t: list of numbers
    
        returns: list of numbers
    """
    new_t = []
    total = 0
    for i in t:
        total += i
        new_t.append(total)
    return new_t

#10-3
def middle(t):
    """ Returns a new list that contains all but the last
        and first elements of t
        
        t: list of numbers
        
        returns: new list
    """
    return t[1:-1]

#10-4
def chop(t):
    """ Modifies list by removing the first and last elements
    
        t: list
        
        returns: None    
    """
    del t[0]
    del t[-1]
    
#10-5
def is_sorted(t):
    """ Takes list t and returns True if list is sorted in
        ascending order. Returns False otherwise.
        
        t: list
        
        returns: Boolean    
    """
    return sorted(t) == t

#10-6
def is_anagram(word1, word2):
    """ Takes two strings and returns True if they are anagrams
    
        word1: string
        word2: string
        
        returns: Boolean
    """
    return sorted(word1) == sorted(word2)

#10-7
def has_duplicates(t):
    """ Takes a list and returns True if any element appears more
        than once.
        
        t: list
        
        returns: Boolean    
    """
    for i in t:
        if t.count(i) > 1:
            return True
    return False

#10-8
def list_of_birthdays():
    """ Generates a list of 23 birthdays
        
        returns: list
    """
    birthdays = []    
    while len(birthdays) < 23:
        
        birthday = randint(1,365)
        
        birthdays.append(birthday)
    
    return birthdays

def probability_of_birthday(n, list_of_birthdays, has_duplicates):
    """ Calculates the probability of two people sharing the same
        birthday according to the Birthday Paradox in n simulations.
        
        list_of_birthdays: function
        has_duplicates: function
        n: int
    
        returns: float    
    """
    count = 0
    for _ in range(n):
        birthdays = list_of_birthdays()
        
        if has_duplicates(birthdays):
            count += 1
    
    return (f'The probability is {count/n*100}%')

#10-9
def build_list(fin):
    list_of_words = []
    for line in fin:
        word = line.strip()
        list_of_words.append(word)
    return list_of_words
    
#list_of_words2 = build_list2(fin)

#10-10
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

#10-11
def reverse_pair(words, in_bisect):
    """ Determines if two words are "reverse pair". Returns a list
        of all reverse pairs.
    
        words: list
        
        in_bisect: function
        
        returns: list
    """
    reverse_pairs = []
    for line in words:
        word = line.strip()
        if word == word[::-1]:
            continue
        elif in_bisect(words, word[::-1]):
            reverse_pairs.append(word)
    
    return reverse_pairs

#10-12
def interlock(words, in_bisect):
    """ Finds interlocked word pairs (taking alternating letters
        from each and forms a new word)
    
        words: list
        
        in_bisect: function
        
        returns: list of lists    
    """
    interlocked = []
    
    for word in words:
        new_word1 = word[::2]
        new_word2 = word[1::2]
        if in_bisect(words, new_word1) and in_bisect(words, new_word2):
            interlocked.append([new_word1, new_word2, word])
    
    return interlocked
