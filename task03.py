matn = input("marn kiriting: ")
sanoq = 0 

for harf in matn:
    if harf.isupper():
        sanoq += 1

print("katta harflar soni: ", sanoq)