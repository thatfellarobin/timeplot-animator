import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt

data = np.loadtxt('data.csv',delimiter = ',',skiprows = 1,usecols = [0,5])
data[:,1] = data[:,1]*0.88 # Scaling thrust data because of a weird result

# User-inputted parameters
t_start = 382 # seconds
t_end = 410 # seconds
framerate = 30 # frames per second

t_delta = data[1,0] - data[0,0]
t_domain = t_end - t_start
xs = np.arange(0,t_domain,t_delta)

t_start_index = int(round((t_start - data[0,0]) / t_delta))
total_num_indices = int(round(((t_end - t_start)/t_delta))) + 1
t_end_index = t_start_index + total_num_indices

ys = data[t_start_index:t_end_index,1]
# print(xs)
# print(ys)

num_frames = t_domain * framerate
frame_tstep = 1. / framerate

fig,ax = plt.subplots()


for frame in range(num_frames): # replace range with num_frames
    ax.cla()
    
    # Plot properties
    ax.set(\
        xlabel = 'Time (s)',\
        ylabel = 'Thrust (lbf)',\
        title = 'Thrust versus Time',\
        )
    ax.set_xlim(0, t_end - t_start)
    ax.set_ylim(0, np.ceil(max(ys)/100) * 100)
    ax.grid()
    
    # Plotting
    frametime = frame_tstep * frame
    frameindex = int(round(frametime / t_delta))
    ax.plot(xs[0:frameindex],ys[0:frameindex], 'r', linewidth = 3)
    
    # Line properties


    fig.savefig('frames/frame_' + str(frame) + '.png')

    print('saved frame',frame)






