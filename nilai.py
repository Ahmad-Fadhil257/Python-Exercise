nilai = int(input("Masukkan inputan nilai : "))

if nilai >= 90 and nilai <= 100:
     print ("Nilai [A]")
elif nilai >= 80:
     print ("Nilai [B]")
elif nilai >= 70:
     print ("Nilai [C]")
elif nilai >= 60:
     print ("Nilai [D]")
elif nilai <60:
     print ("Nilai [E]")
else:
     print ("Inputan salah")