# -*- coding: utf-8 -*-


alphabet = "abcdefghijklmnopqrstuvwxyz"

TABLE = {
    "a": "h",
    "b": "p",
    "c": "x",
    "d": "k",
    "e": "s",
    "f": "m",
    "g": "u",
    "h": "o",
    "i": "b",
    "j": "z",
    "k": "g",
    "l": "t",
    "m": "c",
    "n": "r",
    "o": "i",
    "p": "w",
    "q": "y",
    "r": "l",
    "s": "f",
    "t": "j",
    "u": "a",
    "v": "v",
    "w": "e",
    "x": "q",
    "y": "n",
    "z": "d"
}


def permutation(plain_text):
    cipher_text = ""
    for letter in plain_text:
        if alphabet.find(letter) != -1:
            cipher_text += TABLE[letter]
        else:
            cipher_text += " "

    return cipher_text


def main():
    plain_text = raw_input("Plain Text: ").lower()
    cipher_text = permutation(plain_text)
    print(cipher_text)


if __name__ == '__main__':
    main()
