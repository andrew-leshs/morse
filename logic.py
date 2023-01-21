class Logic:
    MorseCode = {'A': '.-', 'B': '-...',
                 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-',
                 'L': '.-..', 'M': '--', 'N': '-.',
                 'O': '---', 'P': '.--.', 'Q': '--.-',
                 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--',
                 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                 '1': '.----', '2': '..---', '3': '...--',
                 '4': '....-', '5': '.....', '6': '-....',
                 '7': '--...', '8': '---..', '9': '----.',
                 '0': '-----', ', ': '--..--', '.': '.-.-.-',
                 '?': '..--..', '/': '-..-.', '-': '-....-',
                 '(': '-.--.', ')': '-.--.-'}

    @staticmethod
    def encode_to_morse(text: str):
        text = text.upper()
        to_return = ""
        for char in text:
            if char == " ":
                to_return += " / "
            else:
                to_return += Logic.MorseCode[char] + " "
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

