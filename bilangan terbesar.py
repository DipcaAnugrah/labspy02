# Mencari Bilangan Terbesar
a = int(input("Masukkan Nilai ke-1: "))
b = int(input("Masukkan Nilai ke-2: "))
c = int(input("Masukkan Nilai ke-3: "))
if c < a > b :
    d = a
elif c > a < b :
    d = b
    if c > b:
        d = c
print ("Bilangan terbesar adalah : ",d)