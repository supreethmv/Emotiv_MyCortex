import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

fig, axs = plt.subplots(3,2)



def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
    for eachLine in dataArray:
        if len(eachLine)>1:
            xar.append(int(eachLine.split(',')[0]))
            for i in range(7):
                if i is 2:continue
                yar[i].append(int(float(eachLine.split(',')[i+1])))
    for ax in axs.flat:
        ax.clear()
    for i,row in enumerate(axs):
        for j,col in enumerate(row):
            col.plot(xar,yar[i*len(row)+j])
            col.set_title(str(i)+','+str(j))
    #axs[0,0].plot(xar,yar[0])
    #axs[0,1].plot(xar,yar[1],'tab:orange')
    #axs[1,0].plot(xar,yar[2],'tab:red')
    #axs[1,1].plot(xar,yar[3],'tab:green')
    #axs[2,0].plot(xar,yar[4])
    #axs[2,1].plot(xar,yar[5])

    #axs[0,0].set_title('Metric 1')
    #axs[0,1].set_title('Metric 2')
    #axs[1,0].set_title('Metric 3')
    #axs[1,1].set_title('Metric 4')
    #axs[2,0].set_title('Metric 5')
    #axs[2,1].set_title('Metric 6')
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()