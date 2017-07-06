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
        pass