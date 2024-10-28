print('==========================')
print('Program mengkonversi detik')
print('==========================')

DETIK_MENIT = 60
DETIK_JAM = 60 * 60
DETIK_HARI = 60 * 60 * 24

detik = int(input('Masukkan jumlah detik : '))

hari = int(detik / DETIK_HARI)
detik = detik % DETIK_HARI

jam = int(detik / DETIK_JAM)
detik = detik % DETIK_JAM

menit = int(detik / DETIK_MENIT)
detik = detik % DETIK_MENIT

print(f'Hasilnya adalah : {hari} hari {jam} jam {menit} menit {detik} detik')