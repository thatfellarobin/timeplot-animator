# timeplot-animator
If a plot has time on the x-axis, this script can produce the necessary video frames to animate the plot as time evolves.

This was originally developed to animate rocket engine test data, to overlay on top of test footage. An example of the result can be seen in [this video](https://www.youtube.com/watch?v=liMpHmOH-Bc "UXO - Kismet Static Fire #2")

## How do I use it?
The script reads in a csv file containing the appropriate data. Column 0 should have contain timestamps, and column 1 should contain the data. Note that the script currently assumes a single header row, and does not support data with variable sampling frequency.

Running timeplot_animator.py should open a GUI. Here's a quick reference:

![if u see dis da image is broken lmao](https://github.com/thatfellarobin/timeplot-animator/blob/master/keyCAD_timeplotanim/keyCAD_timeplotanim.001.jpeg "Behold... my first GUI")

## Possible future developments:
- Prettier graphs
- Prettier GUI
- GUI allows control of more parameters
- Export video file directly
- Handle non-constant time deltas between data points (already does if interpolation is used)
- Plot more than one line
