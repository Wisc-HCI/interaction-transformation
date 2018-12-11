import sys
import os
from PyQt5.QtCore import QSize, QRect, Qt, QCoreApplication, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFrame, QScrollArea, QSlider, QComboBox, QGroupBox, QProgressBar, QPushButton, QListWidget, QListWidgetItem, QMainWindow, QAction, QSpinBox, QCheckBox
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import QWebEngineView

from controller import *
from json_exporter import *
from reader import *
from plot_window import *

class App(QMainWindow):

    '''
    Set up the window
    '''

    def __init__(self):
        super(App, self).__init__()
        self.title = 'Repair Progress'
        desktop = QApplication.desktop()
        screen_resolution = desktop.screenGeometry()
        self.width, self.height = screen_resolution.width(), screen_resolution.height()

        # read the interaction
        self.json_exp = JSONExporter()
        self.TS, self.micro_selection = Reader("interaction.xml").build()
        st_reachables = {}
        for state in self.TS.states:
            st_reachables[state] = True
        # DELETE:
        st_reachables["Begin"] = False
        st_reachables["QA_While_Move"] = False
        st_reachables["All_Topics"] = False
        self.json_exp.export_from_object(self.TS, st_reachables)

        # initialize the controller
        self.adapter = Controller(self.TS, sys.argv[1])

        # show the UI
        self.initUI()
        self.show()

    def initUI(self):

        '''
        Initialize components within the main window
        '''
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

        # d3 stuff
        self.make_dimension_file()
        self.webView = QWebEngineView(self)
        self.webView.setGeometry(0, 0, self.width, self.height)
        self.load_graph()

        # control panel
        self.control_panel = QLabel(self)
        self.control_panel.setGeometry(0,0,100,200)
        self.control_panel.setFrameShape(QFrame.Box)
        self.adapt_button = QPushButton("Adapt", self.control_panel)
        self.adapt_button.setGeometry(10, 10, 80, 50)
        self.adapt_button.setStyleSheet(""".QPushButton {color: white; border-radius: 4px;background: rgb(255, 150, 0);}
                                     .QPushButton:pressed {color: white; border-radius: 4px;background: rgb(200, 100, 0);}""")
        self.adapt_button.clicked.connect(self.mcmc_adapt)
        self.view_before_button = QPushButton("pre adapt", self.control_panel)
        self.view_before_button.setGeometry(10, 100, 80, 40)
        self.view_before_button.setStyleSheet(""".QPushButton {color: white; border-radius: 4px;background: rgb(100, 100, 100);}
                                     .QPushButton:pressed {color: white; border-radius: 4px;background: rgb(50, 50, 50);}""")
        self.view_after_button = QPushButton("post adapt", self.control_panel)
        self.view_after_button.setGeometry(10, 150, 80, 40)
        self.view_after_button.setStyleSheet(""".QPushButton {color: white; border-radius: 4px;background: rgb(0, 200, 230);}
                                     .QPushButton:pressed {color: white; border-radius: 4px;background: rgb(0, 150, 180);}""")

        # initialize the plotting window
        print(QApplication.desktop().screenGeometry().height())
        print(self.height)
        self.reward_window = PlotWindow(self, self.width - 300, 4*self.height/5.55, 300, self.height/5.55)
        self.reward_window.setFrameShape(QFrame.Box)

        # initialize progress window
        self.progress_window = PlotWindow(self, self.width - 300, 3*self.height/5.55, 300, self.height/5.55)
        self.progress_window.setFrameShape(QFrame.Box)
        self.progress_window.set_title("progress over time")
        self.progress_window.update_graph([])

        # initialize cost window
        self.cost_window = PlotWindow(self, self.width - 300, 2*self.height/5.55, 300, self.height/5.55)
        self.cost_window.setFrameShape(QFrame.Box)
        self.cost_window.set_title("cost over time")
        self.cost_window.set_ylabel("cost")
        self.cost_window.update_graph([])

        # model checking window
        self.prop_window = PlotWindow(self, self.width - 300, self.height/5.55, 300, self.height/5.55)
        self.prop_window.setFrameShape(QFrame.Box)
        self.prop_window.set_title("ratio of props satisfied")
        self.prop_window.set_ylabel("ratio")
        self.prop_window.update_graph([])

        # initialize distance window
        self.distance_window = PlotWindow(self, self.width - 300, 0, 300, self.height/5.55)
        self.distance_window.setFrameShape(QFrame.Box)
        self.distance_window.set_title("distance to original")
        self.distance_window.set_ylabel("distance")
        self.distance_window.update_graph([])

    def load_graph(self):
        url = QUrl.fromLocalFile("{}/d3js/example2.html".format(os.getcwd()))
        self.webView.load(url)

    def make_dimension_file(self):
        dimension_dict = {"width":self.width, "height":self.height, "font":16, "behaviors":False}
        with open('d3js/dimensions.json', 'w') as outfile:
            json.dump(dimension_dict, outfile)

    def mcmc_adapt(self):
        self.TS, st_reachables = self.adapter.mcmc_adapt(self.TS, self.micro_selection, self.reward_window, self.progress_window, self.cost_window, self.prop_window, self.distance_window)
        self.json_exp.export_from_object(self.TS, st_reachables)
        self.load_graph()

    def z3_adapt(self):
        solution = self.adapter.z3_adapt()
        self.json_exp.export_from_z3(solution)
        self.load_graph()

if __name__ == "__main__":

    # start the GUI
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
