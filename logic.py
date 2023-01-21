class Logic:
    MorseCode = {'a': '.-', 'b': '-...',
                 'c': '-.-.', 'd': '-..', 'e': '.',
                 'f': '..-.', 'g': '--.', 'h': '....',
                 'i': '..', 'j': '.---', 'k': '-.-',
                 'l': '.-..', 'm': '--', 'n': '-.',
                 'o': '---', 'p': '.--.', 'q': '--.-',
                 'r': '.-.', 's': '...', 't': '-',
                 'u': '..-', 'v': '...-', 'w': '.--',
                 'x': '-..-', 'y': '-.--', 'z': '--..',
                 '1': '.----', '2': '..---', '3': '...--',
                 '4': '....-', '5': '.....', '6': '-....',
                 '7': '--...', '8': '---..', '9': '----.',
                 '0': '-----', ', ': '--..--', '.': '.-.-.-',
                 '?': '..--..', '/': '-..-.', '-': '-....-',
                 '(': '-.--.', ')': '-.--.-'}

    @staticmethod
    def encode_to_morse(text: str):
        text = text.lower()
        to_return = ""
        for char in text:
            if char == " ":
                to_return += " / "
            else:
                to_return += Logic.MorseCode[char] + " "
        to_return = to_return.replace("  ", " ")
        return to_return

    @staticmethod
    def decode_from_morse(code: str):
        inverted_dict = {v: k for k, v in Logic.MorseCode.items()}
        words = code.split(" / ")
        to_return = ""
        for word in words:
            chars = word.split()
            for char in chars:
                try:
                    to_return += inverted_dict[char]
                except KeyError:
                    pass
            to_return += " "
        return to_return[:-1]

