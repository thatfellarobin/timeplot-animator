import tkinter as tk
import os
import numpy as np
from scipy import interpolate, signal
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt  # https://github.com/MTG/sms-tools/issues/36


class MainApplication:
    def __init__(self, master):

        master.title('Timeplot Animator')

        # General Parameters
        self.param_frame = tk.Frame(master)
        self.param_frame.grid(row=0, column=0)
        self.param_label = tk.Label(self.param_frame,
            text='General Parameters',
            font='Helvetica 16 bold',
            width=40,
            anchor=tk.W)
        self.t_start_label = tk.Label(self.param_frame, text='Start Time (data units)')
        self.t_start_field = tk.Entry(self.param_frame)
        self.t_end_label = tk.Label(self.param_frame, text='End Time (data units)')
        self.t_end_field = tk.Entry(self.param_frame)
        self.anim_scale_label = tk.Label(self.param_frame, text='Animation Scale')
        self.anim_scale_field = tk.Entry(self.param_frame)
        self.framerate_label = tk.Label(self.param_frame, text='Animation Framerate')
        self.framerate_field = tk.Entry(self.param_frame)

        self.param_label.grid(row=0, column=0, columnspan=2)
        self.t_start_label.grid(row=1, column=0, sticky=tk.W)
        self.t_start_field.grid(row=1, column=1)
        self.t_end_label.grid(row=2, column=0, sticky=tk.W)
        self.t_end_field.grid(row=2, column=1)
        self.anim_scale_label.grid(row=3, column=0, sticky=tk.W)
        self.anim_scale_field.grid(row=3, column=1)
        self.framerate_label.grid(row=4, column=0, sticky=tk.W)
        self.framerate_field.grid(row=4, column=1)

        # Smoothing
        self.run_smooth = tk.IntVar()
        self.smoothing_frame = tk.Frame(master)
        self.smoothing_frame.grid(row=1, column=0)
        self.smoothing_label = tk.Label(self.smoothing_frame,
            text='Smoothing',
            font='Helvetica 16 bold',
            width=40,
            anchor=tk.W)
        self.smoothing_check = tk.Checkbutton(self.smoothing_frame,
            text='Apply Smoothing',
            variable=self.run_smooth)

        self.smoothing_label.grid(row=0, column=0, sticky='W')  # Not working as expected
        self.smoothing_check.grid(row=1, column=0)

        # Interpolation
        self.run_interpolate = tk.IntVar()
        self.interp_frame = tk.Frame(master)
        self.interp_frame.grid(row=2, column=0)
        self.interp_label = tk.Label(self.interp_frame,
            text='Interpolation',
            font='Helvetica 16 bold',
            width=40,
            anchor=tk.W)
        self.interp_check = tk.Checkbutton(self.interp_frame,
            text='Apply Interpolation',
            variable=self.run_interpolate)

        self.interp_label.pack(anchor=tk.W)
        self.interp_check.pack()

        # Graph Preview
        self.preview_frame = tk.Frame(master)
        self.preview_label = tk.Label(self.preview_frame,
            text='Plot Preview (final frame)',
            font='Helvetica 16 bold',
            width=50,
            anchor=tk.N)

        self.preview_frame.grid(row=0, column=1, rowspan=3, sticky=tk.N)
        self.preview_label.pack(fill='y')

        # Execution
        self.execution_frame = tk.Frame(master)
        self.preview_button = tk.Button(self.execution_frame,
            text='Generate Plot Preview')
        self.execution_button = tk.Button(self.execution_frame,
            text='Generate Animation',
            command=lambda: plotting_execution(self))

        self.execution_frame.grid(row=3, column=0, columnspan=2)
        self.preview_button.grid(row=0, column=0, padx=5, pady=5)
        self.execution_button.grid(row=0, column=1, padx=5, pady=5)

        def test(self):
            print('testing testing!')

        # Finds the order of magnitude of a number
        def numorder(self, n):
            n = abs(n)
            if n == 0:
                raise Exception('number is 0, has no order!')
            testorder = 0
            while 10**testorder >= n:
                testorder -= 1
            while 10**testorder <= n:
                testorder += 1
            return testorder - 1

        # Finds appropriate y-axis limits for data
        def find_graphlims(self, max=10, min=-10):
            maxorder = numorder(self, max)
            minorder = numorder(self, min)
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

        # Prepare output folder
        def plot_prepare(self):
            directory = os.getcwd() + '/frames'
            if not os.path.exists(directory):
                os.makedirs(directory)

            for oldFrame in os.listdir('frames'):
                if oldFrame.endswith('.png'):
                    os.unlink('frames/' + oldFrame)

        # Export Frames
        def frame_export(self):
            self.ax.cla()

            # Plot properties
            plt.xlabel('Time', fontdict=self.font)
            plt.ylabel('Data', fontdict=self.font)
            plt.title('Data versus Time', fontdict=self.font)
            self.ax.set_xlim(0, self.t_domain)
            self.ax.set_ylim(find_graphlims(self, max=np.max(self.ys), min=np.min(self.ys)))
            self.ax.grid()

            # Plotting
            self.animation_time = self.frame_tstep * self.frame
            self.frameindex = int(round(self.animation_time / (self.a_scale * self.t_delta)))
            self.ax.plot(self.xs[0:self.frameindex], self.ys[0:self.frameindex], 'r', linewidth=3)

            self.fig.savefig('frames/frame_' + str(self.frame) + '.png', dpi=200)

            print('saved frame', self.frame)

        # Build this out to validate all the user inputs and warn/abort as necessary
        def input_validate(self):
            pass

        def plotting_execution(self):
            print('executing plotting')

            self.t_i = float(self.t_start_field.get())
            self.t_f = float(self.t_end_field.get())
            self.a_scale = float(self.anim_scale_field.get())
            self.fr = float(self.framerate_field.get())
            self.filename = 'data.csv'

            # Load data
            self.data = np.loadtxt(self.filename, delimiter=',', skiprows=1, usecols=[0, 1])

            # Preparing cropped list of x values
            self.t_delta = self.data[1, 0] - self.data[0, 0]
            self.t_domain = self.t_f - self.t_i
            self.xs = np.linspace(0, self.t_domain, num=self.t_domain / self.t_delta)

            # Preparing cropped list of y values
            self.t_start_index = int(round((self.t_i - self.data[0, 0]) / self.t_delta))
            self.t_end_index = self.t_start_index + len(self.xs)
            self.ys = self.data[self.t_start_index:self.t_end_index, 1]

            self.num_frames = int(self.t_domain * self.fr * self.a_scale)
            self.frame_tstep = 1. / self.fr  # How much animation-time passes per frame

            if self.run_smooth.get():
                self.smoothing_window = int(np.ceil(np.median([4, 2 * len(self.xs) / self.num_frames, 12])) // 2 * 2 + 1)  # Round up to nearest odd number
                print('smoothing with window', self.smoothing_window)
                if self.smoothing_window <= 5:
                    print('warning: small smoothing window')
                self.ys = signal.savgol_filter(self.ys, window_length=self.smoothing_window, polyorder=3)

            if self.run_interpolate.get():
                f = interpolate.interp1d(self.xs, self.ys, kind='quadratic')
                self.new_xs = np.linspace(0, self.t_domain, num=self.num_frames)
                self.t_delta = self.new_xs[1] - self.new_xs[0]
                self.new_ys = f(self.new_xs)
                self.xs = self.new_xs
                self.ys = self.new_ys

            self.fig, self.ax = plt.subplots()

            self.font = {'weight': 'bold',
                'fontname': 'Arial'}

            print('outputting', self.num_frames, 'frame(s)')

            plot_prepare(self)

            for self.frame in range(self.num_frames):
                frame_export(self)


if __name__ == '__main__':
    root = tk.Tk()
    mainwindow = MainApplication(root)
    tk.mainloop()
