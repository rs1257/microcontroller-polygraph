import Tkinter as tk
from recordeddata import recordeddata
from ryanmaths import rateofchangefoo

class sample:
    def __init__(self):
              
        self.window = tk.Tk()
        self.window.wm_title("Sample Window")
        
        message = tk.Label(self.window, text = "this is a placeholder window")
        message.pack()
        
       
        tk.mainloop()
        


class initial:
    def __init__(self):
        
        self.master = tk.Tk()
        self.master.wm_title("Polygraph")
        top = tk.Frame(self.master)
        top.pack(side=tk.TOP)
        
        self.calibration = tk.Button(self.master, text="Calibration Mode", command=self.calibrationpressed, width = 20)
        self.interview = tk.Button(self.master, text="Interview Mode", command=self.interviewpressed, width = 20)
        
        self.calibration.pack()
        self.interview.pack()
        
        tk.mainloop()
    
    def calibrationpressed(self):
        self.master.destroy()
        warningwindow('calibration')
        
    def interviewpressed(self):
        self.master.destroy()
        warningwindow('interview')
        
class warningwindow:
    def __init__(self, mode):
        
        self._mode = mode
        
        self.window = tk.Tk()
        self.window.wm_title("WARNING!")
        bottom = tk.Frame(self.window)
        bottom.pack(side=tk.BOTTOM)
        
        message = tk.Label(self.window, text = "Are you sure you want to proceed to %s mode?" % (mode))
        message.pack()
        
        yes = tk.Button(self.window, text="YES", command=self.yespressed, width = 20)
        yes.pack(in_=bottom, side=tk.LEFT)
        
        no = tk.Button(self.window, text="NO", command=self.nopressed, width = 20)
        no.pack(in_=bottom, side=tk.RIGHT)
        
        tk. mainloop()
        
    def yespressed(self):
        sample
        self.window.destroy()
        if self._mode == 'calibration':
            startcalibration()
        if self._mode == 'interview':
            startinterview()
            
    def nopressed(self):
        self.window.destroy()
        initial()
        
        
class interviewwindow(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)

        from redyellowbuttons import setupgpio

        setupgpio()
        
        self.window = window
        self.window.wm_title('interview mode')
        
        self.button = tk.Button(self, text="Main Graph", command=self.mainGraph)
        self.button.pack(side="top")
        self.button1 = tk.Button(self, text="SCR - Rate of Change", command=self.rateofchangegraph)
        self.button1.pack(side="top")
        self.button2 = tk.Button(self, text="HR - Interpolation", command=self.interpolatewindow)
        self.button2.pack(side="top")
        self.button3 = tk.Button(self, text="SCR-SST-RR Digital Filters", command=self.filterwindow)
        self.button3.pack(side="top")
        
        self.breath = recordeddata()
        self.conduct = recordeddata()
        self.temp = recordeddata()
        self.heart = recordeddata()
        self.yellow = recordeddata()
        self.red = recordeddata()
        self.rateofchange = recordeddata()
        self.conductfilter = recordeddata()
        self.tempfilter = recordeddata()
        self.breathfilter = recordeddata()
        
        
        self.n = 0
        
        self.window.after(125, self.collectData)
        
        
    def collectData(self):
        from sensordata import getalldata
        getalldata(self.n, self.heart, self.conduct, self.temp, self.breath, self.yellow, self.red)
        self.rateofchange.newvalue(rateofchangefoo(0.1, self.conduct.getgraphlist()[-5:]))
        self.n += 1
        self.window.after(125, self.collectData)
        

    def create_window(self):
        t = tk.Toplevel(self)
        t.wm_title("Window")
        l = tk.Label(t, text="This is window")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
            
        
    def mainGraph(self):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        import matplotlib.animation as animation
        
        self.plt = plt
        window = tk.Toplevel(self)
        window.wm_title('main graph')
        
        figure = self.plt.figure(figsize=(10, 5))
        subplot = figure.add_subplot(111)
        subplot.set_ylim([0, 100])
        
        canvas = FigureCanvasTkAgg(figure, master=window)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        breathline, = subplot.plot([i for i in xrange(200)], self.breath.getgraphlist(), 'red', label='breathing')
        heartline, = subplot.plot([i for i in xrange(200)], self.heart.getgraphlist(), 'green', label='heart')
        templine, = subplot.plot([i for i in xrange(200)], self.temp.getgraphlist(), 'blue', label='temperature')
        conductline, = subplot.plot([i for i in xrange(200)], self.conduct.getgraphlist(), 'purple', label='conduct')
        yellowline, = subplot.plot([i for i in xrange(200)], self.yellow.getgraphlist(), 'yellow', label='yellow button')
        redline, = subplot.plot([i for i in xrange(200)], self.red.getgraphlist(), 'red', label='red button')
        handles, labels = subplot.get_legend_handles_labels()
        subplot.legend(handles, labels, loc=2)
        
        def animate(i):
            breathline.set_ydata(self.breath.getgraphlist())
            heartline.set_ydata(self.heart.getgraphlist())
            templine.set_ydata(self.temp.getgraphlist())
            conductline.set_ydata(self.conduct.getgraphlist())
            yellowline.set_ydata(self.yellow.getgraphlist())
            redline.set_ydata(self.red.getgraphlist())
            return breathline
        def animategraph():
            ani = animation.FuncAnimation(figure, animate, interval=500, blit=False)
            window.after(500, self.mainGraph.animategraph)
        animategraph()
        
        
    def rateofchangegraph(self):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        import matplotlib.animation as animation
        
        self.plt = plt
        window = tk.Toplevel(self)
        window.wm_title('rate of change')
        figure = self.plt.figure(figsize=(10, 5))
        subplot = figure.add_subplot(111)
        subplot.set_ylim([-100, 100])
        canvas = FigureCanvasTkAgg(figure, master=window)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
              
        line, = subplot.plot([i for i in xrange(200)], self.rateofchange.getgraphlist(), 'red', label='rate of change')
        
        def animate(i):
            self.rateofchange.newvalue(rateofchangefoo(0.125, self.conduct.getgraphlist()[-5:]))
            line.set_ydata(self.rateofchange.getgraphlist())
            return line
        def animategraph():
            ani = animation.FuncAnimation(figure, animate, interval=500, blit=False)
            window.after(500, self.mainGraph.animategraph)
        animategraph()
        
    def interpolatewindow(self):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        import matplotlib.animation as animation
        from ryanmaths import interpolate
        
        self.plt = plt
        window = tk.Toplevel(self)
        window.wm_title('Interpolated heart rate')
        figure = self.plt.figure(figsize=(10, 5))
        subplot = figure.add_subplot(111)
        subplot.set_ylim([0, 100])
        subplot.set_xlim([0, 100])
        canvas = FigureCanvasTkAgg(figure, master=window)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
              
        line, = subplot.plot(self.rateofchange.getgraphlist(), 'red', label='interpolation')
        
        def animate(i):
            graphvals = interpolate(self.heart.getgraphlist())
            line.set_ydata(graphvals[1])
            line.set_xdata(graphvals[0])
            return line
        def animategraph():
            ani = animation.FuncAnimation(figure, animate, interval=500, blit=False)
            window.after(500, self.mainGraph.animategraph)
        animategraph()
        
    def filterwindow(self):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        import matplotlib.animation as animation
        from ryanmaths import digitalfilter
        
        self.plt = plt
        window = tk.Toplevel(self)
        window.wm_title('Digital Filter')
        figure = self.plt.figure(figsize=(10, 5))
        subplot = figure.add_subplot(111)
        subplot.set_ylim([0, 100])
        canvas = FigureCanvasTkAgg(figure, master=window)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
              
        breath, = subplot.plot(self.breathfilter.getgraphlist(), 'red', label='Breathing')
        conduct, = subplot.plot(self.conductfilter.getgraphlist(), 'green', label='Conductance')
        temp, = subplot.plot(self.tempfilter.getgraphlist(), 'blue', label='Temperature')
        handles, labels = subplot.get_legend_handles_labels()
        subplot.legend(handles, labels, loc=2)
        
        def animate(i):
            self.breathfilter.newvalue(digitalfilter(self.breath.getgraphlist()[-10:]))
            breath.set_ydata(self.breathfilter.getgraphlist())
            self.conductfilter.newvalue(digitalfilter(self.conduct.getgraphlist()[-10:]))
            conduct.set_ydata(self.conductfilter.getgraphlist())
            self.tempfilter.newvalue(digitalfilter(self.temp.getgraphlist()[-10:]))
            temp.set_ydata(self.tempfilter.getgraphlist())
            return breath, conduct, temp
        def animategraph():
            ani = animation.FuncAnimation(figure, animate, interval=500, blit=False)
            window.after(500, self.mainGraph.animategraph)
        animategraph()
        
        
class startinterview:           
    def __init__(self):
        window = tk.Tk()
        main = interviewwindow(window)
        main.pack(side="top", fill="both", expand=True)
        window.mainloop()
        
        
class calibrationmode(tk.Frame):
    def __init__(self, window):
        from sensordata import getValue
        import LEDBars
        from sensordata import getValue
        
        tk.Frame.__init__(self, window)
        
        LEDBars.setup()
        
        self.window = window
        self.window.wm_title('calibration mode')
        
        self.button = tk.Button(self, text="back", command=self.back)
        self.button.pack(side="top")
        
        scrdata = recordeddata()
        rrdata = recordeddata()
        
        scrdata.newvalue(getValue(0x80))
        rrdata.newvalue(getValue(0x10))
        scrvoltage = (scrdata.lastvalue/4092.0)*3
        rrvoltage = (rrdata.lastvalue/4092.0)*3
        
        self.SCRlabel = tk.Label(self, text="SCR %s volts" % (scrvoltage))
        self.RRlabel = tk.Label(self, text="RR %s volts" % (rrvoltage))
        self.SCRlabel.pack()
        self.RRlabel.pack()
        
        heartval = getValue(0x40) 
        LEDBars.bars((heartval/4092)*200)
        
        def updatewindow():
            window.destroy()
            startcalibration()
        
        updatebutton = tk.Button(self, text="update", command=updatewindow)
        updatebutton.pack()
        
        def updateheart():
            heartval = getValue(0x40) 
            LEDBars.bars(heartval)
            window.after(100, updateheart)
        updateheart()


        
    def back(self):
        from LEDBars import bars
        bars(0)
        self.window.destroy()
        initial()
        
class startcalibration:
    def __init__(self):
        window = tk.Tk()
        main = calibrationmode(window)
        main.pack(side="top", fill="both", expand=True)
        
        window.mainloop()
        
