# timeplot-animator
If a plot has time on the x-axis, this script can produce the necessary video frames to animate the plot as time evolves.

This was originally developed to animate rocket engine test data, to overlay on top of test footage. An example of the result can be seen in [this video](https://www.youtube.com/watch?v=liMpHmOH-Bc "UXO - Kismet Static Fire #2")

## How do I use it?
The script reads in a csv file containing the appropriate data, which must be in the same folder as the script. Column 0 should have contain timestamps, and column 1 should contain the data. Note that the script currently assumes a single header row, and does not support data with variable sampling frequency.

Running timeplot_animator.py should open a GUI. Here's a quick reference:

![if u see dis da image is broken lmao](https://github.com/thatfellarobin/timeplot-animator/blob/master/keyCAD_timeplotanim/keyCAD_timeplotanim.001.png)

![if u see dis da image is broken lmao](https://github.com/thatfellarobin/timeplot-animator/blob/master/keyCAD_timeplotanim/keyCAD_timeplotanim.002.png)

![if u see dis da image is broken lmao](https://github.com/thatfellarobin/timeplot-animator/blob/master/keyCAD_timeplotanim/keyCAD_timeplotanim.003.png)

![if u see dis da image is broken lmao](https://github.com/thatfellarobin/timeplot-animator/blob/master/keyCAD_timeplotanim/keyCAD_timeplotanim.004.png)

## Possible future developments:
- Prettier graphs
- Prettier GUI
- GUI allows control of more parameters
- File import preview
- Export video file directly
- Handle non-constant time deltas between data points (already does if interpolation is used)
- Graph Legend
- Secondary Axis
- Able to accept excel files

### Known issues:
- Byte order mark at the beginning of some files can mess things up if there are no header rows.
- If the start or end time are out of bounds, the script doesn't run properly.
- The window can be hard to close sometimes. Exit button, cmd-Q, etc. don't work. Workaround: use ctrl-C (keyboard interrupt) in the terminal.
