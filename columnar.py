text=input("Enter message: ").replace(" ","")
key1=input("Enter first key: ")
key2=input("Enter second key: ")

def encrypt(text,key):
    n=len(key)
    rows=[]
    for i in range(0,len(text),n):
        row=text[i:i+n]
        if len(row)<n:
            row+="X"*(n-len(row))
        rows.append(row)

    order=sorted(range(n),key=lambda i:key[i])
    result=""

    for col in order:
        for row in rows:
            result+=row[col]

    return result

def decrypt(text,key):
    n=len(key)
    rows=len(text)//n
    order=sorted(range(n),key=lambda i:key[i])
    columns=[""]*n
    index=0

    for col in order:
        columns[col]=text[index:index+rows]
        index+=rows

    result=""
    for i in range(rows):
        for col in range(n):
            result+=columns[col][i]

    return result.rstrip("X")

first=encrypt(text,key1)
encrypted=encrypt(first,key2)

print("Encrypted:",encrypted)

first=decrypt(encrypted,key2)
decrypted=decrypt(first,key1)

print("Decrypted:",decrypted)