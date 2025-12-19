eng_katta = int(input("1-sonni kiriting: "))

for i in range(5):
    son = int(input("Son kiriting: "))
    if son > eng_katta:
        eng_katta = son

print("Eng katta son:", eng_katta)
