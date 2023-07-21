
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                   'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
                   '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                   ', ': '--..--', '.': '.-.-.-', '?': '..--..',
                   '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

# LATIN_HARF = {} 
# for latin,mors in MORSE_CODE_DICT.items():
    # LATIN_HARF[mors] = latin


user_input = input("Lutfen adinizi latin harfleri ile yazin:")


a = list(user_input.upper())




user_output = {}



for x in a:
    for l,m in MORSE_CODE_DICT.items():
        if l == x:
            user_output[l] = m


cod = list(user_output.values())


b = ""
for z in cod:
    b += " " + z



print("Mors cod:",b)