import numpy as np
from scipy import interpolate, signal
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt # https://github.com/MTG/sms-tools/issues/36
import os
import tkinter as tk

def test():
    print('testing testing!')

def numorder(n): # Finds the order of magnitude of a number
    number = abs(n)
    if n == 0:
        raise Exception('number is 0, has no order!')
    testorder = 0
    while 10**testorder >= n:
        testorder -= 1
    while 10**testorder <= n:
        testorder += 1
    return testorder - 1

def find_graphlims(max=10,min=-10): # Finds appropriate y-axis limits for data
    maxorder = numorder(max)
    minorder = numorder(min)
    if maxorder - minorder >= 3:
        minlim = 0
    elif minorder - maxorder >= 3:
        maxlim = 0
    else:
        if max == 0:
            maxlim = 0
        else:
            maxlim = np.ceil(max/float(10**maxorder)) * 10**maxorder
        if min == 0:
            minlim = 0
        else:
            minlim = np.floor(min/float(10**minorder)) * 10**minorder
    return minlim, maxlim

def pull_vars(t_start,t_end,animation_scale,framerate):
    print('pulling vars')
    print(t_start.get())
    return t_start.get(), t_end.get(), animation_scale.get(), framerate.get()

def plotting_execution(t_start_field,t_end_field,anim_scale_field,framerate_field,run_smooth,run_interpolate,smoothing_check,interp_check):
    print('executing plotting')

    t_i = tk.DoubleVar()
    t_f = tk.DoubleVar()
    a_scale = tk.DoubleVar()
    fr = tk.DoubleVar()
    run_smo = run_smooth.get()
    run_intp = run_interpolate.get()

    t_i = t_start_field.get()
    t_f = t_end_field.get()
    a_scale = anim_scale_field.get()
    fr = framerate_field.get()

    print('t_start is:',t_i)
    print('smoothing check:', run_smo)
    print('interp check:', run_intp)
