def tambah(x, y):
    return x + y 

def kurang(x, y):
    return x - y 
  
def kali(x, y):
    return x * y 
  
def bagi (x, y):
  if y == 0:
    print("Tak Terdefinisi")
  
  else:
   return x / y
  
print("pilih opsi :")
print("1. pertambahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")

pilihan = input("pilih opsi 1/2/3/4 :")

angka1 = float(input("Angka kesatu :"))
angka2 = float(input("angka kedua :"))
  
if pilihan =="1":
    print("Hasil :", tambah(angka1, angka2))
elif pilihan =="2":
    print("Hasil :", kurang(angka1, angka2))
elif pilihan == "3":
   print("Hasil :", kali(angka1, angka2))
elif pilihan == "4":
    print("Hasil :", bagi(angka1, angka2))
else :
  print("Opsi Tak Ditemukan 😭") 
