__author__ = 'Sandi'
def strip_url_params(url, params_to_strip = []):
    from collections import OrderedDict
    # check if any params
    qm = url.find("?")
    if qm == -1:
        return url
    left = url[:qm]
    right = url[qm+1:]
    alreadyFound = OrderedDict()

    params = right.split("&")
    for p in params:
        k, v = p.split("=")
        if k in params_to_strip:
            continue

        if k not in alreadyFound:
            alreadyFound[k] = v

    right = '&'.join([k+"="+v for k, v in alreadyFound.items()]).strip("&")

    url = left+'?'+right
    return url




assert strip_url_params('www.codewars.com', ['b']) == "www.codewars.com"
assert strip_url_params('www.codewars.com?a=1&b=2&a=2') == "www.codewars.com?a=1&b=2"
assert strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']) == "www.codewars.com?a=1"