# === CS 115 Homework 2 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Esther Li
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 2 ===
import sys


sys.setrecursionlimit(10000) # Allows up to 10000 recursive calls
morse = (
    ('.-', 'A'), ('-...', 'B'), ('-.-.', 'C'), ('-..', 'D'), ('.', 'E'),
    ('..-.', 'F'), ('--.', 'G'), ('....', 'H'), ('..', 'I'), ('.---', 'J'),
    ('-.-', 'K'), ('.-..', 'L'), ('--', 'M'), ('-.', 'N'), ('---', 'O'),
    ('.--.', 'P'), ('--.-', 'Q'), ('.-.', 'R'), ('...', 'S'), ('-', 'T'),
    ('..-', 'U'), ('...-', 'V'), ('.--', 'W'), ('-..-', 'X'), ('-.--', 'Y'),
    ('--..', 'Z')
)

morseList = ('.-', '-...', '-.-.', '-..', '.', '..-.', '--.','....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
 '--.-', '.-.', '...', '-','..-',  '...-', '.--', '-..-', '-.--', '--..')
letterList  = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

dictionary = ("AM", "AS", "BE", "BED", "CAN", "EGG", "HE", "HER", "HIM",
    "HIS", "ILL", "IS", "KID", "ME", "MY", "ON", "OR", "SEE", "SO", "TO",
    "TOE", "TOW", "WAS", "WOW",)

from dict import dictionary

def lookup(letter):
    """
    Takes a letter and looks for its morse code equivalemt
    """
    def checkLetter(tup):
        """
        Checks whether or not the letter is in the inputted tuple
        """
        if letter in tup:
             return True
        return False
    return tuple(filter(checkLetter, morse))[0][0] #filters through the big morse list and adds the tuple with the lettter in it to a big tuple. To get the morse code equivalent, we take tuple with the morse-letter pair(index 0 because it is the only thing in the list), and get the index of the morse code (0 again)

def lookupRev(morseCode):
    """
    Takes a morse code and looks for its letter code equivalemt
    """
    def checkMorse(tup):
        """
        Checks whether or not the morse code is in the inputted tuple
        """
        if morseCode in tup:
             return True
        return False
    if(len(list(filter(checkMorse, morse))) == 0):
        return "?"
    return list(list(filter(checkMorse, morse))[0])[1]

def encode(plaintext):
    """
    Takes a string and translates it into morse code
    """
    listForm = list(plaintext)
    a = " "
    return a.join(list(map(lookup, listForm)))

def decode(cyphertext):
    
    """
    Takes a morse code and translates it into string code
    """
    
    listForm = []
    addString = ""
    def findSpace(string, addString):
        """
        Sorts through a string of morse code and seperates it into blocks, then adds them to a list
        """
        
        if(len(string)>0):
            if(string[0:1].isspace()):
                listForm.append(addString)
                addString = ""
                return findSpace(string[1:], addString)
            else:
                addString = addString + (string[0:1])
                if(len(string) == 1):
                    listForm.append(addString)
                else: return findSpace(string[1:], addString)
       
    findSpace(cyphertext, addString)
            
    
    a = ""
    return a.join(list(map(lookupRev, listForm)))


def encode2(plaintext):
    """
    Takes a string and translates it into morse code, without spaces
    """
    listForm = list(plaintext)
    a = ""
    return a.join(list(map(lookup, listForm)))


def matches(cyphertext):
    """
    takes cyphertext and returns a tuple with all possible words it could be that are also in "dictionary"
    """                      
    def isEqual(word):
        """
        Checks if the word in morse code without spaces matches the inputted morse code
        """
        translated = encode2(word)
        if(translated == cyphertext):
            return True
        
    return tuple(filter(isEqual, dictionary))
    
