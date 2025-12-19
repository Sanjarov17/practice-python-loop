import random

pin = random.randint(1000, 9999)
urinishlar = 0 

while urinishlar < 7:
    taxmin = int(input("pin kiriting: "))
    urinishlar += 1

    if taxmin > pin:
        print("juda katta son ")
    elif taxmin < pin:
        print("juda kichik son ")
    else:
        print("tabriklaymiz topding")
        break
else:
    print("urinishlar soni tugadi pin: " , pin)