# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import re

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, 'r') as f:
        file_content = f.read()
    
    return file_content

# Additionals to check
#content = read_file_content('story.txt')
#print(content)



def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    # First: We turn all characters to lowercase
    text = text.lower()

    # Second: We substitute all not alphanumeric characters to a whitespace at all
    text = re.sub(r'[^\w]', ' ', text)

    # Third: we turn the double whitespaces into single whitespace
    text = re.sub(r'[^\w]', ' ', text)

    # Fourth: We split the file based on whitespaces and save the individual strngs to a list
    list_of_words = text.split(" ")

    # Fifth: We create an empty dictionary
    dict_of_words = {}

    # Fifth: We loop through the list to obtain each word
    for words in list_of_words:
        
        # Sixth: We check if the word is a key in the dictionary already
        if words in dict_of_words.keys():
            
            # Then we update the value by 1
            dict_of_words[words] += 1

        # Checking if it is an empty string then pass
        elif words == "":
            pass

        # Seventh: If the word is not a key yet then we create a new one
        else:

            # Then we give it the value of 1
            dict_of_words[words] = 1

    return dict_of_words

# Check Solution
#solution = count_words()
#print(solution)
