matn = input("matn kiriting: ")
sanoq = 0 

for belgi in matn:
    if belgi == ".":
        sanoq += 1

print("gaplar soni: ", sanoq)