import tkinter as tk
from PIL import ImageTk, Image
import os
import glob
import numpy as np
from scipy import interpolate, signal
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt  # https://github.com/MTG/sms-tools/issues/36
import cv2


class MainApplication:
    def __init__(self, master):

        master.title('Timeplot Animator')

        # File loading
        self.file_frame = tk.Frame(master)
        self.file_label = tk.Label(self.file_frame,
            text='File Load',
            font='Helvetica 16 bold',
            anchor=tk.N)

        self.filename_label = tk.Label(self.file_frame, text='Filename')
        self.filename_field = tk.Entry(self.file_frame)
        self.filename_field.insert(0, 'data.csv')
        self.headerrows_label = tk.Label(self.file_frame, text='Number of Header Rows')
        self.headerrows_field = tk.Entry(self.file_frame)
        self.headerrows_field.insert(0, '1')
        self.datacolumns_label = tk.Label(self.file_frame, text='Number of Lines to Plot')
        self.datacolumns_field = tk.Entry(self.file_frame)
        self.datacolumns_field.insert(0, '1')

        self.file_frame.grid(row=0, column=0, sticky=tk.NW)
        self.file_label.grid(row=0, column=0, columnspan=2, sticky=tk.W)
        self.filename_label.grid(row=1, column=0, sticky=tk.W)
        self.filename_field.grid(row=1, column=1)
        self.headerrows_label.grid(row=2, column=0, sticky=tk.W)
        self.headerrows_field.grid(row=2, column=1)
        self.datacolumns_label.grid(row=3, column=0, sticky=tk.W)
        self.datacolumns_field.grid(row=3, column=1)

        # General Parameters
        self.param_frame = tk.Frame(master)
        self.param_label = tk.Label(self.param_frame,
            text='General Parameters',
            font='Helvetica 16 bold',
            anchor=tk.NW)

        self.t_start_label = tk.Label(self.param_frame, text='Start Time (data units)')
        self.t_start_field = tk.Entry(self.param_frame)
        self.t_end_label = tk.Label(self.param_frame, text='End Time (data units)')
        self.t_end_field = tk.Entry(self.param_frame)
        self.anim_scale_label = tk.Label(self.param_frame, text='Animation Scale')
        self.anim_scale_field = tk.Entry(self.param_frame)
        self.anim_scale_field.insert(0, '1')
        self.framerate_label = tk.Label(self.param_frame, text='Animation Framerate')
        self.framerate_field = tk.Entry(self.param_frame)
        self.framerate_field.insert(0, '30')

        self.param_frame.grid(row=1, column=0, sticky=tk.NW)
        self.param_label.grid(row=0, column=0, columnspan=2, sticky=tk.W)
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
        self.smoothing_label = tk.Label(self.smoothing_frame,
            text='Smoothing',
            font='Helvetica 16 bold',
            anchor=tk.NW)
        self.smoothing_check = tk.Checkbutton(self.smoothing_frame,
            text='Apply Smoothing',
            variable=self.run_smooth)

        self.smoothing_frame.grid(row=2, column=0, sticky=tk.NW)
        self.smoothing_label.grid(row=0, column=0, sticky=tk.NW)
        self.smoothing_check.grid(row=1, column=0, sticky=tk.NW)

        # Interpolation
        self.run_interpolate = tk.IntVar()
        self.interp_frame = tk.Frame(master)
        self.interp_label = tk.Label(self.interp_frame,
            text='Interpolation',
            font='Helvetica 16 bold',
            anchor=tk.NW)
        self.interp_check = tk.Checkbutton(self.interp_frame,
            text='Apply Interpolation',
            variable=self.run_interpolate)

        self.interp_frame.grid(row=3, column=0, sticky=tk.NW)
        self.interp_label.grid(row=0, column=0, sticky=tk.NW)
        self.interp_check.grid(row=1, column=0, sticky=tk.NW)

        # Graph Settings
        self.graphsetting_frame = tk.Frame(master)
        self.graphsetting_label = tk.Label(self.graphsetting_frame,
            text='Graphing Parameters',
            font='Helvetica 16 bold',
            anchor=tk.N)

        self.graphtitle_label = tk.Label(self.graphsetting_frame, text='Graph Title')
        self.graphtitle_field = tk.Entry(self.graphsetting_frame)
        self.graphtitle_field.insert(0, 'Data versus Time')
        self.graphx_label = tk.Label(self.graphsetting_frame, text='X Axis Label')
        self.graphx_field = tk.Entry(self.graphsetting_frame)
        self.graphx_field.insert(0, 'Time')
        self.graphy_label = tk.Label(self.graphsetting_frame, text='Y Axis Label')
        self.graphy_field = tk.Entry(self.graphsetting_frame)
        self.graphy_field.insert(0, 'Data')

        self.graphsetting_frame.grid(row=0, column=1, rowspan=4, sticky=tk.NW)
        self.graphsetting_label.grid(row=0, column=0, columnspan=2, sticky=tk.W)
        self.graphtitle_label.grid(row=1, column=0, sticky=tk.W)
        self.graphtitle_field.grid(row=1, column=1)
        self.graphx_label.grid(row=2, column=0, sticky=tk.W)
        self.graphx_field.grid(row=2, column=1)
        self.graphy_label.grid(row=3, column=0, sticky=tk.W)
        self.graphy_field.grid(row=3, column=1)

        # Graph Preview
        self.preview_frame = tk.Frame(master)
        self.preview_label = tk.Label(self.preview_frame,
            text='Plot Preview (final frame)',
            font='Helvetica 16 bold',
            anchor=tk.N)

        self.preview_frame.grid(row=0, column=2, rowspan=4, sticky=tk.N)
        self.preview_label.grid(row=0, column=0)

        # Execution
        self.execution_frame = tk.Frame(master)
        self.preview_button = tk.Button(self.execution_frame,
            text='Generate Plot Preview',
            command=lambda: self.generate_preview())
        self.execution_button = tk.Button(self.execution_frame,
            text='Generate Frames',
            command=lambda: self.plotting_execution(master))
        self.videoexp_button = tk.Button(self.execution_frame,
            text='Generate Animation\nfrom Existing Frames',
            command=lambda: self.export_video())

        self.execution_frame.grid(row=4, column=0, columnspan=3)
        self.preview_button.grid(row=0, column=0, padx=5, pady=5)
        self.execution_button.grid(row=0, column=1, padx=5, pady=5)
        self.videoexp_button.grid(row=0, column=2, padx=5, pady=5)

        # Some global GUI appearance stuff
        master.grid_columnconfigure(0, weight=0)
        master.grid_columnconfigure(1, weight=0)
        master.grid_columnconfigure(2, weight=2)

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
        maxorder = self.numorder(max)
        minorder = self.numorder(min)
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
    def plot_prepare(self, clear=True):
        directory = os.getcwd() + '/frames'
        if not os.path.exists(directory):
            os.makedirs(directory)

        if clear:
            for oldFrame in os.listdir('frames'):
                if oldFrame.endswith('.png'):
                    os.unlink('frames/' + oldFrame)

        self.fig, self.ax = plt.subplots()

        self.font = {'weight': 'bold',
            'fontname': 'Arial'}

    # Export Frames
    def frame_export(self, title):
        title = str(title)
        self.ax.cla()

        # Plot properties
        plt.xlabel(self.graphx_field.get(), fontdict=self.font)
        plt.ylabel(self.graphy_field.get(), fontdict=self.font)
        plt.title(self.graphtitle_field.get(), fontdict=self.font)
        plt.set_cmap('tab10')
        self.ax.set_xlim(0, self.t_domain)
        self.ax.set_ylim(self.find_graphlims(max=np.max(self.ys), min=np.min(self.ys)))
        self.ax.grid()

        # Plotting
        self.animation_time = self.frame_tstep * self.frame
        self.frameindex = int(round(self.animation_time / (self.a_scale * self.t_delta)))
        for i in range(self.datacolumns):
            self.ax.plot(self.xs[0:self.frameindex], self.ys[0:self.frameindex, i], linewidth=3)

        self.fig.savefig('frames/frame_' + title + '.png', dpi=200)

        print('saved frame_' + title)

    # Build this out to validate all the user inputs and warn/abort as necessary
    # Should fill in some default values if the user left fields blank (or just take care of this by having default values pre-populated)
    def input_validate(self):
        pass

    # Gather user inputs and get the data ready internally
    def prepare_data(self):
        try:
            self.t_i = float(self.t_start_field.get())
            self.t_f = float(self.t_end_field.get())
            self.a_scale = float(self.anim_scale_field.get())
            self.fr = float(self.framerate_field.get())
            self.filename = self.filename_field.get()
            self.headerrows = int(self.headerrows_field.get())
            self.datacolumns = int(self.datacolumns_field.get())
        except ValueError:
            print('Improper input data (put numbers where numbers are supposed to go)')
            self.execution_button.config(text='Generate Frames', state=tk.NORMAL)

        # Load data
        self.data = np.loadtxt(self.filename, delimiter=',', skiprows=self.headerrows)

        # Preparing cropped list of x values
        self.t_delta = self.data[1, 0] - self.data[0, 0]
        self.t_domain = self.t_f - self.t_i
        self.xs = np.linspace(0, self.t_domain, num=int(self.t_domain / self.t_delta))

        # Preparing cropped list of y values
        self.t_start_index = int(round((self.t_i - self.data[0, 0]) / self.t_delta))
        self.t_end_index = self.t_start_index + len(self.xs)
        self.ys = self.data[self.t_start_index:self.t_end_index, 1:self.datacolumns + 1]

        self.num_frames = int(self.t_domain * self.fr * self.a_scale)
        self.frame_tstep = 1. / self.fr  # How much animation-time passes per frame

    def smooth_and_interp(self):
        if self.run_smooth.get():
            self.smoothing_window = int(np.ceil(np.median([4, 2 * len(self.xs) / self.num_frames, 12])) // 2 * 2 + 1)  # Round up to nearest odd number
            print('smoothing with window', self.smoothing_window)
            if self.smoothing_window <= 5:
                print('warning: small smoothing window')
            self.ys = signal.savgol_filter(self.ys,
                window_length=self.smoothing_window,
                polyorder=3,
                axis=0)

        if self.run_interpolate.get():
            self.new_xs = np.linspace(0, self.t_domain, num=self.num_frames)
            self.t_delta = self.new_xs[1] - self.new_xs[0]

            for i in range(self.datacolumns):
                f = interpolate.interp1d(self.xs, self.ys[:, i], kind='quadratic')
                self.new_ys = f(self.new_xs)
                self.ys[:, i] = self.new_ys

            self.xs = self.new_xs

    # Create a preview for the user to evaluate
    def generate_preview(self):
        print('generating preview')

        self.prepare_data()
        self.smooth_and_interp()

        self.plot_prepare(False)

        self.frame = self.num_frames - 1
        self.frame_export('preview')

        self.preview_raw = Image.open('frames/frame_preview.png')
        self.preview_width, self.preview_height = self.preview_raw.size
        self.preview_resized = self.preview_raw.resize(
            (400, int(self.preview_height / (self.preview_width / 400))),
            Image.ANTIALIAS)

        self.preview_image = ImageTk.PhotoImage(self.preview_resized)
        self.preview_panel = tk.Label(self.preview_frame, image=self.preview_image)

        self.preview_panel.grid(row=1, column=0)

    def export_video(self):
        self.fr = float(self.framerate_field.get())
        self.framelist = glob.glob('frames/*.png')
        self.framelist = [s.strip('frames/frame_') for s in self.framelist]
        self.framelist = sorted([int(s.strip('.png')) for s in self.framelist])
        self.framelist = ['frames/frame_' + str(i) + '.png' for i in self.framelist]
        # self.framelist = sorted([int(s.strip('frames/frame_')) for s in glob.glob('frames/*.png')])
        if len(self.framelist) != 0:
            self.first_frame = Image.open(self.framelist[0])
            self.fourcc = cv2.VideoWriter_fourcc(*'MP42')
            self.writer = cv2.VideoWriter('output.avi', self.fourcc, self.fr, self.first_frame.size, isColor=True)
            for fr in self.framelist:
                self.efr = cv2.imread(fr)
                self.writer.write(self.efr)
            self.writer.release()
        else:
            print('no video frames in \'frames\' folder!')

    # Generate the animation frames
    def plotting_execution(self, master):

        self.execution_button.config(text='Generating...', state=tk.DISABLED)
        master.update()

        self.prepare_data()
        self.smooth_and_interp()

        self.plot_prepare()

        print('outputting', self.num_frames, 'frame(s)')

        for self.frame in range(self.num_frames):
            self.frame_export(str(self.frame))

        self.execution_button.config(text='Generate Frames', state=tk.NORMAL)


if __name__ == '__main__':
    root = tk.Tk()
    mainwindow = MainApplication(root)
    tk.mainloop()
