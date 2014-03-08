#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
from random import choice

leet_alphabet = {
    "A": ["4", "/-\\", "/_\\", "@", "/\\"],
    "B": ["B", "b", "8","|3", "13", "|8", "18", "6"],
    "C": ["C", "c", "<", "{", "[", "("],
    "D": ["D", "d", "|)", "|}"],
    "E": ["3"],
    "F": ["F", "f", "|=", "ph"],
    "G": ["G", "g", "[+", "6"],
    "H": ["H", "h", "|-|", "|=|"],
    "I": ["1", "|"],
    "J": ["J", "j", "_|", "_)"],
    "K": ["K", "k", "|<", "1<"],
    "L": ["L", "l", "|_"],
    "M": ["M", "m", "|\/|", "/\/\\", "/X\\"],
    "N": ["N", "n", "|\|", "/V"],
    "O": ["0", "()", "[]", "{}"],
    "P": ["P", "p", "|o", "|O", "|>", "|*"],
    "Q": ["Q", "q", "(,)"],
    "R": ["R", "r", "|2"],
    "S": ["S", "s", "5", "$"],
    "T": ["T","t", "7", "+"],
    "U": ["|_|", "\_\\", "/_/", "\_/", "(_)"],
    "V": ["V", "v", "\/"],
    "W": ["W","w", "\/\/", "\^/", "\X/"],
    "X": ["X","x", "%", "*", "><"],
    "Y": ["Y","y","`/"],
    "Z": ["Z","z","2"],
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
    "leet": ["1337", "|33t"],
    "bye": ["bai"],
    "crap": ["carp"],
    "cake": ["ceak"],
    "dude": ["d00d"],
    "from": ["form"],
    "guys": ["guise"],
    "hacks": ["h4x", "h4x0rz"],
    "hi": ["hai"],
    "cool": ["kewl"],
    "master": ["mastah"],
    "max": ["max0r"],
    "maximum": ["max0r"],
    "own": ["pwn"],
    "fear": ["ph34", "phear", "ph34r", "ph33r"],
    "power": ["powwah"],
    "porn": ["pr0n"],
    "sex": ["secks"],
    "when": ["wen"],
    "winner": ["winnar"],
    "elite": ["1337", "|33t", "31337"],
    "censored": ["c3n50red"],
    "strong": ["stronk"],
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
        if word[len(word)-1].upper() not in leet_alphabet.keys():
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


def convert_all_text(input_all_text):

    split_text = input_all_text.split()
    leet_text = []

    for word in split_text:
        if word[len(word)-1].upper() not in leet_alphabet.keys():
            trunc_word = word[0:len(word)-1]
            if trunc_word.lower() in leet_words.keys():
                leet_text.append("".join([choice(leet_words[trunc_word.lower()]), word[len(word)-1]]))
            else:
                leet_text.append("".join([convert(trunc_word), word[len(word)-1]]))
        else:
            if word.lower() in leet_words.keys():
                leet_text.append(choice(leet_words[word.lower()]))
            else:
                leet_text.append(convert(word))

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
        print "Translation (leet words and vowels only: ", convert_text(text)
        print "Translation (leet words and all letters): ", convert_all_text(text)
    
if __name__ == '__main__':
    main()
