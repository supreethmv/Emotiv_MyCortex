import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

fig, axs = plt.subplots(6)


def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
    for eachLine in dataArray:
        if len(eachLine)>1:
            xar.append(int(eachLine.split(',')[0]))
            for i in range(6):
                yar[i].append(int(float(eachLine.split(',')[i+1])))
    for i in range(6):
        axs[i].clear()
        axs[i].plot(xar,yar[i])
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()