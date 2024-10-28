import sys

print("\t===== Kasus 2 =====")

masuk = int(input("Masukkan jam masuk (1-12) \t : "))
if masuk > 12:
    print ("Jam tidak boleh lebih dari 12") 
    sys.exit()

keluar = int(input("Masukkan jam masuk (1-12) \t : "))
if keluar < 1:
    print ("Jam tidak boleh lebih dari 12") 
    sys.exit()

total = keluar - masuk

if total <0:
    total += 12

if total <=2:
   biaya = 2000
else:
    biaya = 2000 + (total - 2) * 500

print(f"Total parkir : {total} jam")

print (f"Total Biaya parkir : RP {biaya}")