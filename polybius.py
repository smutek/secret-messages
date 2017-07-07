from ciphers import Cipher
from helpers import Helpers
import re


class Polybius(Cipher):
    def __init__(self):
        # instantiate an instance of the helpers class
        self.helpers = Helpers()
        # generate a polybro square

    def __process_text(self, message):
        output = []

        return ''.join(output)

    def encrypt(self, message):

        output = []
        polybius = self.helpers.polybius_square()

        for character in message:
            if str.isalpha(character):
                pair = polybius[character]
                for char in pair:
                    output.append(str(char))
            elif character == " ":
                output.append(character)

        return ''.join(output)

    def decrypt(self, message):

        polybius = self.helpers.polybius_square()
        output = []

        # To convert the encrypted string back to plain text I need
        # to split the numbers into groups of 2, since the pattern
        # is (x,y) for each letter. But, there's also spaces peppered
        # throughout the message, and spaces only take up one space...
        # so..... I'm sure there's a better way to do this, and I'll
        # smack my head when I see some elegant, one line, Pythonic
        # solution, but for now this is the best I've got. :)

        # First convert spaces to a character that takes up 2 spaces
        # with the re: module and a simple regex thing
        # this turns the string from "1213 1415" to "1213::1415"
        convert_spaces = re.sub("[ ]", "::", message)
        n = 2
        # next split the string into chunks of 2. This gives back a
        # list of pairs, so "1213::1415" becomes ['12', '13', '::', '14', '15']
        pairs_list = [convert_spaces[i:i + 2] for i in range(0, len(convert_spaces), 2)]

        # Now render the output by going through each pair and matching it
        # to a pair in the polybius square so we can pull the appropriate key
        # and append it to the output
        for pair in pairs_list:
            # Convert & append the space.
            if pair == "::":
                output.append(" ")
            else:
                # values in the polybius square are comma separated
                # lists of 2 integers. Our pairs are strings with 2 numbers,
                # so, convert each string to an int, so ['13'] becomes [1,3]
                value_to_match = [int(x) for x in pair]
                # now find a match in the polybius square
                for key, value in polybius.items():
                    if value == value_to_match:
                        # and add the key back to the output
                        output.append(key)

        return ''.join(output)
