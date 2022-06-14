
class recordeddata(object):
    '''
    this is used to store recorded data so it can be put onto the graph and output to a csv
    '''


    def __init__(self):
        self.graphlist = [0]*200
        self.max = 1.0
        self.lastvalue = 0
        
    def newvalue(self, x):
        '''
        used for inputting data recorded from a port
        '''
        if x > self.max:
            for i in xrange(len(self.graphlist)):
                self.graphlist[i] *= self.max
                self.graphlist[i] /= x
            self.max = float(x)
            
        self.graphlist.pop(0)
        self.graphlist.append((x/self.max)*100)
        self.lastvalue = x
        
    def getgraphlist(self):
        return self.graphlist
                
                
                
        