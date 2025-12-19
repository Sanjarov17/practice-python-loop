soz = input("soz kiriting: ")
teskari = ""

for harf in soz:
    teskari = harf + teskari

if soz == teskari:
    print("palindrom")
else:
    print("palindrom emas")