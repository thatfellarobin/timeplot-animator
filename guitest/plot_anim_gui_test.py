import tkinter as tk

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

param_frame = tk.Frame(root)
param_frame.grid(row=0,column=0)
param_label = tk.Label(param_frame, text='General Parameters', width=40)
param_label.pack()

smoothing_frame = tk.Frame(root)
smoothing_frame.grid(row=1,column=0)
smoothing_label = tk.Label(smoothing_frame, text='Smoothing')
smoothing_check = tk.Checkbutton(smoothing_frame,text='Apply Smoothing',variable=run_smooth)
smoothing_check.pack()
smoothing_label.pack()

interp_frame = tk.Frame(root)
interp_frame.grid(row=2,column=0)
interp_label = tk.Label(interp_frame, text='Interpolation')
interp_check = tk.Checkbutton(interp_frame,text='Apply Interpolation',variable=run_interpolate)
interp_check.pack()
interp_label.pack()

preview_frame = tk.Frame(root)
preview_frame.grid(row=0,column=1)
preview_label = tk.Label(preview_frame, text='Plot Preview (final frame)')
preview_label.pack()

tk.mainloop()

# TODO eventually:
# - explanation under each section label
# - Organize frames by grid, with proper sizing
# - Figure out how to use field entries
