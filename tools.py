import os
os.system('clear')

print ("=========================")
print ("Welcome To The This Tools") #gausah so asik di ubah ubah ya anjing
print ("dev tools by : hazz")
print ("GUNAKAN TOOLS INI DENGAN BIJAK!!")
print ("=========================")

def main ():
	print ("SILAHKAN PILIH TOOLS")
	print ("1. Modul Pyhton")
	print ("2. Modul WebDev")
	print ("3. keluar")
	
	Pilihan = input ("masukan pilihan : ")
	
	if Pilihan == "1":
		sandi = input ("silahkan masukan sandi untuk mengakses : ")
		if sandi == "31":
			print()
			print ("https://github.com/novalagung/dasarpemrogramanpython/raw/ebooks/dasarpemrogramanpython.pdf?v=beta1.20231011")
			print ()
			print ("copas aja bang buka di browser")
		else:
			print("\nsandi salah!! program dihentikan")
			exit()
			
	elif Pilihan == "2":
		sandi = input ("silahkan masukan kata kunci untuk mengakses : ")
		if sandi == "31":
			print()
			print ("https://repository.bsi.ac.id/index.php/unduh/item/242521/cover-dan-isi-lengkap-web-pro.pdf")
			print()
			print("copas buka di chrome terus klik titik 3 lalu download")
		else:
			print("\nkata kunci salah!! program dihentikan")
			exit()
		
	elif Pilihan == "3":
		print()
		print ("Good Bye!!")
		print ()
		
	else :
		print ("ngetik apaan sih bang")
		print ()
	
if __name__ == "__main__" :
	main ()
