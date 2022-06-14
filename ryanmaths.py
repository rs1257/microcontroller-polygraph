from time import asctime
def rateofchangefoo (p, x):
    '''
    need to pass an list in of f(n-2p) f(n - p) f(n) f(n + p) f(n + 2p)
    '''
    rateofchange = ((-x[4]) + (8 * x[3]) - (8 * x[1]) + (x[0]))/(12.0 * p)
    
    return rateofchange

def digitalfilter (x): # x is a list of at least 7 samples
    from math import ceil
    value = 0
    if len(x) >= 7:
        x = sorted(x)
        for _ in x:
            if len(x)%2 == 0:
                one = int(((len(x)/2.0)-1)) 
                two = int((len(x)/2.0))
                value = (x[one] + x[two])/2.0
            else:
                index = int(ceil((len(x)-1)/2.0))
                value = x[index]
    return value

def interpolate(inputlst):
    import numpy as np
    from scipy import interpolate
    x = np.arange(0, len(inputlst), 1) #10000 needs to be the same size as the list inputed
    y = inputlst
    tck = interpolate.splrep(x, y, s=0)
    xnew = np.arange(0,100, 0.1)
    ynew = interpolate.splev(xnew, tck, der=0)
    f = open('interpolatedheart.csv', 'a')
    for i in ynew:
        f.write(asctime()+','+str(i)+'\n')
    f.close()
    return [xnew, ynew]