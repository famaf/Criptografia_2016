# -*- coding: utf-8 -*-


def print_frecuency(dictionary):
    for key in dictionary:
        print key, "=" , str(dictionary[key])+"%"


def check_percentage(dictionary):
    suma = 0

    for key in dictionary:
        suma += dictionary[key]

    if suma != 100:
        return -1
    else:
        return 1


def counter(plain_text):
    letter_counter = {}

    for letter in plain_text:
        letter_counter[letter] = letter_counter.get(letter, 0) + 1

    return letter_counter


def main():
    plain_text = str(raw_input("Plain Text: ")).lower()
    letter_counter = counter(plain_text)

    lenght = len(plain_text)

    frecuency_letter = {}
    for letter in letter_counter:
        frecuency = round(((letter_counter[letter]*100)/float(lenght)), 2)
        frecuency_letter[letter] = frecuency

    print_frecuency(frecuency_letter)


if __name__ == "__main__":
    main()
