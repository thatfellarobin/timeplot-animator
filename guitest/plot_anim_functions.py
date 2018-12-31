def test():
    print('testing testing!')

def numorder(number): # Finds the order of magnitude of a number
    number = abs(number)
    if number == 0:
        raise Exception('number is 0, has no order!')
    testorder = 0
    while 10**testorder >= number:
        testorder -= 1
    while 10**testorder <= number:
        testorder += 1
    return testorder - 1

def find_graphlims(max=10,min=-10): # Finds appropriate y-axis limits for data
    maxorder = numorder(max)
    minorder = numorder(min)
    if maxorder - minorder >= 3:
        minlim = 0
    elif minorder - maxorder >= 3:
        maxlim = 0
    else:
        if max == 0:
            maxlim = 0
        else:
            maxlim = np.ceil(max/float(10**maxorder)) * 10**maxorder
        if min == 0:
            minlim = 0
        else:
            minlim = np.floor(min/float(10**minorder)) * 10**minorder
    return minlim, maxlim

def pull_vars(t_start,t_end,animation_scale,framerate,run_smooth,run_interpolate)
    return t_start.get(), t_end.get(), animation_scale.get(), framerate.get(), run_smooth.get(), run_interpolate.get()

def plotting_execution(t_start,t_end,animation_scale,framerate,run_smooth,run_interpolate):
    t_start, t_end, animation_scale, framerate, run_smooth, run_interpolate = pull_vars(t_start,t_end,animation_scale,framerate,run_smooth,run_interpolate)
    
