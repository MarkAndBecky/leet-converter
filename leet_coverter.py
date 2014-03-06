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


def convert(input_word):

    leet_word = ""

    for i in input_word:
        if i.upper() not in leet_alphabet.keys():
            leet_word += i
        else:
            leet_word += choice(leet_alphabet[i.upper()])

    print leet_word
    return leet_word


def convert_vowels(input_word):

    leet_word = ""
    vowels = ["A", "E", "I", "O", "U", " "]

    for i in input_word:
        if i.upper() in vowels:
            leet_word += choice(leet_alphabet[i.upper()])
        else:
            leet_word += i

    print leet_word
    return leet_word
    
    
def main():

    word = raw_input("Word to convert:")
    convert(word)
    convert_vowels(word)

if __name__ == '__main__':
    main()