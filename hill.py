text = input("Enter 4-letter text: ").upper()

# Key matrix
a = [[3, 3],
     [2, 5]]

# Convert letters to numbers
p = []

for ch in text:
    p.append(ord(ch) - 65)

# Encryption
c = []

for i in range(0, 4, 2):
    x = a[0][0] * p[i] + a[0][1] * p[i+1]
    y = a[1][0] * p[i] + a[1][1] * p[i+1]

    c.append(x % 26)
    c.append(y % 26)

encrypted = ""

for x in c:
    encrypted += chr(x + 65)

print("Encrypted:", encrypted)

# Inverse key matrix
inverse = [[15, 17],
           [20, 9]]

# Decryption
d = []

for i in range(0, 4, 2):
    x = inverse[0][0] * c[i] + inverse[0][1] * c[i+1]
    y = inverse[1][0] * c[i] + inverse[1][1] * c[i+1]

    d.append(x % 26)
    d.append(y % 26)

decrypted = ""

for x in d:
    decrypted += chr(x + 65)

print("Decrypted:", decrypted)