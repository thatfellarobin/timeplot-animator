import numpy as np
from scipy import interpolate, signal
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt # https://github.com/MTG/sms-tools/issues/36
import os
import tkinter as tk
from plot_anim_functions import *

root = tk.Tk()

t_start = tk.DoubleVar() # In the same time units as your data
t_end = tk.DoubleVar() # In the same time units as your data
animation_scale = tk.DoubleVar() # Scaling for animation speed, ie seconds of animation per data-time unit.
framerate = tk.DoubleVar() # frames per second of animation
run_smooth = tk.IntVar() # If your data is noisy, you can use this to make the data smoother
run_interpolate = tk.IntVar() # If your data sample rate is low, you can use this to interpolate intermediate values for smoother animation
graph_title = tk.StringVar()
graph_ylabel = tk.StringVar()
graph_xlabel = tk.StringVar()

root.title('Timeplot Animator')

# General Parameters
param_frame = tk.Frame(root)
param_frame.grid(row=0,column=0)
param_label = tk.Label(param_frame, text='General Parameters', width=40)
t_start_label = tk.Label(param_frame, text='Start Time (data units)')
t_start_field = tk.Entry(param_frame)
t_end_label = tk.Label(param_frame, text='End Time (data units)')
t_end_field = tk.Entry(param_frame)
anim_scale_label = tk.Label(param_frame, text='Animation Scale')
anim_scale_field = tk.Entry(param_frame)
framerate_label = tk.Label(param_frame, text='Animation Framerate')
framerate_field = tk.Entry(param_frame)

param_label.grid(row=0, column=0, columnspan=2, sticky=tk.W) # Not working as expected
t_start_label.grid(row=1, column=0, sticky=tk.W)
t_start_field.grid(row=1, column=1)
t_end_label.grid(row=2, column=0, sticky=tk.W)
t_end_field.grid(row=2, column=1)
anim_scale_label.grid(row=3, column=0, sticky=tk.W)
anim_scale_field.grid(row=3, column=1)
framerate_label.grid(row=4, column=0, sticky=tk.W)
framerate_field.grid(row=4, column=1)

# Smoothing
smoothing_frame = tk.Frame(root)
smoothing_frame.grid(row=1, column=0)
smoothing_label = tk.Label(smoothing_frame, text='Smoothing')
smoothing_check = tk.Checkbutton(smoothing_frame,text='Apply Smoothing',variable=run_smooth)

smoothing_label.pack(anchor=tk.W) # Not working as expected
smoothing_check.pack()

# Interpolation
interp_frame = tk.Frame(root)
interp_frame.grid(row=2, column=0)
interp_label = tk.Label(interp_frame, text='Interpolation')
interp_check = tk.Checkbutton(interp_frame,text='Apply Interpolation',variable=run_interpolate)

interp_label.pack(anchor=tk.W) # Not working as expected
interp_check.pack()

# Graph Preview
preview_frame = tk.Frame(root)
preview_frame.grid(row=0, column=1, rowspan=3)
preview_label = tk.Label(preview_frame, text='Plot Preview (final frame)')

preview_label.pack()

# Execution
execution_frame = tk.Frame(root)
execution_button = tk.Button(execution_frame, text='Generate Animation', command=test)

execution_frame.grid(row=3, column=0, columnspan=2)
execution_button.pack()

tk.mainloop()

# TODO eventually:
# - explanation under each section label
# - Organize frames by grid, with proper sizing
# - Figure out how to use field entries
# - Data preview?
