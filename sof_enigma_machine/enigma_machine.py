# ----------------- Enigma-Machine-Theory / Components ------------------

# The Enigma Machine contains five different components:
# Keyboard:
# The keyboard is used to retrieve the user input.
# The# Enigma machine is a symmetric encryption machine.
# Which means that it can be used to both encrypt or decrypt a
# message using the same settings. The keyboard is hence used
# to either enter the plaintext that needs to be
# encrypted or the ciphertext that needs to be decrypted.
# # They keyboard consists of 26 keys for each letter of the alphabet.

# Plugboard:
# Once a key is pressed on the keyboard, it goes through
# the plugboard which provides the first stage of the
# encryption process. It is based on the principles of
# a substitution cipher, a form of transposition encryption.

# Rotors:
# After the plugboard, the letter goes through the three rotors
# in order (from right to left), each of them changing it
# differently using a combination of transposition cipher and
# Caesar cipher!
# This provides a few settings of the Enigma machine: which
# rotors to use, and in which order to position them.
#
# Reflector:
# The reflector is another type of rotor inside the machine.
# Once the letter has gone through the three # rotors from
# right to left, the reflector will reflect the electrical
# current back through the rotors, sending the
# encrypted letter through the rotors from left to right
# for another three stages of encryption and then through the
# plugboard again for a final substitution cipher.
# When going through the reflector, a permutation cipher
# is also applied to the letter.
#
# Lampboard: The lampboard is the final stage of the encryption
# process and is used to show the output (encrypted
# letter). It consists of 26 light bulbs, one for each letter of the alphabet.
# -------------------------------------------------------------------

# ----------------- Settings for the Enigma-Machine -----------------

import random as r
from colorama import init
from colorama import Fore
import time

rotors = ("I", "II", "III")
reflector = "PQR-D"
settings_ring = "ABC"
positions_ring = "FGH"
plugboard = "AT BS DE FM IR KN LZ OW PV XY"


# In this section you can do some basic setups for the enigma machine.
# ---------------------------------------------------------------------

# ------------------------ Code Explanation ---------------------------
# Code Explanation Section 1: At first we program the so called
# caesar algorithm for further usage.

# Explanation of the caesar cipher: is one of the simplest and most widely
# known encryption techniques. It is a type of substitution cipher in which
# each letter in the plaintext is replaced by a letter some fixed number of positions
# down the alphabet.
# ----------------------------------------------------------------------

def caesar_algorithm(string, amount):
    output = ""

    for i in range(0, len(string)):
        c = string[i]
        code = ord(c)
        if (code >= 65) and (code <= 90):
            c = chr(((code - 65 + amount) % 26) + 65)
        output = output + c

    return output


# ----------------- Enigma-Notch-Explanation -----------------
# Sets the starting position for each rotor
# (can easily be changed)
# ----------------------------------------------------------

def enigma_machine(emptytext):
    global rotors, reflector, settings_ring, positions_ring, plugboard
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor1Notch = "J"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor2Notch = "E"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    rotor3Notch = "P"
    rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
    rotor4Notch = "X"
    rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
    rotor5Notch = "G"

    rotorDict = {"I": rotor1, "II": rotor2, "III": rotor3, "IV": rotor4, "V": rotor5}
    rotorNotchDict = {"I": rotor1Notch, "II": rotor2Notch, "III": rotor3Notch, "IV": rotor4Notch, "V": rotor5Notch}

    reflectorB = {"A": "Y", "Y": "A", "B": "R", "R": "B", "C": "U", "U": "C", "D": "H", "H": "D", "E": "Q", "Q": "E",
                  "F": "S", "S": "F", "G": "L", "L": "G", "I": "P", "P": "I", "J": "X", "X": "J", "K": "N", "N": "K",
                  "M": "O", "O": "M", "T": "Z", "Z": "T", "V": "W", "W": "V"}
    reflectorC = {"A": "F", "F": "A", "B": "V", "V": "B", "C": "P", "P": "C", "D": "J", "J": "D", "E": "I", "I": "E",
                  "G": "O", "O": "G", "H": "Y", "Y": "H", "K": "R", "R": "K", "L": "Z", "Z": "L", "M": "X", "X": "M",
                  "N": "W", "W": "N", "Q": "T", "T": "Q", "S": "U", "U": "S"}

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if reflector == "PQR-D":
        reflectorDict = reflectorB
    else:
        reflectorDict = reflectorC

    # ----------------- Enigma-Rotor-Direction ------------------
    # A = LEFT Rotor
    # B = MIDDLE Rotor
    # C = RIGHT Rotor
    # ----------------------------------------------------------

    rotor_A = rotorDict[rotors[0]]
    rotor_B = rotorDict[rotors[1]]
    rotor_C = rotorDict[rotors[2]]
    # rotorNotchA = rotorNotchDict[rotors[0]]
    # never reached, but for comprehensibility i did not delete it
    notch_rotor_B = rotorNotchDict[rotors[1]]
    notch_rotor_C = rotorNotchDict[rotors[2]]

    letter_rotor_A = positions_ring[0]
    letter_rotor_B = positions_ring[1]
    letter_rotor_C = positions_ring[2]

    rotor_setting_A = settings_ring[0]
    offset_setting_A = alphabet.index(rotor_setting_A)
    # rotor_setting_B = ringSettings[1]
    # never reached, but for comprehensibility i did not delete it
    offset_setting_B = alphabet.index(rotor_setting_A)
    # rotor_setting_C = ringSettings[2]
    # never reached, but for comprehensibility i did not delete it
    offset_setting_C = alphabet.index(rotor_setting_A)

    rotor_A = caesar_algorithm(rotor_A, offset_setting_A)
    rotor_B = caesar_algorithm(rotor_B, offset_setting_B)
    rotor_C = caesar_algorithm(rotor_C, offset_setting_C)

    if offset_setting_A > 0:
        rotor_A = rotor_A[26 - offset_setting_A:] + rotor_A[0, 26 - offset_setting_A]
    if offset_setting_B > 0:
        rotor_B = rotor_B[26 - offset_setting_B:] + rotor_B[0, 26 - offset_setting_B]
    if offset_setting_C > 0:
        rotor_C = rotor_C[26 - offset_setting_C:] + rotor_C[0, 26 - offset_setting_C]

    ciphertext = ""

    # Setup the dictionary for the plugboard
    connections_plugboard = plugboard.upper().split(" ")
    dictionary_plugboard = {}
    for pairwise in connections_plugboard:
        if len(pairwise) == 2:
            dictionary_plugboard[pairwise[0]] = pairwise[1]
            dictionary_plugboard[pairwise[1]] = pairwise[0]

    emptytext = emptytext.upper()
    for letter in emptytext:
        letter_encrypted = letter

        if letter in alphabet:
            # First spin of the rotor - needs to be executed before first letter gets encrypted
            rotor_trigger = False
            # Third rotor increases by one for each letter pressed.
            if letter_rotor_C == notch_rotor_C:
                rotor_trigger = True
            letter_rotor_C = alphabet[(alphabet.index(letter_rotor_C) + 1) % 26]
            # Check if rotor three needs to turn
            if rotor_trigger:
                rotor_trigger = False
                if letter_rotor_B == notch_rotor_B:
                    rotor_trigger = True
                letter_rotor_B = alphabet[(alphabet.index(letter_rotor_B) + 1) % 26]

                # Check if rotor one needs to turn
                if rotor_trigger:
                    rotor_trigger = False
                    letter_rotor_A = alphabet[(alphabet.index(letter_rotor_A) + 1) % 26]

            else:
                # Check for double sequence
                if letter_rotor_B == notch_rotor_B:
                    letter_rotor_B = alphabet[(alphabet.index(letter_rotor_B) + 1) % 26]
                    letter_rotor_A = alphabet[(alphabet.index(letter_rotor_A) + 1) % 26]

            # Implementation of the plugboard
            if letter in dictionary_plugboard.keys():
                if dictionary_plugboard[letter] != "":
                    letter_encrypted = dictionary_plugboard[letter]

            # ----------------- User-Input to Encryption ------------------

            # Encryption of the rotors
            offset_A = alphabet.index(letter_rotor_A)
            offset_B = alphabet.index(letter_rotor_B)
            offset_C = alphabet.index(letter_rotor_C)

            # Encryption of the first rotor
            position = alphabet.index(letter_encrypted)
            let = rotor_C[(position + offset_C) % 26]
            position = alphabet.index(let)
            letter_encrypted = alphabet[(position - offset_C + 26) % 26]

            # Encryption of the second rotor
            position = alphabet.index(letter_encrypted)
            let = rotor_B[(position + offset_B) % 26]
            position = alphabet.index(let)
            letter_encrypted = alphabet[(position - offset_B + 26) % 26]

            # Encryption of the third rotor
            position = alphabet.index(letter_encrypted)
            let = rotor_A[(position + offset_A) % 26]
            position = alphabet.index(let)
            letter_encrypted = alphabet[(position - offset_A + 26) % 26]

            # Encryption of the reflectors
            if letter_encrypted in reflectorDict.keys():
                if reflectorDict[letter_encrypted] != "":
                    letter_encrypted = reflectorDict[letter_encrypted]

            # ----------------- Encryption to original User Input ------------------

            # Encryption of the first rotor
            position = alphabet.index(letter_encrypted)
            let = alphabet[(position + offset_A) % 26]
            position = rotor_A.index(let)
            letter_encrypted = alphabet[(position - offset_A + 26) % 26]

            # Encryption of the second rotor
            position = alphabet.index(letter_encrypted)
            let = alphabet[(position + offset_B) % 26]
            position = rotor_B.index(let)
            letter_encrypted = alphabet[(position - offset_B + 26) % 26]

            # Encryption of the third rotor
            position = alphabet.index(letter_encrypted)
            let = alphabet[(position + offset_C) % 26]
            position = rotor_C.index(let)
            letter_encrypted = alphabet[(position - offset_C + 26) % 26]

            # Implementation of the plugboard
            if letter_encrypted in dictionary_plugboard.keys():
                if dictionary_plugboard[letter_encrypted] != "":
                    letter_encrypted = dictionary_plugboard[letter_encrypted]

        ciphertext = ciphertext + letter_encrypted

    return ciphertext


def matrix_effect():
    init()

    symbols = ["0", "1", " ", " "]
    line = []
    counter = 0

    for i in range(118):
        x = r.randint(0, 3)
        line.append(symbols[x])

        counter += 1

    for i in range(100):
        if counter % 5 == 0:
            r_symbols = [r.randint(0, 117) for x in range(10)]

            for i in r_symbols:
                line[i] = symbols[r.randint(0, 3)]
        print(Fore.GREEN, *line)
        counter += 1
        time.sleep(0.01)


# ----------------------------------------------------

# OUTPUT:

# ----------------------------------------------------

print("""                 _-====-__-======-__-========-_____-============-__
               _(                                                 _)
            OO(           _/_ _  _  _/_   _/_ _  _  _/_           )_
           0  (_          (__(_)(_) (__   (__(_)(_) (__            _)
         o0     (_                                                _)
        o         '=-___-===-_____-========-___________-===-dwb-='
      .o                                _________
     . ______          ______________  |         |      _____         _____         _____
   _()_||__|| ________ |            |  |_________|   __||___||__   __||___||__   __||___||__
  (         | |      | |            | __Y______00_| |           | |_         _| |_         _|
 /-OO----OO""="OO--OO"="OO--------OO"="OO-------OO"="OO-------OO"="OO-------OO"="OO-------OO"=
###############################################################################################
""")
print("Thank you for travelling with the encryption train! \nIt will be a pleasure for us to encrypt your text!")
print("")
print("Please enter the text you want to encrypt:")
user_input = input(">>")
solution_encrypted = enigma_machine(user_input)
matrix_effect()

print("\nEncrypted Text: \n " + solution_encrypted)
