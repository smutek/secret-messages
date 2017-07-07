from ciphers import Cipher
from helpers import Helpers


class Atbash(Cipher):
    def __init__(self):
        # alphabet
        self.helpers = Helpers()
        self.alphabet = self.helpers.alphabet()
        # reverse alphabet
        self.reverse = self.alphabet[::-1]

    def encrypt(self, text):
        """
        Encrypt text by building a dictionary of key value pairs
        for the plain text char : encrypted text char

        :param text: plain text string
        :return: encrypted string
        """
        encryption_key = {}
        output = []
        text = text.upper()
        # build encrypt and decrypt keys as lists of corresponding
        # key value pairs ( {A:Z, B:Y} etc.)
        for i in range(len(self.alphabet)):
            encryption_key[self.alphabet[i]] = self.reverse[i]

        for letter in text:
            if letter in encryption_key:
                # match the incoming letter with its counterpart
                output.append(encryption_key[letter])
            else:
                # Pass punctuation and numbers through normally
                output.append(letter)

        return ''.join(output)

    def decrypt(self, text):
        """
        Decrypt text by building a dictionary of key value pairs
        Essentially the same as the process above, but in reverse

        :param text:
        :return:
        """
        decryption_key = {}
        output = []
        text = text.upper()
        for i in range(len(self.alphabet)):
            decryption_key[self.reverse[i]] = self.alphabet[i]

        for letter in text:
            if letter not in decryption_key:
                output.append(letter)
            else:
                output.append(decryption_key[letter])

        return ''.join(output)
