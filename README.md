# timeplot-animator
If a plot has time on the x-axis, this script can produce the necessary video frames to animate the plot as time evolves.

This was originally developed to animate the burn sequence of a rocket engine. That's why the python script is called burnanimator.py

The script reads in a csv file containing the appropriate data. As a user, you need only to:

- Make sure your data is formatted correctly, or you edit the script accordingly
- Make sure it's reading the file you want, the way you want (appropriate rows ignored and columns grabbed)
- Ensure that the start time and end time are correct
- Enter the targeted video framerate
- Enter the appropriate scaling factor (you'd use this if the time units of your data aren't seconds and/or if your playback rate isn't real time. A value of 1 means one second of animation for one unit of data.)
- Indicate in the code if interpolation and/or smoothing should be performed on the data.
- Note: I haven't actually tested the smoothing yet. Unknown if it works.

Some assumptions made about the data:

- The timestep between measurements is constant, there is no variable frsampling frequency during data collection
- The data is comma-separated

Possible future developments:

- Prettier graphs
- GUI

An example of the result can be seen in [this video](https://www.youtube.com/watch?v=liMpHmOH-Bc "UXO - Kismet Static Fire #2")
