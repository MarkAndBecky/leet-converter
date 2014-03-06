import sys
import os.path
from random import choice

leet_alphabet = {
    "A": ["4", "/-\\", "/_\\", "@", "/\\"],
    "B": ["8","|3", "13", "|}", "|:", "|8", "18", "6", "|B"],
    "C": ["<", "{", "[", "("],
    "D": ["|)", "|}", "|]"],
    "E": "3",
    "F": ["|=", "ph", "|#", "|"],
    "G": ["[-", "[+", "6"],
    "H": ["|-|", "[-]", "{-}", "|=|", "[=]", "{=}"],
    "I": ["1", "|"],
    "J": ["_|", "_/", "_7", "_)"],
    "K": ["|<", "1<"],
    "L": ["|_", "|,"],
    "M": ["44", "|\/|", "^^", "/\/\\", "/X\\", "[]\/][", "[]V[]", "][\\\\//][", "//.", ".\\\\", "N\\"],
    "N": ["|\|", "/\/", "/V", "][\\]["],
    "O": ["0", "()", "[]", "{}"],
    "P": ["|o", "|O", "|>", "|*", "|D", "/o"],
    "Q": ["O_", "9", "(,)"],
    "R": ["|2", "12", ".-", "|^"],
    "S": ["5", "$"],
    "T": ["7", "+", "7`", "'|'"],
    "U": ["|_|", "\_\\", "/_/", "\_/", "(_)"],
    "V": "\/",
    "W": ["\/\/", "(/\)", "\^/", "|/\|", "\X/", "\\\\'", "'//"],
    "X": ["%", "*", "><", "}{", ")("],
    "Y": ["`/"],
    "Z": ["2", "7_", ">_"],
    " ": " "
}


leet_words = {
    "and": ["nd"],
    "the": ["teh", "t3h"],
    "like": ["liek"],
    "hacker": ["Haxx0r", "Haxxr"],
    "please": ["pl0x"],
    "what": ["wut", "wat", "whut"],
    "you": ["u", "j00"],
    "are": ["r"],
    "why": ["y"],
    "leet": ["1337", "|33t"]
}


def convert(input_word):

    leet_word = ""

    for i in input_word:
        if i.upper() not in leet_alphabet.keys():
            leet_word += i
        else:
            leet_word += choice(leet_alphabet[i.upper()])

    return leet_word

def convert_vowels(input_word):

    leet_word = ""
    vowels = ["A", "E", "I", "O", "U", " "]

    for i in input_word:
        if i.upper() in vowels:
            leet_word += choice(leet_alphabet[i.upper()])
        else:
            leet_word += i

    return leet_word

def convert_text(input_text):

    split_text = input_text.split()
    leet_text = []

    for word in split_text:
        if word[len(word)-1].lower() not in leet_alphabet.keys():
            trunc_word = word[0:len(word)-1]
            if trunc_word.lower() in leet_words.keys():
                leet_text.append("".join([choice(leet_words[trunc_word.lower()]), word[len(word)-1]]))
            else:
                leet_text.append("".join([convert_vowels(trunc_word), word[len(word)-1]]))
        else:
            if word.lower() in leet_words.keys():
                leet_text.append(choice(leet_words[word.lower()]))
            else:
                leet_text.append(convert_vowels(word))
                
    return " ".join(leet_text)

def main():
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            input_file = open(sys.argv[1])
            lines = input_file.readlines()
            input_file.close()

            for line in lines:
                print convert_text(line)
        else:
            print "Can't find file"
    else:
        text = raw_input("Text to convert:")
        #print "Translation: ", convert(text)
        #print "Translation: ", convert_vowels(text)
        print "Translation: ", convert_text(text)
    
if __name__ == '__main__':
    main()