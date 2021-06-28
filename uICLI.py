
# Clear Console Function

import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')



# UI
def header():
	print('------------------------- Sistem Notifikasi Lion Air -------------------------')
def footer():
	print('------------------------------------------------------------------------------')

def hasilInputKode(kode):
	print('Kode Penerbangan : ',kode)

def kotaAsal():
	clearConsole()
	header()
	print('>>>>> Silahkan pilih Kota Asal Pesawat')
	print('	(1). Bandung')
	print('	(2). Surabaya')
	print('	(3). Jakarta')
	footer()

def kotaTujuan():
	clearConsole()
	header()
	print('>>>>> Silahkan pilih Kota Tujuan Pesawat')
	print('	(1). Bandung')
	print('	(2). Surabaya')
	print('	(3). Jakarta')
	footer()
