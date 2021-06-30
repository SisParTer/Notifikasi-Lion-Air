
# Clear Console Function

import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')



# UI
def header():
	print('------------------------- Sistem Notifikasi Lion Air -------------------------')
def footer():
	print('------------------------------------------------------------------------------')

def menu():
	clearConsole()
	header()
	print('>>>>> Silahkan pilih Menu Aplikasi')
	print('	(1). Tambah Notifikasi')
	print('	(2). Lihat Notifikasi Pada Session Ini')
	print('	(0). Keluar')
	footer()


def hasilInputKode(kode):
	print('Kode Penerbangan : ',kode)

def kotaAsal():
	clearConsole()
	header()
	print('>>>>> Silahkan pilih Kota Asal Pesawat')
	print('	(1). Bandung (B.Husein Sastranegara)')
	print('	(2). Surabaya (B.Juanda)')
	print('	(3). Jakarta (B.Halim Perdanakusuma)')
	print('	(4). Tanggerang (B.Soekarno-Hatta)')
	print('	(5). Bali (B.Ngurah Rai)')
	print('	(6). Makassar (B.Sultan Hasanuddin)')
	print('	(7). Palembang (B.Sultan Mahmud Badarudin)')
	print('	(8). Batam (B.Hang Nadim)')
	print('	(9). Medan (B.Kualanamu)')
	print('	(10). Mataram (B.Lombok)')
	footer()

def kotaTujuan():
	clearConsole()
	header()
	print('>>>>> Silahkan pilih Kota Tujuan Pesawat')
	print('	(1). Bandung (B.Husein Sastranegara)')
	print('	(2). Surabaya (B.Juanda)')
	print('	(3). Jakarta (B.Halim Perdanakusuma)')
	print('	(4). Tanggerang (B.Soekarno-Hatta)')
	print('	(5). Bali (B.Ngurah Rai)')
	print('	(6). Makassar (B.Sultan Hasanuddin)')
	print('	(7). Palembang (B.Sultan Mahmud Badarudin)')
	print('	(8). Batam (B.Hang Nadim)')
	print('	(9). Medan (B.Kualanamu)')
	print('	(10). Mataram (B.Lombok)')
	footer()
