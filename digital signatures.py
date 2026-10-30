import hashlib

def sign(message, private_key):
    digest = hashlib.sha256(message.encode()).hexdigest()
    signature = hashlib.sha256((digest + private_key).encode()).hexdigest()
    return signature

def verify(message, signature, private_key):
    digest = hashlib.sha256(message.encode()).hexdigest()
    expected = hashlib.sha256((digest + private_key).encode()).hexdigest()
    return signature == expected

message = input("Enter message: ")
private_key = input("Enter private key: ")

signature = sign(message, private_key)
print("Digital Signature:", signature)

if verify(message, signature, private_key):
    print("Signature Verified")
else:
    print("Signature Invalid")

print("\nEthical Considerations:")
print("1. Protect private keys.")
print("2. Do not forge digital signatures.")
print("3. Respect privacy and data integrity.")
print("4. Use digital signatures legally and ethically.")