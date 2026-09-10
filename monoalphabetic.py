import string

def encrypt(text, key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    result = ""

    for ch in text.upper():
        if ch in alphabet:
            index = alphabet.index(ch)
            result += key[index]
        else:
            result += ch

    return result


def decrypt(text, key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    result = ""

    for ch in text:
        if ch in key:
            index = key.index(ch)
            result += alphabet[index]
        else:
            result += ch

    return result


text = input("Enter the text: ")
key = input("Enter the key: ")

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)