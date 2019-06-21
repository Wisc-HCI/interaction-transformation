from interaction_components import *
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QScrollArea, QGroupBox, QGridLayout, QSpinBox

class TrajectoryBuilder(QDialog):

    def __init__(self, ins, outs):
        super(TrajectoryBuilder, self).__init__()
        self.window_width = 800
        self.window_height = 550
        self.resize(self.window_width, self.window_height)
        self.setWindowTitle("Build a trajectory")

        # init traj scroll pane
        self.traj_scroll = QScrollArea(self)
        self.traj_scroll.setGeometry(10, 10, 780, 280)
        self.traj_scroll.setWidgetResizable(False)
        self.traj_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.traj_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # grid layout to go within traj_scroll
        self.groupbox = QGroupBox("Trajectories")
        self.grid_layout = QGridLayout()
        self.groupbox.setLayout(self.grid_layout)
        self.num_rows = 0
        self.groupbox.setGeometry(10, 10, 780, 40 + 30*self.num_rows)
        '''
        self.grid_layout.addWidget(QPushButton('1'),0,0)
        self.grid_layout.addWidget(QPushButton('2'),0,1)
        self.grid_layout.addWidget(QPushButton('3'),0,2)
        self.grid_layout.addWidget(QPushButton('4'),1,0)
        self.grid_layout.addWidget(QPushButton('5'),1,1)
        self.grid_layout.addWidget(QPushButton('6'),1,2)
        self.grid_layout.addWidget(QPushButton('7'),2,0)
        self.grid_layout.addWidget(QPushButton('8'),2,1)
        self.grid_layout.addWidget(QPushButton('9'),2,2)
        '''

        # init builder scroll pane
        self.build_scroll = QScrollArea(self)
        self.build_scroll.setGeometry(10, 300, 780, 90)
        self.build_scroll.setWidgetResizable(False)
        self.build_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.build_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # init human/micro io scroll pane
        self.io_scroll = QScrollArea(self)
        self.io_scroll.setGeometry(10, 400, 780, 90)
        self.io_scroll.setWidgetResizable(False)
        self.io_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.io_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # setup the okay and cancel buttons
        self.okay = QPushButton("Okay", parent=self)
        self.okay.setGeometry(355, 510, 40, 30)
        self.okay.setStyleSheet(""".QPushButton {color: white; border-radius: 4px;background: rgb(100, 100, 100);}
                                     .QPushButton:pressed {color: white; border-radius: 4px;background: rgb(150, 150, 150);}""")
        self.okay.clicked.connect(self.on_okay)

        self.cancel = QPushButton("Cancel", parent=self)
        self.cancel.setGeometry(405, 510, 40, 30)
        self.cancel.setStyleSheet(""".QPushButton {color: white; border-radius: 4px;background: rgb(100, 100, 100);}
                                     .QPushButton:pressed {color: white; border-radius: 4px;background: rgb(150, 150, 150);}""")
        self.cancel.clicked.connect(self.on_cancel)

        self.inputs = ins.alphabet
        self.inputs["leave"] = -1
        self.outputs = outs.alphabet
        self.outputs["END"] = -1

        # populate the io pane with the human inputs
        self.button_to_text = {}
        self.text_to_buttons = {}
        for inp in self.inputs:
            button = QPushButton(inp, parent=self.io_scroll)
            self.button_to_text[button] = inp
            self.text_to_buttons[inp] = button
            button.setStyleSheet(""".QPushButton {color: white; border-radius: 4px;background: rgb(0, 150, 150);}
                                         .QPushButton:pressed {color: white; border-radius: 4px;background: rgb(0, 100, 100);}""")
            button.clicked.connect(partial(self.add_hum_in, inp))
        for out in self.outputs:
            button = QPushButton(out, parent=self.io_scroll)
            self.button_to_text[button] = out
            self.text_to_buttons[out] = button
            button.hide()
            button.setStyleSheet(""".QPushButton {color: white; border-radius: 4px;background: rgb(150, 150, 150);}
                                         .QPushButton:pressed {color: white; border-radius: 4px;background: rgb(100, 100, 100);}""")
            button.clicked.connect(partial(self.add_rob_out, out))
        self.populate_hum_in()

        self.rval = None
        self.trajs = []
        self.curr_traj = []
        self.curr_hum_in = None
        self.curr_traj_text = ""

        self.curr_traj_label = QLabel(self.curr_traj_text, self.build_scroll)
        self.curr_traj_label.setGeometry(10,10,1000,90)
        self.build_scroll.setWidget(self.curr_traj_label)

        self.traj_label_text = ""
        self.trajs_label = QLabel(self.traj_label_text)
        self.trajs_label.setGeometry(10,10,1000,90)
        self.traj_scroll.setWidget(self.groupbox)

        self.traj2spin = {}

    def populate_hum_in(self):
        curr_x = -70
        curr_y = 10
        counter = 0
        for inp in self.inputs:

            if counter%2 == 0:
                curr_y = 10
                curr_x += 80
            else:
                curr_y = 45

            button = self.text_to_buttons[inp]
            button.setGeometry(curr_x, curr_y, 70, 30)
            button.show()

            counter += 1

    def populate_rob_out(self):
        curr_x = -70
        curr_y = 10
        counter = 0
        for out in self.outputs:
            if counter%2 == 0:
                curr_y = 10
                curr_x += 80
            else:
                curr_y = 45

            button = self.text_to_buttons[out]
            button.setGeometry(curr_x, curr_y, 70, 30)
            button.show()

            counter += 1

    def add_hum_in(self, inp):
        if inp == "leave":
            self.package_traj(prefix=True)
        else:
            self.curr_hum_in = HumanInput(inp)
            self.curr_traj_text += "( {} > ".format(inp)
            self.curr_traj_label.setText(self.curr_traj_text)

            for i in self.inputs:
                button = self.text_to_buttons[i]
                button.hide()

            self.populate_rob_out()

    def add_rob_out(self, out):
        micro = Microinteraction(out)
        self.curr_traj_text += "{} ) --> ".format(out)
        self.curr_traj_label.setText(self.curr_traj_text)

        for o in self.outputs:
            button = self.text_to_buttons[o]
            button.hide()

        tup = (self.curr_hum_in, micro)
        self.curr_traj.append(tup)

        if out == "END":
            self.package_traj()

        self.populate_hum_in()

    def package_traj(self, prefix=False):
        self.curr_traj_text = ""
        self.curr_traj_label.setText(self.curr_traj_text)

        new_traj = Trajectory(self.curr_traj,0.0,prefix,False)
        self.trajs.append(new_traj)
        self.traj_label_text += (str(new_traj) + "\n")
        self.trajs_label.setText(self.traj_label_text)
        self.curr_traj = []

        sb = QSpinBox()
        sb.setMinimum(-1.0)
        sb.setMaximum(1.0)

        self.traj2spin[new_traj] = sb

        self.grid_layout.addWidget(sb,self.num_rows,0)
        self.grid_layout.addWidget(QLabel(str(new_traj)),self.num_rows,1)
        self.num_rows += 1
        self.groupbox.setGeometry(10, 10, 780, 40 + 30*self.num_rows)

    def session(self):
        trajs = []
        while True:

            command = input("what do you want to do? (build/exit)")
            if command == "exit":
                break
            elif command == "build":
                pass
            else:
                continue

            trajectory = self.build_trajectory()
            trajs.append(trajectory)

        return trajs

    def build_trajectory(self):
        starter_input = HumanInput("Ready")
        starter_micro = Microinteraction("Greeting")

        vect = [(starter_input, starter_micro)]
        is_prefix = False
        is_correctness = False
        score = 0

        while True:

            hum_inp = input("human input? (exit to create prefix)")
            if hum_inp == "exit":
                score = float(input("score? (-1.0, 0.0, 1.0)"))
                is_prefix = True
                break

            rob_out = input("robot output? (END to end)")
            if rob_out == "END":
                score = float(input("score? (-1.0, 0.0, 1.0)"))
                break

        return Trajectory(vect,score,is_prefix,is_correctness)

    def on_okay(self):
        self.rval = self.trajs
        for traj in self.trajs:
            traj.reward = self.traj2spin[traj].value()
        self.close()

    def on_cancel(self):
        self.close()
