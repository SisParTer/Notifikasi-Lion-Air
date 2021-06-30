import paho.mqtt.client as mqtt
import os
import json
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
    print("Kode Penerbangan : ",messageObj["kode"])
    print("Asal Pesawat     : ",messageObj["asal"])
    print("Tujuan Pesawat   : ",messageObj["tujuan"])
    print("Jadwal           : ",messageObj["jadwal"])
    print("Jam              : ",messageObj["jam"])
    print("Pesan Dibuat     : ",messageObj["created_at"])

    with open("boarding-"+messageObj["kode"]+".txt", "w") as text_file:
    	print("Kode Penerbangan : ",messageObj["kode"], file=text_file)
    	print("jadwal           : ",messageObj["jadwal"], file=text_file)
    	print("jam              : ",messageObj["jam"], file=text_file)

    with open("lokasi-"+messageObj["kode"]+".txt", "w") as text_file:
    	print("Kode Penerbangan : ",messageObj["kode"], file=text_file)
    	print("Asal Pesawat     : ",messageObj["asal"], file=text_file)
    	print("Tujuan Pesawat   : ",messageObj["tujuan"], file=text_file)


def pub(client,topic,msg,qos):
    client.publish(topic,msg,qos)
def sub(client,topic,qos):
    client.subscribe(topic,qos)

# create client
client = mqtt.Client("ClientSub",clean_session=False)
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

# subscribe to the topic "my/test/topic"
# client.subscribe("my/LionAIR/Notifikasi",1)
sub(client,"my/LionAIR/Notifikasi",1)

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
clearConsole()
client.loop_forever()



