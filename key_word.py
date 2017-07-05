from ciphers import Cipher
from helpers import Helpers


class Keyword(Cipher):
    def __init__(self):
        # instantiate an instance of the helpers class
        self.helpers = Helpers()

    def __generate_key(self, keyword, action):
        encryption_key = {}

        # get separate modified & unmodified alpha objects
        plain_alpha = self.helpers.alphabet("list")
        cipher_alpha = self.helpers.alphabet("list")

        # remove duplicate letters from the keyword
        keyword_stripped = self.helpers.unique(keyword)

        # remove keyword letters from cipher alpha
        for i in range(len(keyword_stripped)):
            cipher_alpha.remove(keyword_stripped[i])

        # append keyword letters to cipher alpha
        cipher_alpha = keyword_stripped + cipher_alpha

        if action == "encrypt":
            # generate encryption key
            for i in range(len(plain_alpha)):
                encryption_key[plain_alpha[i]] = cipher_alpha[i]
        elif action == "decrypt":
            # generate decryption key
            for i in range(len(plain_alpha)):
                encryption_key[cipher_alpha[i]] = plain_alpha[i]
        else:
            raise ValueError("Cheatin', uh?")

        return encryption_key

    def __process_text(self, cipher_key, message):
        output = []
        # process text
        for letter in message:
            if letter not in cipher_key:
                output.append(letter)
            else:
                output.append(cipher_key[letter])

        return ''.join(output)

    def encrypt(self, user_input):

        # extract the message and keyword
        message = user_input[0]
        keyword = user_input[1]

        # generate encryption key
        cipher_key = self.__generate_key(keyword, "encrypt")

        # process and return text
        return self.__process_text(cipher_key, message)

    def decrypt(self, user_input):

        # extract the message and keyword
        message = user_input[0]
        keyword = user_input[1]

        # generate decryption key
        cipher_key = self.__generate_key(keyword, "decrypt")

        # process text
        return self.__process_text(cipher_key, message)
