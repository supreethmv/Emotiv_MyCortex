import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

mqtt.Client.connected_flag=False
broker_address="broker.hivemq.com"
print("creating new instance with name 'Producer'")
client = mqtt.Client("Producer")
#client.on_connect=on_connect
print("connecting to broker")
client.connect(broker_address)
client.loop_start()
#while not client.connected_flag: #wait in loop
#    print("Waiting for the connection with the Broker")
#    time.sleep(1)
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","some nonsense")
client.loop_stop()   
client.disconnect() 