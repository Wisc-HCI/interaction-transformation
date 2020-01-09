import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QSizePolicy

class Plotter(FigureCanvas):

	def __init__(self, parent=None, width=5, height=4, dpi=100):
		plt.rcParams.update({'font.size': 5})
		plt.tight_layout()
		self.fig = Figure(figsize=(width/100.0, height/100.0), dpi=dpi)
		FigureCanvas.__init__(self, self.fig)
		self.setParent(parent)
		self.update_geometry(width,height)

	def update_geometry(self, width, height):
		self.fig.set_size_inches(width/100.0, height/100.0)
		self.axes = self.fig.add_subplot(111)

		FigureCanvas.setSizePolicy(self,
				QSizePolicy.Expanding,
				QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

	def plotLineGraph(self, r, ylabel, xlabel, title):

		self.axes.clear()
		self.axes.plot(r)
		self.axes.set_ylabel(ylabel, fontsize=7)
		self.axes.set_xlabel(xlabel, fontsize=7)
		self.axes.set_title(title, fontsize=8)
		self.axes.legend()
		self.draw()
