alfab = "abcdefghijklmnopqrstuvwxyz"
tb = str.maketrans(alfab, alfab[::-1])

def translate(text):
    text = ''.join([s.lower() for s in text if s.isalnum()])
    return text.translate(tb)

def encode(plain_text):
    plain_text = translate(plain_text)
    ciphertext_with_spaces = ""
    for i in range(0, len(plain_text), 5):
        ciphertext_with_spaces += plain_text[i:i+5] + " "
    return ciphertext_with_spaces.strip()

def decode(ciphered_text):
    return translate(ciphered_text)


