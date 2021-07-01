import paho.mqtt.client as mqtt
import os
import json
import time
import uICLI as uI
from threading import Thread
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

import requests

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(" ----- Tersambung dengan client ----- ")
    else:
        print("Error connect code : " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    print("\n>>>>> Notifikasi Baru Dari LionAIR pada Topic : " + msg.topic)
    jsonData = msg.payload.decode("utf-8")
    messageObj = json.loads(jsonData)
    if cekKode(messageObj["kode"]):
    	print("Notifikasi Masuk dengan Kode Penerbangan : "+messageObj["kode"])
    	print("Kode Penerbangan Telah Tersedia")
    	time.sleep(4)
    	client.disconnect()
    else:
	    print("Kode Penerbangan : ",messageObj["kode"])
	    print("Asal Pesawat     : ",messageObj["asal"])
	    print("Tujuan Pesawat   : ",messageObj["tujuan"])
	    print("Jadwal           : ",messageObj["jadwal"])
	    print("Jam              : ",messageObj["jam"])
	    print("Pesan Dibuat     : ",messageObj["created_at"])

	    with open("output/boarding-"+messageObj["kode"]+".txt", "w") as text_file:
	    	print("Kode Penerbangan : ",messageObj["kode"], file=text_file)
	    	print("jadwal           : ",messageObj["jadwal"], file=text_file)
	    	print("jam              : ",messageObj["jam"], file=text_file)

	    with open("output/lokasi-"+messageObj["kode"]+".txt", "w") as text_file:
	    	print("Kode Penerbangan : ",messageObj["kode"], file=text_file)
	    	print("Asal Pesawat     : ",messageObj["asal"], file=text_file)
	    	print("Tujuan Pesawat   : ",messageObj["tujuan"], file=text_file)

	    print(">>> File Baru Ditambahkan : ")
	    print("boarding-"+messageObj["kode"]+".txt & lokasi-"+messageObj["kode"]+".txt didalam Folder /output")

	    global arrMessageObj
	    arrMessageObj.append(messageObj)

def cekKode(kodePenerbangan):
	global arrMessageObj
	for i in arrMessageObj:
		if kodePenerbangan in i["kode"]:
			return True
		else:
			return False

# Fungsi Publish Subscribe

def pub(client,topic,msg,qos):
    client.publish(topic,msg,qos)
def sub(client,topic,qos):
    client.subscribe(topic,qos)

# --------------------- create client --------------
client = mqtt.Client("ClientSub1",clean_session=False)
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)


# ------------------- Untuk Main --------------------

arrMessageObj = [] # Array untuk menyimpan Object Pesan Notifikasi pada Session Ini

MyPas = "Kntl6969"
MyUser = "liezarda"

# set username and password
client.username_pw_set(MyUser, MyPas)

# connect to HiveMQ Cloud on port 8883
client.connect("a9643b4ed5f54c57a7c92814ab6df38a.s1.eu.hivemq.cloud", 8883)

# client subscribe
sub(client,"my/LionAIR/Notifikasi",1)

def inputStop():
	input()
	client.disconnect()
	uI.menuSub()

def loopForever():
	client.connect("a9643b4ed5f54c57a7c92814ab6df38a.s1.eu.hivemq.cloud", 8883)
	clearConsole()
	client.loop_forever()
	# client Disconnected ketika menerima Notifikasi Baru, trigger di on_message, disconnected di inputStop()

def fetchNotifikasi():
	Thread(target = loopForever).start()
	Thread(target = inputStop).start()

# Paralel Thread agar tidak Blocking oleh si loop forevernya
def switchMenu(inputan):
	if inputan=='1':
		fetchNotifikasi()
	elif inputan=='2':
		getNotifikasi()
	else:
		inputan=='69'

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

# --------------------- Main -------------------------

uI.menuSub()
menuInput = input("Silahkan Pilih Mode Notifikasi : ")
while (menuInput != '0'):
	switchMenu(menuInput)
	uI.menuSub()
	menuInput = input("Silahkan Pilih Mode Notifikasi : ")
	




