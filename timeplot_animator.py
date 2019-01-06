from pltanim_func import *
import tkinter as tk
import os
from matplotlib import pyplot as plt  # https://github.com/MTG/sms-tools/issues/36
import numpy as np
from scipy import interpolate, signal
import matplotlib
matplotlib.use("TkAgg")

root = tk.Tk()
run_smooth = tk.IntVar()
run_interpolate = tk.IntVar()

root.title('Timeplot Animator')

# General Parameters
param_frame = tk.Frame(root)
param_frame.grid(row=0, column=0)
param_label = tk.Label(param_frame,
                       text='General Parameters',
                       font='Helvetica 16 bold',
                       width=40,  # Not sure why I need the width to left justify
                       anchor=tk.W)
t_start_label = tk.Label(param_frame, text='Start Time (data units)')
t_start_field = tk.Entry(param_frame)
t_end_label = tk.Label(param_frame, text='End Time (data units)')
t_end_field = tk.Entry(param_frame)
anim_scale_label = tk.Label(param_frame, text='Animation Scale')
anim_scale_field = tk.Entry(param_frame)
framerate_label = tk.Label(param_frame, text='Animation Framerate')
framerate_field = tk.Entry(param_frame)

param_label.grid(row=0, column=0, columnspan=2)  # Not working as expected
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
smoothing_label = tk.Label(smoothing_frame,
                           text='Smoothing',
                           font='Helvetica 16 bold',
                           width=40,  # Not sure why I need the width to left justify
                           anchor=tk.W)
smoothing_check = tk.Checkbutton(smoothing_frame, text='Apply Smoothing', variable=run_smooth)

smoothing_label.grid(row=0, column=0, sticky='W')  # Not working as expected
smoothing_check.grid(row=1, column=0)

# Interpolation
interp_frame = tk.Frame(root)
interp_frame.grid(row=2, column=0)
interp_label = tk.Label(interp_frame,
                        text='Interpolation',
                        font='Helvetica 16 bold',
                        width=40,  # Not sure why I need the width to left justify
                        anchor=tk.W)
interp_check = tk.Checkbutton(interp_frame, text='Apply Interpolation', variable=run_interpolate)

interp_label.pack(anchor=tk.W)  # Not working as expected
interp_check.pack()

# Graph Preview
preview_frame = tk.Frame(root)
preview_label = tk.Label(preview_frame,
                         text='Plot Preview (final frame)',
                         font='Helvetica 16 bold',
                         width=50,
                         anchor=tk.N)

preview_frame.grid(row=0, column=1, rowspan=3, sticky=tk.N)
preview_label.pack(fill='y')  # Not working as expected

# Execution
execution_frame = tk.Frame(root)
preview_button = tk.Button(execution_frame,
                           text='Generate Plot Preview')
execution_button = tk.Button(execution_frame,
                             text='Generate Animation',
                             command=lambda: plotting_execution(t_start_field, t_end_field, anim_scale_field, framerate_field, run_smooth, run_interpolate))

execution_frame.grid(row=3, column=0, columnspan=2)
preview_button.grid(row=0, column=0, padx=5, pady=5)
execution_button.grid(row=0, column=1, padx=5, pady=5)

tk.mainloop()

for i in range(9):
    pass

# TODO eventually:
# - explanation under each section label
# - Organize frames by grid, with proper sizing
# - Figure out how to use field entries
# - Data preview?
