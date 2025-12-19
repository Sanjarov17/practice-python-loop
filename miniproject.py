narx = int(input("1-mahsulot narxini kiriting: "))

jami = narx
eng_qimmat = narx
eng_arzon = narx

for i in range(2, 6):
    narx = int(input(f"{i}-mahsulot narxini kiriting: "))

    jami += narx

    if narx > eng_qimmat:
        eng_qimmat = narx

    if narx < eng_arzon:
        eng_arzon = narx

print("\n HISOBOT")
print("Jami summa:", jami)
print("Eng qimmat mahsulot:", eng_qimmat)
print("Eng arzon mahsulot:", eng_arzon)