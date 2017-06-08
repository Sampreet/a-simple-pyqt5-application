import json
import math
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from resources.layouts import *
from resources.variables import *


#####################################################################
#      The main GUI of Application inherited from QGridLayout       #
#####################################################################

class AppGUI(QMainWindow):
    # initialize the core components of the UI
    def __init__(self):
        # return the parent to AppGUI class
        super().__init__()
        # set up the application menu and status bar
        self.initMenuBar()
        self.initStatusBar()
        
        # configure the application frame
        self.resize(1024, 576)
        rect_frame = self.frameGeometry()
        # get the screen resolution to to locate its center point
        center_point = QDesktopWidget().availableGeometry().center()
        rect_frame.moveCenter(center_point)
        # set the top left of the app window to that of the rectangle
        self.move(rect_frame.topLeft())
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(APP_ICON))
        self.setStatusTip(MSG_READY)
        self.show()

    # initialize the menubar containing the new and exit options
    def initMenuBar(self):
        # create a menubar widget
        menu_bar_main = self.menuBar()
        menu_bar_main.setStatusTip(MENU_TIP)
        
        # associate a file menu to the menubar
        file_menu_main = menu_bar_main.addMenu('&File')
        # create the new option in the file menu and bind it to a handler
        action_new = QAction(QIcon(MENU_FILE_NEW_ICON), '&New', self)
        action_new.setShortcut(MENU_FILE_NEW_SHORTCUT)
        action_new.setStatusTip(MENU_FILE_NEW_TIP)
        action_new.triggered.connect(self.underConstruction)
        file_menu_main.addAction(action_new)

        # create the open option in the file menu and bind it to a handler
        action_new = QAction(QIcon(MENU_FILE_OPEN_ICON), '&Open', self)
        action_new.setShortcut(MENU_FILE_OPEN_SHORTCUT)
        action_new.setStatusTip(MENU_FILE_OPEN_TIP)
        action_new.triggered.connect(self.initLayout)
        file_menu_main.addAction(action_new)

        # create the exit option in the file menu and bind it to the closeEvent handler
        action_exit = QAction(QIcon(MENU_FILE_EXIT_ICON), '&Exit', self)
        action_exit.setShortcut(MENU_FILE_EXIT_SHORTCUT)
        action_exit.setStatusTip(MENU_FILE_EXIT_TIP)
        action_exit.triggered.connect(self.close)
        file_menu_main.addAction(action_exit)

    # initialize the status bar for the homepage
    def initStatusBar(self):
        self.statusBar().showMessage(MSG_WELCOME)
        # add a progress bar
        self.progress_bar = QProgressBar()
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.statusBar().showMessage(MSG_READY)
        
    # initialize the layout for the homepage
    def initLayout(self):
        # initilize the application layout
        self.layout_home = QGridLayout()
        # initialize the combo box for layout selection
        self.layout_home.label_select_layout = QLabel('Select the Layout to display: ')
        self.layout_home.label_select_layout.resize(self.layout_home.label_select_layout.sizeHint())
        self.layout_home.combo = QComboBox()
        self.layout_home.combo.addItems([LAYOUT_FIRST, LAYOUT_SECOND])
        self.layout_home.combo.setCurrentIndex(0)
        self.layout_home.addWidget(self.layout_home.label_select_layout, 0, 0)
        self.layout_home.addWidget(self.layout_home.combo, 0, 1)
        # create button to execute desired selection
        self.layout_home.btn_select = QPushButton(BTN_SELECT)
        self.layout_home.btn_select.setStatusTip(MSG_SELECT)
        self.layout_home.btn_select.resize(self.layout_home.btn_select.sizeHint())
        self.layout_home.btn_select.clicked.connect(self.toggleLayout)
        self.layout_home.addWidget(self.layout_home.btn_select, 1, 1)

        # create a widget to insert the layout into the main window
        self.widget_main = QWidget()
        # add the home layout as the central widget
        self.widget_main.setLayout(self.layout_home)
        self.setCentralWidget(self.widget_main)
        self.statusBar().showMessage(MSG_READY)

    # reimplement the event handler to modify the action of QCloseEvent
    def closeEvent(self, event):
        # display a dialog box before exiting the application
        response = QMessageBox.question(
            self, DIALOG_QUIT, DIALOG_QUIT_MSG, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # take action according to the response
        if response == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
    # display a dialog box for modules under construction
    def underConstruction(self):
        response = QMessageBox.information(self, DIALOG_CONSTRUCT, DIALOG_CONSTRUCT_MSG, QMessageBox.Ok, QMessageBox.Ok)
        
    # toggle layout on button click in the home page
    def toggleLayout(self):
        # conditional toggle upon selection
        if self.layout_home.combo.currentText() == LAYOUT_FIRST:
            # display the first layout
            widget = QWidget()
            layout = FirstLayout(self)
            widget.setLayout(layout)
            self.setCentralWidget(widget)
        elif self.layout_home.combo.currentText() == LAYOUT_SECOND:
            # display the second layout
            widget = QWidget()
            widget.setLayout(SecondLayout())
            self.setCentralWidget(widget)

# run the main loop of the application
if __name__ == '__main__':
    # create application object with command line arguments
    app = QApplication(sys.argv)
    gui = AppGUI()
    # initiate the main loop
    sys.exit(app.exec_())
