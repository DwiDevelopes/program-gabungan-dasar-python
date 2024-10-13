print ("Menu :")
print ("1. Harga Nasi Goreng : Rp.10.000")
print ("2. Harga Ketoprak : Rp.8.000")
print ("3. Harga Teh Botol : Rp.5.000")
print ("4. Harga Nasi Uduk : Rp.12.000")

pilihkarakterwuwa =  int(input("Pilih Daftar Harga nya : ( Pilih Nomor 1 2 3 Dan 4 )"))

harga = 0 
if pilihkarakterwuwa == 1 :
 harga = 10000

if pilihkarakterwuwa == 2 :
 harga = 8000

if pilihkarakterwuwa == 3 :
 harga = 5000

if pilihkarakterwuwa == 4 :
 harga = 12000
 
else :
    print ("Tidak boleh melebihi yang ada di pilihan menu ")

print ("hasil yang di pilih adalah : ", harga)
