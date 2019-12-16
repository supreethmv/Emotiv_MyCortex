import paho.mqtt.client as mqtt #import the client1
import time

################################################

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    print("\n\n----------------------------------------")

################################################

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

########################################

broker_address="broker.hivemq.com"
topic="Topic_of_your_choice"


print("creating new instance with name 'Consumer'")
client = mqtt.Client("Consumer") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","Topic_of_your_choice")
client.subscribe(topic)
time.sleep(100) # wait
client.loop_stop() #stop the loop