import tkinter as tk

root = tk.Tk()
root.title('Timeplot Animator')

param_frame = tk.Frame(root)
param_label = tk.Label(param_frame, text='General Parameters', width=50).grid(row=0,column=0)
param_label = tk.Label(param_frame, text='Test', width=50).grid(row=1,column=0)
# param_frame.grid(row=0,column=0)

# smoothing_frame = tk.Frame(root).grid(row=1,column=0)
# smoothing_label = tk.Label(smoothing_frame, text='Smoothing').pack()
# # smoothing_frame.pack()
#
# interp_frame = tk.Frame(root)#.grid(row=2,column=0)
# interp_label = tk.Label(interp_frame, text='Interpolation')
# # interp_frame.pack()
#
# preview_frame = tk.Frame(root)#.grid(row=0,column=1)
# preview_label = tk.Label(preview_frame, text='Plot Preview (final frame)')
# # preview_frame.pack() # Eventually have the preview frame on the right

tk.mainloop()

# TODO eventually:
# - explanation under each section label
# - Organize frames by grid, with proper sizing
# - Figure out how to use field entries
