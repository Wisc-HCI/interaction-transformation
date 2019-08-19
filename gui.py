import sys
import os
import argparse
from PyQt5.QtCore import QSize, QRect, Qt, QCoreApplication, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFrame, QScrollArea, QSlider, QComboBox, QGroupBox, QProgressBar, QPushButton, QListWidget, QListWidgetItem, QMainWindow, QAction, QSpinBox, QCheckBox
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QColor
from PyQt5 import QtCore

from controller import *
from plot_window import *

from trajectory_builder import *

class App(QMainWindow):

    '''
    Set up the window
    '''

    resized = QtCore.pyqtSignal()

    def __init__(self):
        super(App, self).__init__()

        # parse arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--mcmc", help="run mcmc",
                        action="store_true")
        parser.add_argument("-r", "--random", help="run random",
                        action="store_true")
        parser.add_argument("-s", "--smt", help="run smt",
                        action="store_true")
        args = parser.parse_args(sys.argv[2:])

        self.algorithm="mcmc"
        if args.mcmc:
            self.algorithm="mcmc"
        if args.random:
            self.algorithm="random"
        if args.smt:
            self.algorithm="smt"

        self.title = 'Repair Progress'
        desktop = QApplication.desktop()
        screen_resolution = desktop.screenGeometry()
        self.width, self.height = screen_resolution.width(), screen_resolution.height()

        # initialize the controller
        self.adapter = Controller(sys.argv[1])

        # show the UI
        self.resized.connect(self.resizeWindow)
        self.initUI()
        self.compute_inclusion()
        self.show()
        '''

        if self.algorithm == "mcmc":
            print("running mcmc")
            self.mcmc_adapt()
        elif self.algorithm == "random":
            self.random_adapt()
        elif self.algorithm == "smt":
            self.z3_adapt()
        '''

    def resizeEvent(self, event):
        self.resized.emit()
        return super(App, self).resizeEvent(event)

    def resizeWindow(self):
        print("resizing")
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height() - 20
        self.reward_window.setGeometry(self.width - self.width*0.2, 4*self.height/5, self.width*0.2, self.height/5)
        self.reward_window.updatePlotGeometry()
        self.reward_window.update_graph([])
        self.progress_window.setGeometry(self.width - self.width*0.2, 3*self.height/5, self.width*0.2, self.height/5)
        self.progress_window.updatePlotGeometry()
        self.progress_window.update_graph([])
        self.cost_window.setGeometry(self.width - self.width*0.2, 2*self.height/5, self.width*0.2, self.height/5)
        self.cost_window.updatePlotGeometry()
        self.cost_window.update_graph([])
        self.prop_window.setGeometry(self.width - self.width*0.2, self.height/5, self.width*0.2, self.height/5)
        self.prop_window.updatePlotGeometry()
        self.prop_window.update_graph([])
        self.distance_window.setGeometry(self.width - self.width*0.2, 0, self.width*0.2, self.height/5)
        self.distance_window.updatePlotGeometry()
        self.distance_window.update_graph([])
        self.webView.setGeometry(0,0,self.width, self.height)
        self.control_panel.setGeometry(0,0,400,self.height)
        self.trace_panel.setGeometry(10,110,380,self.height - 220)
        self.trace_list.setGeometry(0,0,380,self.height-220)

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
        self.control_panel.setGeometry(0,0,400,self.height)
        self.control_panel.setFrameShape(QFrame.Box)
        self.control_buttons = QLabel(parent=self.control_panel)
        self.control_buttons.setGeometry(0,0,400,100)

        # the adapt button
        self.adapt_button = QPushButton("Adapt", self.control_buttons)
        self.adapt_button.setGeometry(10, 10, 80, 50)
        self.adapt_button.setStyleSheet(""".QPushButton {color: white; border-radius: 4px;background: rgb(255, 150, 0);}
                                     .QPushButton:pressed {color: white; border-radius: 4px;background: rgb(200, 100, 0);}""")
        if self.algorithm == "mcmc":
            self.adapt_button.clicked.connect(self.mcmc_adapt)
        elif self.algorithm == "random":
            self.adapt_button.clicked.connect(self.random_adapt)
        elif self.algorithm == "smt":
            self.adapt_button.clicked.connect(self.z3_adapt)

        # the add trajectories button
        self.traj_build_button = QPushButton("Traj Build", self.control_buttons)
        self.traj_build_button.setGeometry(100, 10, 80, 50)
        self.traj_build_button.setStyleSheet(""".QPushButton {color: white; border-radius: 4px;background: rgb(255, 0, 150);}
                                     .QPushButton:pressed {color: white; border-radius: 4px;background: rgb(200, 0, 150);}""")
        self.traj_build_button.clicked.connect(self.init_traj_builder)

        # compute correctness mutations button
        self.corr_button = QPushButton("Correctness", self.control_buttons)
        self.corr_button.setGeometry(190, 10, 80, 50)
        self.corr_button.setStyleSheet(""".QPushButton {color: white; border-radius: 4px;background: rgb(255, 100, 100);}
                                     .QPushButton:pressed {color: white; border-radius: 4px;background: rgb(200, 75, 75);}""")
        self.corr_button.clicked.connect(self.compute_correctness_TS)

        self.trace_panel = QScrollArea(parent = self.control_panel)
        self.trace_panel.setGeometry(10,110,380,self.height - 220)
        self.trace_list = QListWidget(parent=self.trace_panel)
        self.trace_list.setGeometry(0,0,380,self.height-220)

        # initialize the plotting window
        print(QApplication.desktop().screenGeometry().height())
        print(self.height)
        self.reward_window = PlotWindow(self, self.width - self.width*0.2, 4*self.height/5.55, self.width*0.2, self.height/5.55)
        self.reward_window.setFrameShape(QFrame.Box)

        # initialize progress window
        self.progress_window = PlotWindow(self, self.width - self.width*0.2, 3*self.height/5.55, self.width*0.2, self.height/5.55)
        self.progress_window.setFrameShape(QFrame.Box)
        self.progress_window.set_title("progress over time")
        #self.progress_window.update_graph([])

        # initialize cost window
        self.cost_window = PlotWindow(self, self.width - self.width*0.2, 2*self.height/5.55, self.width*0.2, self.height/5.55)
        self.cost_window.setFrameShape(QFrame.Box)
        self.cost_window.set_title("cost over time")
        self.cost_window.set_ylabel("cost")
        #self.cost_window.update_graph([])

        # model checking window
        self.prop_window = PlotWindow(self, self.width - self.width*0.2, self.height/5.55, self.width*0.2, self.height/5.55)
        self.prop_window.setFrameShape(QFrame.Box)
        self.prop_window.set_title("ratio of props satisfied")
        self.prop_window.set_ylabel("ratio")
        #self.prop_window.update_graph([])

        # initialize distance window
        self.distance_window = PlotWindow(self, self.width - self.width*0.2, 0, self.width*0.2, self.height/5.55)
        self.distance_window.setFrameShape(QFrame.Box)
        self.distance_window.set_title("distance to original")
        self.distance_window.set_ylabel("distance")
        #self.distance_window.update_graph([])

        self.modification_label = QLabel(parent=self.control_panel)
        self.modification_label.setGeometry(10,self.height-290, 400,200)
        self.modification_label.setText("Modifications:")

    def set_mod_text(self, text):
        self.modification_label.setText("Modifications:\n{}".format(text))
        app.processEvents()

    def load_graph(self):
        url = QUrl.fromLocalFile("{}/d3js/example2.html".format(os.getcwd()))
        self.webView.load(url)

    def make_dimension_file(self):
        dimension_dict = {"width":self.width, "height":self.height, "font":16, "behaviors":False}
        with open('d3js/dimensions.json', 'w') as outfile:
            json.dump(dimension_dict, outfile)

    def update_trace_panel(self, traces):
        self.update_trace_panel_helper(traces)
        app.processEvents()

    def update_trace_panel_helper(self, traces):
        self.trace_list.clear()

        counter = 0
        for trajectory in traces:
            rew = traces[trajectory][0]
            rew_color = abs(max(-1,min(1,rew)))
            color = QColor(0, 0, 0, 0)
            if rew < 0:
                color = QColor(255,85,50,180*rew_color)
            elif rew > 0:
                color = QColor(57,255,20,180*rew_color)

            traj_label = ""
            if trajectory.is_correctness:
                if trajectory.is_prefix:
                    traj_label = "corr. prefix"
                else:
                    traj_label = " correctness"
            else:
                if trajectory.is_prefix:
                    traj_label = "natur. prefix"
                if trajectory.is_generated_prefix:
                    traj_label = "gener. prefix"
                else:
                    traj_label = " full traject"

            item = QListWidgetItem("{0:<0}. {1:<200}".format("{} {}".format(traj_label, counter), traces[trajectory][0]))
            item.setToolTip(str(trajectory))
            if traces[trajectory][1] == False:
                item.setForeground(QColor(0,0,0,100))
                item.setBackground(QColor(200,200,200))
            else:
                item.setBackground(QColor(color))

            counter += 1
            self.trace_list.addItem(item)

    def compute_inclusion(self):
        self.adapter.compute_inclusion(self.update_trace_panel, self.set_mod_text)

    def mcmc_adapt(self):
        self.adapter.mcmc_adapt(self.reward_window, self.progress_window, self.cost_window, self.prop_window, self.distance_window, self.update_trace_panel, self.set_mod_text)
        self.load_graph()

    def random_adapt(self):
        self.adapter.mcmc_adapt(self.reward_window, self.progress_window, self.cost_window, self.prop_window, self.distance_window, self.update_trace_panel, self.algorithm)
        self.load_graph()

    def z3_adapt(self):
        self.adapter.z3_adapt(self.reward_window, self.progress_window, self.cost_window, self.prop_window, self.distance_window, self.update_trace_panel)
        #self.json_exp.export_from_z3(solution)
        self.load_graph()

    def init_traj_builder(self):
        tb = TrajectoryBuilder(self.adapter.inputs, self.adapter.outputs)
        tb.exec_()
        rval = tb.rval
        if rval is None:
            return
        self.adapter.add_trajs(rval)

    def compute_correctness_TS(self):
        self.adapter.compute_correctness_TS()

if __name__ == "__main__":

    # start the GUI
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
