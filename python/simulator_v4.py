import random
import time

file=open("sampleText.txt","w+")
file.close()
count=0

while True:
    file=open("sampleText.txt","a+")
    file.write(str(count)+",{\"met\":[false,"+str(random.random())+",false,"+str(random.random())+",0.0,false,"+str(random.random())+",false,"+str(random.random())+",false,"+str(random.random())+",false,"+str(random.random())+"],\"sid\":\"de918bb5-aab5-4e9f-89a7-fb51ab368016\",\"time\":1575903661.5274}\n")
    file.close()
    count+=1
    time.sleep(1)