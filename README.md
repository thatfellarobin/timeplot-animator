# timeplot-animator
If a plot has time on the x-axis, this script can produce the necessary video frames to animate the plot as time evolves.

This was originally developed to animate the burn sequence of a rocket engine, so it is made specifically for sequences that evolve on the order of ~10 seconds.
With light modification, the script would work fine for any other order of timescale.

The script reads in a csv file containing the appropriate data. As a user, you need only to:

- Make sure your data is formatted correctly, or you edit the script accordingly
- Make sure it's reading the file you want, the way you want (appropriate rows ignored and columns grabbed)
- Ensure that the start time and end time are correct
- You enter the targeted video framerate


Possible future developments:

- Add flexibility for other timescale orders (ie, user-specified rate of time evolution)
