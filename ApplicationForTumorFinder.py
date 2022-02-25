"""

Basic application for tumor finder.

Author: Tolga AY
Github: evnflow3
Mail: ecetolgaay@gmail.com

"""
import sys

from PyQt5 import QtWidgets            #Implenetaion of neccessary libraries.

import MyMethod

class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()                #The init function which is inheritaged by QtWidget

        self.init_ui()

    def init_ui(self):

        self.button1 = QtWidgets.QPushButton("Picture 1")
        self.button2 = QtWidgets.QPushButton("Picture 2")
        self.button3 = QtWidgets.QPushButton("Picture 3")        #The ui function for building the app and the button areas.
        self.button4 = QtWidgets.QPushButton("Picture 4")
        self.button5 = QtWidgets.QPushButton("Picture 5")




        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.button1)
        v_box.addWidget(self.button2)
        v_box.addWidget(self.button3)                   #Vertical boxes for buttons.
        v_box.addWidget(self.button4)
        v_box.addWidget(self.button5)


        v_box.addStretch()

        self.setLayout(v_box)
        self.button1.clicked.connect(self.click1)
        self.button2.clicked.connect(self.click2)
        self.button3.clicked.connect(self.click3)         #If someone clicks this buttons, run the click functions.
        self.button4.clicked.connect(self.click4)
        self.button5.clicked.connect(self.click5)

        self.show()

    def click1(self):
        self.button1 = MyMethod.TumorFinder("1.jpg", 5, 5,130)
    def click2(self):
        self.button2= MyMethod.TumorFinder("2.jpg", 5, 5,160)
    def click3(self):
        self.button3 = MyMethod.TumorFinder("3.jpg", 9, 9, 135)        #The click functions for buttons.
    def click4(self):
        self.button4 = MyMethod.TumorFinder("4resized.jpg", 9, 9, 110)
    def click5(self):
        self.button5 = MyMethod.TumorFinder("5.jpg", 9, 9, 115)



def App():

    app1 = QtWidgets.QApplication(sys.argv)
    pencere = Window()
    pencere.setWindowTitle("Application")         #Building the app with app function and calling the App() function.
    pencere.setGeometry(400, 600, 200, 150)
    sys.exit(app1.exec_())

App()
















