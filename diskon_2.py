belanja = int(input("Masukkan Nominal Belanjaan : "))

diskon = 0 #inisialisasi, agar kalau kurang dari 100rb otomatis diskon nya 0

if belanja >= 1_000_000: #nominal paling besar di atas
     diskon = 10/100 * belanja
elif belanja >= 500_000:
     diskon = 5/100 * belanja
elif belanja >= 100_000:
     diskon = 2/100 * belanja

total = belanja - diskon

print (f'''
Harga beli        : {belanja}
Diskon            : {diskon}
Dibayar           : {total}
''') #agar ada jarak nya jangan pake spasi, bisa pake tombol tab atau "\t" (nanti warna nya merah
#karna ini lagi pake themes yang beda )