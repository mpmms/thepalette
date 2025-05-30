from ..colors import Color

def maker(*args, **kwargs):
    if kwargs:
        p = kwargs
        if p["intype"] == "hex":
            c = []
            for i in range(len(args)):
                c.append(Color().get_rgb(hex=args[i]))
            args = c
        if p["intype"] == "cmyk":
            c = []
            for i in range(len(args)):
                c.append(Color().get_rgb(cmyk=args[i]))
            args = c
        if p["intype"] == "hsl":
            c = []
            for i in range(len(args)):
                c.append(Color().get_rgb(hsl=args[i]))
            args = c
        if p["intype"] == "hsv":
            c = []
            for i in range(len(args)):
                c.append(Color().get_rgb(hsv=args[i]))
            args = c
    l = len(args)
    s = [0, 0, 0]
    for t in args:
        for i in range(3):
            s[i] += t[i] / l
    for i in range(3):
        s[i] = round(s[i])
    s = tuple(s)
    if kwargs:
        p = kwargs
        if p["outtype"] == "hex":
            return Color().get_hex(rgb=s)
        if p["outtype"] == "cmyk":
            return Color().get_cmyk(rgb=s)
        if p["outtype"] == "hsl":
            return Color().get_hsl(rgb=s)
        if p["outtype"] == "hsv":
            return Color().get_hsv(rgb=s)
    return s