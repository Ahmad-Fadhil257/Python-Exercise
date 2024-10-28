bulan = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Otober','November','Desember']


print(bulan[2],bulan[9])

bulan[7] = 'August'
bulan[0] = 'January'

bulan.append ('Muharram')

for nomer,y in enumerate(bulan):
     # print(x+1,'.',y)
     print(f'Bulan ke-{nomer+1} {y}')

     #bikin list nama dan list nilai sesuai , terbesar, rata - rata, terkecil