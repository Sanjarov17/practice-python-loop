import random

yashirin_son = random.randint(1, 20)
topildi = False

while not topildi:
    taxmin = int(input("Son kiriting: "))

    if taxmin == yashirin_son:
        print("topding ")
        topildi = True
    else:
        print("xaro yna urinib kuring")