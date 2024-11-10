inputan = int(input("Masukkan jumlah perkalian : "))

print("*",end="\t")
for a in range (1, inputan + 1):
     print(a,end="\t")
print()

for a in range(1,inputan + 1):
     print(a,end="\t")
     for b in range(1,inputan + 1):
          print(a * b,end= "\t")
     print()