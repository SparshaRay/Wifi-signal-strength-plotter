import os                                   # for running iwconfig
import matplotlib.pyplot as plt             # ubiquitous library
import matplotlib.animation as animation    # for animating

plt.style.use('dark_background')            # looks cool

fig = plt.figure()                          
ax = plt.axes(xlim=(0, 300), ylim=(-100, 0)) 
ax.get_xaxis().set_visible(False)
plt.ylabel('dBW')
line, = ax.plot([], [], lw=2) 

xdata, ydata = range(300), [0 for i in range(300)]      # making arrays to store data, xdata is just the time array, ydata stores signal strength values

def init(): 
	line.set_data([], []) 
	return line, 

def animate(i): 
    while (output := os.popen('iwconfig wlo1').read().split('\n')[5].split()[3][6:]) == '0' : ()        # os.popen gets the output of iwconfig of wlo1 (wireless network) interface ...
                                                                                                        # ... which is parsed to get the signal strength ...
                                                                                                        # ... and this whole thing is run again and again until a nonzero value appears
                                                                                                        # idk what was i thinking when i wrote this absolutely unreadable museum piece
    ydata.pop(0)                                            # remove oldest value
    ydata.append(sum([*ydata[-5:], int(output)])/6)         # append new value through this "low pass" filter that my melting sanity cooked up at 4am
    line.set_data(xdata, ydata)                             # set data
    return line,                                            # return data
	
 
anim = animation.FuncAnimation(fig, animate, init_func=init, interval=1000/90, blit=True)  # create animation
plt.grid()  # gridsss
plt.show()  # vibe check