print('==========================')
print('Program mengkonversi hari')
print('==========================')

hari_bulan = 30
hari_tahun = 365

hari = int(input('Masukkan jumlah hari : '))

tahun = int(hari / hari_tahun)
hari = hari % hari_tahun

bulan = int(hari / hari_bulan)
hari = hari % hari_bulan

print (f"Hasilnya adalah : {tahun} tahun {bulan} bulan {hari} hari")