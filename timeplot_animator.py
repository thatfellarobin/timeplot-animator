from pltanim_func import *
import tkinter as tk
import os
import numpy as np
from scipy import interpolate, signal
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt  # https://github.com/MTG/sms-tools/issues/36


class MainApplication:
    def __init__(self, master):
        run_smooth = tk.IntVar()
        run_interpolate = tk.IntVar()
        master.title('Timeplot Animator')

        # General Parameters
        param_frame = tk.Frame(master)
        param_frame.grid(row=0, column=0)
        param_label = tk.Label(param_frame,
            text='General Parameters',
            font='Helvetica 16 bold',
            width=40,
            anchor=tk.W)
        t_start_label = tk.Label(param_frame, text='Start Time (data units)')
        t_start_field = tk.Entry(param_frame)
        t_end_label = tk.Label(param_frame, text='End Time (data units)')
        t_end_field = tk.Entry(param_frame)
        anim_scale_label = tk.Label(param_frame, text='Animation Scale')
        anim_scale_field = tk.Entry(param_frame)
        framerate_label = tk.Label(param_frame, text='Animation Framerate')
        framerate_field = tk.Entry(param_frame)

        param_label.grid(row=0, column=0, columnspan=2)
        t_start_label.grid(row=1, column=0, sticky=tk.W)
        t_start_field.grid(row=1, column=1)
        t_end_label.grid(row=2, column=0, sticky=tk.W)
        t_end_field.grid(row=2, column=1)
        anim_scale_label.grid(row=3, column=0, sticky=tk.W)
        anim_scale_field.grid(row=3, column=1)
        framerate_label.grid(row=4, column=0, sticky=tk.W)
        framerate_field.grid(row=4, column=1)

        # Smoothing
        smoothing_frame = tk.Frame(master)
        smoothing_frame.grid(row=1, column=0)
        smoothing_label = tk.Label(smoothing_frame,
            text='Smoothing',
            font='Helvetica 16 bold',
            width=40,
            anchor=tk.W)
        smoothing_check = tk.Checkbutton(smoothing_frame, text='Apply Smoothing', variable=run_smooth)

        smoothing_label.grid(row=0, column=0, sticky='W')  # Not working as expected
        smoothing_check.grid(row=1, column=0)

        # Interpolation
        interp_frame = tk.Frame(master)
        interp_frame.grid(row=2, column=0)
        interp_label = tk.Label(interp_frame,
            text='Interpolation',
            font='Helvetica 16 bold',
            width=40,
            anchor=tk.W)
        interp_check = tk.Checkbutton(interp_frame, text='Apply Interpolation', variable=run_interpolate)

        interp_label.pack(anchor=tk.W)
        interp_check.pack()

        # Graph Preview
        preview_frame = tk.Frame(master)
        preview_label = tk.Label(preview_frame,
            text='Plot Preview (final frame)',
            font='Helvetica 16 bold',
            width=50,
            anchor=tk.N)

        preview_frame.grid(row=0, column=1, rowspan=3, sticky=tk.N)
        preview_label.pack(fill='y')

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

        def test():
            print('testing testing!')

        def numorder(n):  # Finds the order of magnitude of a number
            n = abs(n)
            if n == 0:
                raise Exception('number is 0, has no order!')
            testorder = 0
            while 10**testorder >= n:
                testorder -= 1
            while 10**testorder <= n:
                testorder += 1
            return testorder - 1

        def find_graphlims(max=10, min=-10):  # Finds appropriate y-axis limits for data
            maxorder = numorder(max)
            minorder = numorder(min)
            if maxorder - minorder >= 3:
                minlim = 0
                maxlim = np.ceil(max / float(10**maxorder)) * 10**maxorder
            elif minorder - maxorder >= 3:
                minlim = np.floor(min / float(10**minorder)) * 10**minorder
                maxlim = 0
            else:
                if max == 0:
                    maxlim = 0
                else:
                    maxlim = np.ceil(max / float(10**maxorder)) * 10**maxorder
                if min == 0:
                    minlim = 0
                else:
                    minlim = np.floor(min / float(10**minorder)) * 10**minorder
            return minlim, maxlim

        def plot_prepare():
            directory = os.getcwd() + '/frames'
            if not os.path.exists(directory):
                os.makedirs(directory)

            for oldFrame in os.listdir('frames'):
                if oldFrame.endswith('.png'):
                    os.unlink('frames/' + oldFrame)

        def frame_export(xs, ys, t_domain, frame_tstep, a_scale, t_delta, fig, ax, font, frame):
            ax.cla()

            # Plot properties
            plt.xlabel('Time', fontdict=font)
            plt.ylabel('Data', fontdict=font)
            plt.title('Data versus Time', fontdict=font)
            ax.set_xlim(0, t_domain)
            ax.set_ylim(find_graphlims(max=np.max(ys), min=np.min(ys)))
            # ax.set_ylim(0, np.ceil(max(ys)/100) * 100)
            ax.grid()

            # Plotting
            animation_time = frame_tstep * frame
            frameindex = int(round(animation_time / (a_scale * t_delta)))
            ax.plot(xs[0:frameindex], ys[0:frameindex], 'r', linewidth=3)

            fig.savefig('frames/frame_' + str(frame) + '.png', dpi=200)

            print('saved frame', frame)

        def input_validate():  # Build this out to validate all the user inputs and warn/abort as necessary
            pass

        def plotting_execution(t_start_field, t_end_field, anim_scale_field, framerate_field, run_smooth, run_interpolate):
            print('executing plotting')

            t_i = float(t_start_field.get())
            t_f = float(t_end_field.get())
            a_scale = float(anim_scale_field.get())
            fr = float(framerate_field.get())
            run_smo = run_smooth.get()
            run_intp = run_interpolate.get()
            filename = 'data.csv'

            # print(t_i)
            # print(t_i == 5.)
            # print(run_smo == True)
            # print(run_intp == True)

            # Load data
            data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0, 1])

            # Preparing cropped list of x values
            t_delta = data[1, 0] - data[0, 0]
            t_domain = t_f - t_i
            xs = np.linspace(0, t_domain, num=t_domain / t_delta)

            # Preparing cropped list of y values
            t_start_index = int(round((t_i - data[0, 0]) / t_delta))
            t_end_index = t_start_index + len(xs)
            ys = data[t_start_index:t_end_index, 1]

            num_frames = int(t_domain * fr * a_scale)
            frame_tstep = 1. / fr  # How much animation-time passes per frame

            if run_smo:
                smoothing_window = int(np.ceil(np.median([4, 2 * len(xs) / num_frames, 12])) // 2 * 2 + 1)
                print('smoothing with window', smoothing_window)
                if smoothing_window <= 5:
                    print("warning: small smoothing window")
                ys = signal.savgol_filter(ys, window_length=smoothing_window, polyorder=3)

            if run_intp:
                f = interpolate.interp1d(xs, ys, kind='quadratic')
                new_xs = np.linspace(0, t_domain, num=num_frames)
                t_delta = new_xs[1] - new_xs[0]
                new_ys = f(new_xs)
                xs = new_xs
                ys = new_ys

            fig, ax = plt.subplots()

            font = {'weight': 'bold',
                    'fontname': 'Arial'
                    }

            print('outputting', num_frames, 'frame(s)')

            plot_prepare()

            for frame in range(num_frames):
                frame_export(xs, ys, t_domain, frame_tstep, a_scale, t_delta, fig, ax, font, frame)


if __name__ == '__main__':
    root = tk.Tk()
    mainwindow = MainApplication(root)
    tk.mainloop()
