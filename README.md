# timeplot-animator
If a plot has time on the x-axis, this script can produce the necessary video frames to animate the plot as time evolves.

This was originally developed to animate the burn sequence of a rocket engine.

The script reads in a csv file containing the appropriate data. As a user, you need only to:

- Make sure your data is formatted correctly, or you edit the script accordingly
- Make sure it's reading the file you want, the way you want (appropriate rows ignored and columns grabbed)
- Ensure that the start time and end time are correct
- Enter the targeted video framerate
- Enter the appropriate scaling factor


Possible future developments:

- Prettier graphs
An example of the result can be seen in [this video](https://youtu.be/xugzcG_lRMA "Waterloo Rocketry STF 8")
