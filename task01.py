matn = input("matn kiriting: ")
unlilar = "aeiouAEIOU"
sanoq = 0

for harf in matn:
    if harf in unlilar:
        sanoq += 1

print("unli harflar: ", sanoq)