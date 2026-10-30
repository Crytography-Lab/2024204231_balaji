p = int(input("Enter prime number: "))
g = int(input("Enter primitive root: "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's public key:", A)
print("Bob's public key:", B)

alice_key = pow(B, a, p)
bob_key = pow(A, b, p)

print("Alice's shared key:", alice_key)
print("Bob's shared key:", bob_key)

if alice_key == bob_key:
    print("Key exchange successful")
else:
    print("Key exchange failed")

print("\nMan-in-the-Middle (MitM) Consideration")
print("Diffie-Hellman alone does not authenticate users.")
print("An attacker may intercept and replace public keys.")
print("Use digital signatures or certificates to prevent MitM attacks.")