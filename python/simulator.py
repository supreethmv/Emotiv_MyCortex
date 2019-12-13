import random
import time

file=open("sampleText.txt","w+")
file.close()
count=0

while True:
    file=open("sampleText.txt","a+")
    file.write(str(count)+","+','.join([str(round(round(random.random(),2)*100,0)) for _ in range(7)])+"\n")
    file.close()
    count+=1
    time.sleep(1)