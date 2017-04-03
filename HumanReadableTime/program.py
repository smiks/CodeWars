__author__ = 'Sandi'
def make_readable(seconds):
    hours = seconds//3600
    seconds = seconds-(hours*3600)

    minutes = seconds//60
    seconds = seconds-(minutes*60)

    ht = hours
    if hours < 10:
        ht = "0"+str(hours)

    mt = minutes
    if minutes < 10:
        mt = "0"+str(minutes)

    st = seconds
    if seconds < 10:
        st = "0"+str(seconds)

    return str(ht)+":"+str(mt)+":"+str(st)



print(make_readable(86399))