import math
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from resources.variables import *


#####################################################################
#    			First Layout inherited from QGridLayout     		#
#####################################################################

class FirstLayout(QGridLayout):
    # initialize the super class and call the layout method
    def __init__(self, parent):
        super().__init__()
        self.window = parent
        self.setSpacing(5)
        self.initLayout()

    # initialize the layout
    def initLayout(self):
        # an entry field
        self.val_pi = QLineEdit()
        self.val_pi.setText('3.14159')
        self.addWidget(
            QLabel('Enter the value of Pi rounded to 5 decimal places: '), 0, 0)
        self.addWidget(self.val_pi, 0, 1)
        self.val_pi.setText('3.14159')

		# a combo box
        self.sel_pi = QComboBox()
        self.sel_pi.addItems(['3.14157', '3.14158', '3.14159', '3.14286'])
        self.addWidget(
            QLabel('Select the value of Pi rounded to 5 decimal places: '), 1, 0)
        self.addWidget(self.sel_pi, 1, 1)

       	# a push button to check the answers of the form
        self.btn_check = QPushButton('Check Answers')
		# display status tip on hover
        self.btn_check.setStatusTip(
            'Click on the button to check the answers.')
        self.btn_check.resize(self.btn_check.sizeHint())
		# execute a function on click
        self.btn_check.clicked.connect(self.checkAns)
        self.addWidget(self.btn_check, 3, 1)

       	# a push button to calibrate progress bar
        self.btn_calib = QPushButton('Calibrate Progress Bar')
		# display status tip on hover
        self.btn_calib.setStatusTip(
            'Click on the button to calibrate the progress bar.')
        self.btn_calib.resize(self.btn_calib.sizeHint())
		# execute a function on click
        self.btn_calib.clicked.connect(self.calibProg)
        self.addWidget(self.btn_calib, 4, 1)

    def checkAns(self):
        # initialize the x-axis variation type
        if self.sel_pi.currentIndex() == 2 and self.val_pi.text() == '3.14159':
            self.window.statusBar().showMessage('Correct Answer!')
            print('Correct Answer!')
        else:
            self.window.statusBar().showMessage('Wrong Answer!')
            print('Wrong Answer!')
        
    def calibProg(self):
        self.window.statusBar().showMessage(MSG_RUNNING)
        # iterate over various values
        for i in range(1, int(1000)+1):
            self.displayStatus(1, float(i/10))
        self.displayStatus(0, 0)

    def displayStatus(self, mode, val):
        if mode == 0:
            self.window.statusBar().showMessage(MSG_READY)
            self.window.progress_bar.reset()
        elif mode == 1:
            self.window.statusBar().showMessage(MSG_RUNNING)
            self.window.progress_bar.setValue(val)
        
#####################################################################
#    			Second Layout inherited from QGridLayout      		#
#####################################################################
class SecondLayout(QGridLayout):
    # initialize the super class and call the layout method
    def __init__(self):
        super().__init__()    
