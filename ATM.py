print("\tPercobaan Bikin ATM")
print("-------------------------------")
print('1 | Tabung')
print('2 | Tarik Tunai')
print('3 | Cek Saldo')
print("-------------------------------")
kode = int(input('Pilih nomer\t\t:'))
if kode == 1:
    jumlah = int(input('masukan jumlah uang\t:'))
    print('Transaksi Berhasil')
elif kode == 2:
    print('Saldo anda habis')
elif kode == 3:
    print('RP 0')
else:
    print('Pilihan gagal, silahkan coba lagi')
    