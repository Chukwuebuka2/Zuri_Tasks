# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

import re

    
def find_anagram(word, anagram):

    # To ignore whitespaces and symbols add
    '''word = re.sub(r'[^\w]', '', word)
    anagram = re.sub(r'[^\w]', '', anagram)'''
    
    # We sort and turn all characters to lower case
    if sorted(word.lower()) == sorted(anagram.lower()):
        return True
    else:
        return True
