import sys #untuk memfungsikan system

print("\t===== Kasus 1 =====")
jam_masuk = int(input("Masukkan jam masuk (1-12)\t: "))

if jam_masuk > 12:
    print("Jam tidak boleh lebih dari 12.")
    sys.exit() #jadi kalau jam masuk nya lebih dari 12 inputannya berhenti, tapi kalau engga inputannya lanjut

jam_pulang = int(input("Masukkan jam keluar (1-12)\t: "))

if jam_pulang < 1:
    print("Jam tidak boleh kurang dari 1")
    sys.exit() #ini juga sama

lama_jam = jam_pulang - jam_masuk

if lama_jam < 0: 
    lama_jam += 12

print(f"Lama bekerja: {lama_jam} jam") 