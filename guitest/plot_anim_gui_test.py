import tkinter as tk

root = tk.Tk()
root.title('Timeplot Animator')

param_frame = tk.Frame(root)
param_frame.pack(side = BOTTOM)
smoothing_frame = tk.Frame(root)
smoothing_frame.pack(side = BOTTOM)
interp_frame = tk.Frame(root)
interp_frame.pack(side = BOTTOM)
preview_frame = tk.Frame(root)
preview_frame.pack(side = BOTTOM) # Eventually have the preview frame on the right

root.mainloop()
