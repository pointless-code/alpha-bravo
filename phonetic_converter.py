import json
import sys

class PhoneticConverter:
    def __init__(self, json_file):
        with open(json_file, 'r') as file:
            self.phonetic_alphabet = json.load(file)

    def convert_to_phonetic(self, text):
        result = []
        for char in text.upper():
            if char in self.phonetic_alphabet:
                result.append(self.phonetic_alphabet[char])
            else:
                result.append(char)
        return ' '.join(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the text to convert as a command-line argument.")
        sys.exit(1)

    text = sys.argv[1]
    converter = PhoneticConverter('phonetic_alphabet.json')
    phonetic_text = converter.convert_to_phonetic(text)
    print(phonetic_text)
