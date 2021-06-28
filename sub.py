import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(" ----- Tersambung ----- ")
    else:
        print("Error connect code : " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("\n Notifikasi Baru Dari LionAIR pada Topic : " + msg.topic + " -> " + msg.payload.decode("utf-8"))

# create client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

MyPas = "Kontol69"

# set username and password
client.username_pw_set("liezarda", MyPas)

# connect to HiveMQ Cloud on port 8883
client.connect("a9643b4ed5f54c57a7c92814ab6df38a.s1.eu.hivemq.cloud", 8883)

# subscribe to the topic "my/test/topic"
client.subscribe("my/LionAIR/Notifikasi")

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()


