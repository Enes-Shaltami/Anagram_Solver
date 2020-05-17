from itertools import permutations
from PyDictionary import PyDictionary

def allScrambledCombos(sample_string, string_size):
    AllStrings = set(permutations(sample_string, string_size))
    return AllStrings

def FindMeaningfulWords(AllStrings):
    dictionary = PyDictionary()
    Mean_Words = []

    for word in AllStrings:
        assem_word = ""
        for letter in word:
            assem_word += letter

        if (dictionary.meaning(assem_word, disable_errors=True) != None):
            Mean_Words.append(assem_word)
        else:
            pass    

    return Mean_Words

if __name__ == '__main__':
    sample_string = input("Enter a string to search for anagrams: ")
    string_size = input("How many letters should the anagram be? ")

    while(int(string_size) < 0 or int(string_size) > len(sample_string)):
        print("ERROR! The number of letters must be between 0 and {}. Please try again.".format(len(sample_string)))
        string_size = input("How many letters should the anagram be?")

    AllStrings = allScrambledCombos(sample_string, int(string_size))
    Mean_Words = FindMeaningfulWords(AllStrings)
    if len(Mean_Words) != 0:
        print("All possible anagrams:")
        for word in Mean_Words:
            print(word)
    else:
        print("No possible anagrams.")