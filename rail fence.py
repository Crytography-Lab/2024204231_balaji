text=input("Enter message: ").replace(" ","")
key=int(input("Enter number of rails: "))

rail=["" for i in range(key)]
row=0
direction=1

for ch in text:
    rail[row]+=ch
    if row==0:
        direction=1
    elif row==key-1:
        direction=-1
    row+=direction

encrypted="".join(rail)
print("Encrypted:",encrypted)

pattern=[]
row=0
direction=1

for i in range(len(text)):
    pattern.append(row)
    if row==0:
        direction=1
    elif row==key-1:
        direction=-1
    row+=direction

decrypted=[""]*len(text)
index=0

for r in range(key):
    for i in range(len(text)):
        if pattern[i]==r:
            decrypted[i]=encrypted[index]
            index+=1

print("Decrypted:","".join(decrypted))