import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
import json

fig, axs = plt.subplots(3,2)

def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    x = []
    y = {'eng':[],'exc':[],'lex':[],'str':[],'rel':[],'int':[],'foc':[]}
    for eachLine in dataArray:
        if len(eachLine)>1:
            x.append(int(eachLine.split(',')[0]))
            eeg_json = json.loads(','.join(eachLine.split(',')[1:]))
            y['engIsActive']=eeg_json["met"][0]
            y['eng'].append(eeg_json["met"][1])
            y['excIsActive']=eeg_json["met"][2]
            y['exc'].append(eeg_json["met"][3])
            y['lex'].append(eeg_json["met"][4])
            y['strIsActive']=eeg_json["met"][5]
            y['str'].append(eeg_json["met"][6])
            y['relIsActive']=eeg_json["met"][7]
            y['rel'].append(eeg_json["met"][8])
            y['intIsActive']=eeg_json["met"][9]
            y['int'].append(eeg_json["met"][10])
            y['focIsActive']=eeg_json["met"][11]
            y['foc'].append(eeg_json["met"][12])
    for ax in axs.flat:
        ax.clear()
    #for i,row in enumerate(axs):
    #    for j,col in enumerate(row):
    #        col.plot(x,y[i*len(row)+j])
    #        col.set_title(str(i)+','+str(j))
    axs[0,0].plot(x,y['eng'],'tab:grey')
    axs[0,1].plot(x,y['exc'],'tab:orange')
    axs[1,0].plot(x,y['str'],'tab:purple')
    axs[1,1].plot(x,y['rel'],'tab:green')
    axs[2,0].plot(x,y['int'],'tab:cyan')
    axs[2,1].plot(x,y['foc'],'tab:blue')

    axs[0,0].set_title('Engagement'+str(y['engIsActive']))
    axs[0,1].set_title('Excitement'+str(y['excIsActive']))
    axs[1,0].set_title('Stress'+str(y['strIsActive']))
    axs[1,1].set_title('Relaxation'+str(y['relIsActive']))
    axs[2,0].set_title('Interest'+str(y['intIsActive']))
    axs[2,1].set_title('Focus'+str(y['focIsActive']))
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()