import paho.mqtt.client as mqtt
import os
import datetime
import sys
import json
import time

# Function dari Import
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# ----------------------------------- SETUP HIVE MQ CLOUD -----------------------------------

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(" ----- Tersambung dengan client ----- ")
    else:
        print("Error connect code : " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

def pub(client,topic,msg,qos):
    client.publish(topic,msg,qos)
def sub(client,topic,qos):
    client.subscribe(topic,qos)

# create the client
client = mqtt.Client("ClientPub",clean_session=False)
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

MyPas = "Kntl6969"
MyUser = "liezarda"

# set username and password
client.username_pw_set(MyUser, MyPas)

# connect to HiveMQ Cloud on port 8883
client.connect("a9643b4ed5f54c57a7c92814ab6df38a.s1.eu.hivemq.cloud", 8883)



# ---------------- Fungsi-Fungsi Untuk Main Program --------------------------

import uICLI

def resetConn():
	client.disconnect()
	client.connect("a9643b4ed5f54c57a7c92814ab6df38a.s1.eu.hivemq.cloud", 8883)


# Fungsi untuk Cek Asal dan Tujuan Pesawat
def cekAsal(Asal,Tujuan):
	if ((Asal == Tujuan) or (Asal == "") or (Tujuan == "")):
		return False
	else:
		return True

# Fungsi untuk Cek Kode Penerbangan
def cekKodePenerbangan(kode):
	# global kodeSession
	message = ""
	if ((len(kode) > 4) or (len(kode) < 4) or (kode.isnumeric() == False)):
		message = "Kode Penerbangan harus berjumlah 4 Digit dan Bertipe Numerik!"
		return False,message
	else:
		kodeDalem = "JT "+kode
		if kodeDalem in kodeSession:
			message = "Kode Penerbangan Telah Di-Notifikasikan!"
			return False,message
		else:
			return True,message
	return True,message

# Switch Kode Kota
def switchKodeKota(inputan):
	switcher = {
        '1': "Bandung (B.Husein Sastranegara)",
        '2': "Surabaya (B.Juanda)",
        '3': "jakarta (B.Halim Perdanakusuma)",
        '4': "Tanggerang (B.Soekarno-Hatta)",
        '5': "Bali (B.Ngurah Rai)",
        '6': "Makassar (B.Sultan Hasanuddin)",
        '7': "Palembang (B.Sultan Mahmud Badarudin)",
        '8': "Batam (B.Hang Nadim)",
        '9': "Medan (B.Kualanamu)",
        '10': "Mataram (B.Lombok)",       
    }
	return switcher.get(inputan, "")

def cekTanggal(tanggal):
	if (tanggal > 0) and (tanggal <= 31):
		return True
	else:
		return False

def cekBulan(bulan):
	if (bulan > 0) and (bulan <= 12):
		return True
	else:
		return False

def convertTanggal(tanggal, bulan):
	d = datetime.datetime(2021, bulan, tanggal)
	return '{:%Y-%m-%d}'.format(d)

def convertJam(jam, menit):
	j = datetime.time(jam,menit)
	return '{:%H:%M}'.format(j)

# Fungsi untuk Cek Tanggal dan bulan untuk jadwal
def cekJadwal(date_string):
	status = True
	format = '%Y-%m-%d'
	try:
		datetime.datetime.strptime(date_string,format)
	except ValueError:
		status = False
	return status

def cekJam(date_string):
	status = True
	format = '%H:%M'
	try:
		datetime.datetime.strptime(date_string,format)
	except ValueError:
		status = False
	return status


# Input Nomor Penerbangan
def inputKodePenerbangan():
	
	uICLI.header()
	print('Contoh : "3704" (4 Digit angka bertipe Numerik)')
	KodePenerbangan = input("Masukan Kode Penerbangan : ")
	status, message = cekKodePenerbangan(KodePenerbangan)
	while (status == False):
		print('Input Salah : ')
		print("\n",message)
		print('\n')
		KodePenerbangan = input("Masukan Kode Penerbangan : ")
		status, message = cekKodePenerbangan(KodePenerbangan)
	KodePenerbangan = 'JT '+KodePenerbangan
	return KodePenerbangan
# Input Kota Asal dan Tujuan Penerbangan
def inputKota():
	# Input Kota Asal Pesawat
	uICLI.kotaAsal()
	inputan = input("Masukan Kode Kota Asal : ")
	Asal = switchKodeKota(inputan)
	
	# Input Kota Tujuan Pesawat
	uICLI.kotaTujuan()
	inputan = input("Masukan Kode Kota Tujuan : ")
	Tujuan = switchKodeKota(inputan)

	# Cek input
	while (cekAsal(Asal,Tujuan) == False):
		print(Asal,' - ',Tujuan,'\n')
		uICLI.kotaTujuan()
		print('Asal dan Tujuan tidak boleh sama atau kosong! \n')
		print('Input Anda : ')
		print('Asal = ',Asal) 
		print('Tujuan = ',Tujuan)
		print(uICLI.footer())
		inputan = input("Masukan Kode Kota Asal : ")
		Asal = switchKodeKota(inputan)
		inputan = input("Masukan Kode Kota Tujuan : ")
		Tujuan = switchKodeKota(inputan)
	return Asal, Tujuan

# Input Jadwal Penerbangan
def inputJadwal():
	clearConsole()
	uICLI.header()
	print('Contoh : "12" (Tanggal 12)')
	Tanggal = int(input('Masukan Tanggal : '))
	while not cekTanggal(Tanggal):
		clearConsole()
		uICLI.header()
		print('Masukan Salah')
		Tanggal = int(input('Masukan Tanggal : '))
	print('Contoh : "10" (Bulan Oktober)')
	Bulan = int(input('Masukan Bulan : '))
	while not cekBulan(Bulan):
		clearConsole()
		uICLI.header()
		print('Masukan Salah')
		Bulan = int(input('Masukan Bulan : '))
	# Convert ke datetime format
	date_string = convertTanggal(Tanggal,Bulan)
	clearConsole()
	while (cekJadwal(date_string) == False):
		clearConsole()
		uICLI.header()
		print("Masukan Anda Salah")
		Tanggal = int(input('Masukan Tanggal (dd) : '))
		Bulan = int(input('Masukan Bulan (mm) : '))
		date_string = convertTanggal(Tanggal,Bulan)
	return date_string

def inputJamPenerbangan():
	clearConsole()
	uICLI.header()
	Jam = int(input("Masukan Jam Penerbangan (Format 0-23) : "))
	Menit = int(input("Masukan Menit Penerbangan (Format 00 - 59) : "))
	date_string = convertJam(Jam,Menit)
	clearConsole()
	while (cekJam(date_string) == False):
		clearConsole()
		uICLI.header()
		print("Masukan Anda Salah")
		Jam = int(input("Masukan Jam Penerbangan Format 00-23 (Contoh '19' (Jam 7 Malam)) : "))
		Menit = int(input("Masukan Menit Penerbangan Format 00 - 59 (Contoh '45' (Jam 7.45 Malam)) : "))
		date_string = convertJam(Jam,Menit)
	return date_string

# Input Semua Data Penerbangan
def inputPenerbangan():
	# Kompilasi semua inputan
	clearConsole()
	
	KodePenerbangan = inputKodePenerbangan()
	Asal, Tujuan = inputKota()
	Jadwal = inputJadwal()
	Jam = inputJamPenerbangan()

	return KodePenerbangan, Asal, Tujuan, Jadwal, Jam


def formatJsonNotifikasi(kode,asal,tujuan,jadwal,jam):
	now = datetime.datetime.now()

	jsonData = {"kode":kode,
				 "asal":asal,
				 "tujuan":tujuan,
				 "jadwal":jadwal,
				 "jam":jam,
				 "created_at":now.strftime("%d/%m/%Y %H:%M:%S")
				 }
	
	return jsonData

# Get Pesan Notifikasi pada session sekarang
def getNotifikasi():
	global arrMessageObj
	print("Ada "+str(len(arrMessageObj))+" Notifikasi Pada Session ini ")
	for i in arrMessageObj:
		print("Pesan Dibuat     : ",i["created_at"])
		print("Kode Penerbangan : ",i["kode"])
		print("Asal Pesawat     : ",i["asal"])
		print("Tujuan Pesawat   : ",i["tujuan"])
		print("Jadwal           : ",i["jadwal"])
		print("Jam              : ",i["jam"])
		print("--------------------------------------------------------")
	input("\nOk ...")

# Fungsi Untuk Menu di Main Program

def switchMenu(inputan):
	if inputan=='1':
		mainProg()
	elif inputan=='2':
		getNotifikasi()
	else:
		inputan=='99'

def mainProg():
	global kodeSession
	global arrMessageObj
	KodePenerbangan, Asal, Tujuan, Jadwal, Jam = inputPenerbangan()
	uICLI.header()
	print('Apakah Input Anda Sudah Benar?')
	print('Kode   : ', KodePenerbangan)
	print('Asal   : ', Asal)
	print('Tujuan : ', Tujuan)
	print('Jadwal : ', Jadwal)
	print('Pukul  : ', Jam)
	inputan = input("(n) untuk Cancel, Enter jika sudah benar : ")
	if (inputan == 'n'):
		KodePenerbangan = ''
		Asal = ""
		Tujuan = ""
		Jam = ""
		print('Publish Notifikasi Dibatalkan')
	else:
		payload = formatJsonNotifikasi(KodePenerbangan,Asal,Tujuan,Jadwal,Jam)
		arrMessageObj.append(payload)
		kodeSession.append(KodePenerbangan)
		data_out=json.dumps(payload)
		pub(client,"my/LionAIR/Notifikasi",data_out,1)
		print('Notifikasi Berhasil Dikirimkan')
		time.sleep(2)
		

# ----------------------------------- MAIN -----------------------------------

kodeSession = [] # Bertipe Array untuk mengecek apakah Kode Penerbangan telah diinputkan
arrMessageObj = []	# Bertipe Array Of Object
clearConsole()
uICLI.menuPub()
menuInput = input("Silahkan Masukan Input : ")
while (menuInput != '0'):
	resetConn()
	switchMenu(menuInput)
	uICLI.menuPub()
	menuInput = input("Silahkan Masukan Input : ")
print("	. . . Exit")
sys.exit()
