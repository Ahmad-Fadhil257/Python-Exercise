karakter = input("Masukkan nilai karakter siswa \t\t: ").lower()
Matematika = int(input("Masukkan nilai Matematika siswa \t: "))
indo = int(input("Masukkan nilai B.Indonesia siswa \t: "))
ing = int(input("Masukkan nilai B.Inggris siswa \t\t: "))

if (karakter == 'a' or karakter == 'b') and Matematika >= 60 and indo >= 70 and ing >= 55:
     print ("Kamu lulus")
else:
     print ("Kamu ga lulus")