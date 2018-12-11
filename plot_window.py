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
        self.m = Plotter(parent=self, width=4, height=2.5)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.m.setGeometry(10,10,self.width-20,self.height-20)
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
