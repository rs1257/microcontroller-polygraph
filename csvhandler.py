from time import asctime

def writetofile(yellow, red, a, b, c, d):
    '''
    This function will write the given inputs to the file "data.csv"
    
    the data will be separated by indentations
    '''
    f = open("data.csv", "a")
    f.write(asctime()+','+str(yellow)+","+str(red)+","+str(a)+","+str(b)+","+str(c)+","+str(d)+"\n")
    f.close()
    
def readfromfile(lines):
    '''
    this function will read the last lines from "data.csv"
    
    the "lines" variable defines how many will be read
    
    THIS WILL USE A LOT OF MEMORY IF THE FILE IS LARGE. IT SHOULD ONLY BE USED FOR TESTING CODE.
    '''
    f = open("data.csv", 'r')
    lst = []
    for line in f:
        lst.append(line.rstrip('\n'))
    f.close()
    return lst[-lines:]
