def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            encrypted = chr(
                (ord(ch) - ord('A') + shift) % 26 + ord('A')
            )

            result += encrypted
            key_index += 1
        else:
            result += ch

    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            decrypted = chr(
                (ord(ch) - ord('A') - shift) % 26 + ord('A')
            )

            result += decrypted
            key_index += 1
        else:
            result += ch

    return result


text = input("Enter message: ")
key = input("Enter key: ")

encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)