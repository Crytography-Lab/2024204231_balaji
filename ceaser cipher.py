def caesar_encrypt(text, shift):
    result = ""

    for char in text:

        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

if shift < 1 or shift > 26:
    print("Invalid shift value! Enter a value between 1 and 26.")

else:
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypted)