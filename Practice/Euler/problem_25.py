__author__ = 'karthikb'


def fibnonacci():
    a,b = 0,1
    c = 0
    while len(str(c))< 1000:
        c = a + b
        a,b = b,c
    return c


print fibnonacci()
