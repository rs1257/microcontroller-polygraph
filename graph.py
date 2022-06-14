class graph(object):
    '''
    docstring
    '''


    def __init__(self):
        '''
        Constructor
        
        This sets up the size of the graph and displays it on the screen
        '''
        import matplotlib.pyplot as plt
              
        self.plt = plt
        self.figure = plt.figure(figsize=(10, 5))
        self.subplot = self.figure.add_subplot(111)
        self.subplot.set_ylim([0, 100])
        
        
        self.lines = {}
        
        
        plt.show(block=False)
        
        
    def addline(self, line):
        '''
        this is used for adding a line to the graph
        
        input a line class
        '''
        self.lines[line.name], = self.subplot.plot([i for i in xrange(50)], [0]*50, line.colour, label=line.name)
        handles, labels = self.subplot.get_legend_handles_labels()
        self.subplot.legend(handles, labels, loc=2)
     
    def changeline(self, linename, yvals):
        '''
        this is used for changing a line that is already plotted on the graph
        '''
        try:
            graph_y = self.lines[linename].get_ydata()
            
            for _ in xrange(len(yvals)):
                graph_y.pop(0)
                
            graph_y += yvals
        
        except AttributeError:
            graph_y = self.lines[linename].get_ydata().tolist()
            
            for _ in xrange(len(yvals)):
                graph_y.pop(0)
                
            graph_y += yvals
        
        self.lines[linename].set_ydata(graph_y)
        
        
        
    def update(self):
        '''
        this is used to update the data displayed on the graph
        '''

        self.plt.draw()
        
        
        
        
class line(object):
    '''
    docstring
    
    create a line to display on the graph.
    
    xvals, yvals -- are arrays of numbers to plot
    
    colour -- the colour the line should be
    '''
    
    def __init__(self, name, colour):
        '''
        Constructor
        '''
        self.colour = colour
        self.name = name
        

    
