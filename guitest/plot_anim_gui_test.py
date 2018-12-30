import tkinter as tk

root = tk.Tk()
root.title('Timeplot Animator')

param_frame = tk.Frame(root)
param_frame.grid(row=0,column=0)
param_label = tk.Label(param_frame, text='General Parameters', width=40)
param_label.pack()

smoothing_frame = tk.Frame(root)
smoothing_frame.grid(row=1,column=0)
smoothing_label = tk.Label(smoothing_frame, text='Smoothing')
smoothing_label.pack()

interp_frame = tk.Frame(root)
interp_frame.grid(row=2,column=0)
interp_label = tk.Label(interp_frame, text='Interpolation')
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
