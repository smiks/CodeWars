__author__ = 'Sandi'
def format_duration(seconds):

    if seconds == 0:
        return "now"

    years = seconds // (365*86400)
    seconds = seconds-(years*365*86400)

    days = seconds // 86400
    seconds = seconds-(days*86400)

    hours = seconds//3600
    seconds = seconds-(hours*3600)

    minutes = seconds//60
    seconds = seconds-(minutes*60)

    output = []
    if years == 1:
        output.append("{0} year".format(years))
    if years > 1:
        output.append("{0} years".format(years))

    if days == 1:
        output.append("{0} day".format(days))
    if days > 1:
        output.append("{0} days".format(days))

    if hours == 1:
        output.append("{0} hour".format(hours))
    if hours > 1:
        output.append("{0} hours".format(hours))

    if minutes == 1:
        output.append("{0} minute".format(minutes))
    if minutes > 1:
        output.append("{0} minutes".format(minutes))

    if seconds == 1:
        output.append("{0} second".format(seconds))
    if seconds > 1:
        output.append("{0} seconds".format(seconds))

    mes = ""
    if len(output) == 1:
        return output[0]

    for e, i in enumerate(output):
        if e+1 == len(output):
            mes += " and " + i
        else:
            mes +=", " + i

    return mes.lstrip("and ").lstrip(", ")