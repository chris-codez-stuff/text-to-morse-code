CODE = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "0": "_____",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    ".": "._._._",
    ",": "__..__",
    "?": "..__..",
    "'": ".____.",
    "!": "_._.__",
    "/": "_.._.",
    "(": "_.__.",
    ")": "_.__._",
    "&": "._...",
    ":": "___...",
    ";": "_._._.",
    "=": "_..._",
    "+": "._._.",
    "-": "_...._",
    "_": "..__._",
    "\"": "._.._.",
    "$": "..._.._",
    "@": ".__._.",
    " ": "/"
}

letters = [letter.upper() for letter in list(input("Enter the text: "))]

morse_code = [CODE[letter] for letter in letters]

print(f"Morse Code: {" ".join(morse_code)}")
