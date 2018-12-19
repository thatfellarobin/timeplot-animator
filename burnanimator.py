import numpy as np
from scipy import interpolate, signal
import matplotlib.pyplot as plt
import os
from math import factorial

# def savitzky_golay(y, window_size, order, deriv=0, rate=1):
#     try:
#         window_size = np.abs(np.int(window_size))
#         order = np.abs(np.int(order))
#     except ValueError, msg:
#         raise ValueError("window_size and order have to be of type int")
#     if window_size % 2 != 1 or window_size < 1:
#         raise TypeError("window_size size must be a positive odd number")
#     if window_size < order + 2:
#         raise TypeError("window_size is too small for the polynomials order")
#     order_range = range(order+1)
#     half_window = (window_size -1) // 2
#     # precompute coefficients
#     b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
#     m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
#     # pad the signal at the extremes with
#     # values taken from the signal itself
#     firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
#     lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
#     y = np.concatenate((firstvals, y, lastvals))
#     return np.convolve( m[::-1], y, mode='valid')

data = np.loadtxt('data.csv',delimiter = ',',skiprows = 1,usecols = [0,1])

# User-inputted parameters
t_start = 2505 # In the same time units as your data
t_end = 2515 # In the same time units as your data
animation_scale = 1 # Scaling for animation speed, ie seconds of animation per data-time unit.
framerate = 30 # frames per second of animation
run_smooth = False # If your data is noisy, you can use this to make the data smoother
run_interpolate = False # If your data sample rate is low, you can use this to interpolate intermediate values for smoother animation

# Preparing cropped list of x values
t_delta = data[1,0] - data[0,0]
t_domain = t_end - t_start
xs = np.linspace(0,t_domain,num=t_domain/t_delta)

# Preparing cropped list of y values
t_start_index = int(round((t_start - data[0,0]) / t_delta))
t_end_index = t_start_index + len(xs)
ys = data[t_start_index:t_end_index,1]

num_frames = int(t_domain * framerate * animation_scale)
frame_tstep = 1. / framerate # How much animation-time passes per frame

if run_smooth:
    smoothing_window = max(2*len(xs)/num_frames,10)
    # ys = savitzky_golay(ys, window=smoothing_window, order=3)
    ys = signal.savgol_filter(ys, window_length=smoothing_window, polyorder=3)

if run_interpolate:
    f = interpolate.interp1d(xs,ys,kind='quadratic')
    new_xs = np.linspace(0,t_domain,num=num_frames)
    t_delta = new_xs[1] - new_xs[0]
    new_ys = f(new_xs)
    xs = new_xs
    ys = new_ys

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
    animation_time = frame_tstep * frame
    frameindex = int(round(animation_time / (animation_scale * t_delta)))
    ax.plot(xs[0:frameindex],ys[0:frameindex], 'r', linewidth = 3)

    fig.savefig('frames/frame_' + str(frame) + '.png', dpi = 200)

    print('saved frame',frame)
