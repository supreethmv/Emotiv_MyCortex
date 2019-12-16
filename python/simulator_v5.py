import paho.mqtt.client as mqtt
import random
import time

file=open("sampleText.txt","w+")
file.close()
count=0

broker_address="broker.hivemq.com"
topic="Topic_of_your_choice"

print("creating new instance with name 'Producer'")
client = mqtt.Client("Producer")
print("connecting to broker")
client.connect(broker_address)
client.loop_start()
print("Publishing message to topic",topic)
n=50
while n:
    file=open("sampleText.txt","a+")
    junk=str(count)+",{\"met\":[false,"+str(random.random())+",false,"+str(random.random())+",0.0,false,"+str(random.random())+",false,"+str(random.random())+",false,"+str(random.random())+",false,"+str(random.random())+"],\"sid\":\"de918bb5-aab5-4e9f-89a7-fb51ab368016\",\"time\":1575903661.5274}\n"
    file.write(junk)
    client.publish(topic,junk)
    print("Published",junk)
    file.close()
    count+=1
    time.sleep(1)
    n-=1


client.loop_stop()
client.disconnect()