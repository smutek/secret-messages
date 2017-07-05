import string


class Helpers():
    def unique(self, text):

        output = []

        for letter in text:
            if letter not in output:
                output.append(letter)

        return output

    def alphabet(self, type=None):

        if type is None or type == "string":
            alpha = string.ascii_uppercase
        elif type == "list":
            alpha = list(string.ascii_uppercase)

        return alpha
