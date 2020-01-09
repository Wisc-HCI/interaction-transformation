from PyQt5.QtWidgets import QLabel, QFrame

from plotter import *

class PlotWindow(QLabel):

    def __init__(self, parent, left, top, width, height):
        super(PlotWindow, self).__init__(parent=parent)
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.title = "reward over time"
        self.ylabel = "reward"
        self.xlabel = "itr"
        self.initUI()

    def initUI(self):
        self.setFrameShape(QFrame.Box)
        #self.m = Plotter(parent=self, width=self.width, height=self.height)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.m = Plotter(parent=self, width=self.frameGeometry().width(), height=self.frameGeometry().height())
        #self.m.setGeometry(0,0,self.width,self.height)
        #self.init_plot()

    def updatePlotGeometry(self):
        self.m.setGeometry(0,0,self.frameGeometry().width(),self.frameGeometry().height())
        self.m.update_geometry(self.frameGeometry().width(),self.frameGeometry().height())
        self.init_plot()

    def set_title(self, title):
        self.title = title

    def set_xlabel(self, label):
        self.xlabel = label

    def set_ylabel(self, label):
        self.ylabel = label

    def init_plot(self):
        self.m.plotLineGraph([], self.ylabel, self.xlabel, self.title)

    def update_graph(self, r):
        self.m.plotLineGraph(r, self.ylabel, self.xlabel, self.title)
