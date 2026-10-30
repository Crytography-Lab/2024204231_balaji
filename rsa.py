
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))

if not is_prime(p) or not is_prime(q) or p == q:
    print("Enter two distinct prime numbers")
else:
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = 1
    while (d * e) % phi != 1:
        d += 1

    print("\nn =", n)
    print("Phi =", phi)
    print("Public exponent e =", e)
    print("Private exponent d =", d)
    print("Public key =", (e, n))
    print("Private key =", (d, n))

    m = int(input("Enter message as a number: "))

    if 0 <= m < n:
        c = pow(m, e, n)
        print("Encrypted message =", c)

        decrypted = pow(c, d, n)
        print("Decrypted message =", decrypted)
    else:
        print("Message must be between 0 and", n - 1)