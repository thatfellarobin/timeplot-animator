import numpy as np
import matplotlib.pyplot as plt
import os

data = np.loadtxt('data.csv',delimiter = ',',skiprows = 1,usecols = [0,1])

# User-inputted parameters
t_start = 2505 # In the same time units as your data
t_end = 2506 # In the same time units as your data
anim_scale = 1 # Scaling for animation speed, ie seconds of animation per data-time unit.
framerate = 30 # frames per second of animation

# Preparing cropped list of x values
t_delta = data[1,0] - data[0,0]
t_domain = t_end - t_start
xs = np.arange(0,t_domain,t_delta)

# Preparing cropped list of y values
t_start_index = int(round((t_start - data[0,0]) / t_delta))
total_num_indices = int(round(t_domain/t_delta)) + 1
t_end_index = t_start_index + total_num_indices
ys = data[t_start_index:t_end_index,1]

num_frames = int(t_domain * framerate * anim_scale)
frame_tstep = 1. / framerate # How much animation-time passes per frame

fig,ax = plt.subplots()

font = {'weight': 'bold',
        'fontname': 'Arial'
        }

for oldFrame in os.listdir('frames'):
    if oldFrame.endswith('.png'):
        os.unlink('frames/' + oldFrame)

print('outputting',num_frames,'frame(s)')

for frame in range(num_frames): # replace range with num_frames when not testing
    ax.cla()

    # Plot properties
    plt.xlabel('Time (s)', fontdict = font)
    plt.ylabel('Thrust (lbf)', fontdict = font)
    plt.title('Thrust versus Time', fontdict = font)
    ax.set_xlim(0, t_end - t_start)
    ax.set_ylim(0, np.ceil(max(ys)/100) * 100)
    ax.grid()

    # Plotting
    frametime = frame_tstep * frame
    frameindex = int(round(frametime / (anim_scale * t_delta)))
    ax.plot(xs[0:frameindex],ys[0:frameindex], 'r', linewidth = 3)

    fig.savefig('frames/frame_' + str(frame) + '.png', dpi = 200)

    print('saved frame',frame)
