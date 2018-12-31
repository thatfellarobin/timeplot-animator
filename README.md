# timeplot-animator
If a plot has time on the x-axis, this script can produce the necessary video frames to animate the plot as time evolves.

This was originally developed to animate rocket engine test data, to overlay on top of test footage. An example of the result can be seen in [this video](https://www.youtube.com/watch?v=liMpHmOH-Bc "UXO - Kismet Static Fire #2")

## How do I use it?
The script reads in a csv file containing the appropriate data. Column 0 should have contain timestamps, and column 1 should contain the data. Note that the script currently assumes a single header row, and does not support data with variable sampling frequency.

Running timeplot_animator.py should open a GUI. Here are some notes about the various fields and buttons.
- Ensure that the start time and end time are correct
- Enter the targeted video framerate
- Enter the appropriate scaling factor (you'd use this if the time units of your data aren't seconds and/or if your playback rate isn't real time. A value of 1 means one second of animation for one unit of data.)
- Indicate in the code if interpolation and/or smoothing should be performed on the data.

Some assumptions made about the data:

- The timestep between measurements is constant, there is no variable sampling frequency during data collection
- The data is comma-separated

Possible future developments:

- Prettier graphs
- GUI
- Export video file directly
- Variable output image resolution
- Handle non-constant time deltas between data points (already does if interpolation is used)
