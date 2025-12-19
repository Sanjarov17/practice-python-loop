togr_parol = "1122"

for urinish in range(3):
    parol = input("parolni kiriting: ")


    if parol == togr_parol:
        print("xush kelibsiz")
        break
    else:
        print("yana urinib kuring ")
else:
    print("Bloklandiz")