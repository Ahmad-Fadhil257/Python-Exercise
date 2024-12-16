text = input("Masukkan kalimat : ")

doubled_text = ''.join(char * 2 for char in text)

print(f"Teks asal: {text}")
print(f"Teks setelah huruf digandakan: {doubled_text}")
