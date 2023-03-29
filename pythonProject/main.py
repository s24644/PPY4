# =-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=
import math
import string

print("=-=-=-=-=-=-Zadanie 1=-=-=-=-=-=")


def panel_calc(floor_length, floor_width, panel_length, panel_width, number_in_pack):
    floor_surface = floor_length * floor_width * 1.1
    panel_surface = panel_width * panel_length
    panel_number = int(math.ceil(floor_surface / panel_surface))
    package_number = int(math.ceil(panel_number / number_in_pack))

    return package_number


print("Wymagana liczba opakowań: ", panel_calc(4, 4, 0.20, 1, 10))

# =-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-

print("=-=-=-=-=-=Zadanie 2=-=-=-=-=-=-")


def prime(*args):
    for number in args:
        is_prime = True
        for i in range(2, int(math.ceil(math.sqrt(number))) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(number, "is prime")
        else:
            print(number, "is not prime")


prime(5, 6, 4, 3, 7, 5, 3, 2, 5)

# -=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print("=-=-=-=-=-Zadanie 3=-=-=-=-=-=-=")

alphabet_list = list(string.ascii_lowercase)
print(alphabet_list)

def cesar(sentence, key):
    sentence = sentence.lower()
    key = math.fmod(key, len(alphabet_list))
    print("final key: ", key)
    result = ""
    sentence_array = [char for char in sentence]
    for char in sentence_array:
        if char in alphabet_list:
            indexOfCurrentElement = alphabet_list.index(char)

            if key + indexOfCurrentElement > len(alphabet_list)-1: # czy wychodzi poza zakres listy
                tmpval = key - (len(alphabet_list) - indexOfCurrentElement)
                result += alphabet_list[int(tmpval)]

            else:
                result += alphabet_list[int(indexOfCurrentElement + key)]
        else:
            result += char
    print("result: ", result)

cesar("Dzień dobry, jestem Michał", 34)



