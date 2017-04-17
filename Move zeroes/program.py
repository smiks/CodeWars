def move_zeroes(*args):
    args = sorted( list( filter(lambda x: x!= 0, args) ) ) + [0]*sum(1 for i in args if i == 0) 
    return args