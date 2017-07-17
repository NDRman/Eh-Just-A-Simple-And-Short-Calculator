import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        global calculation
        calculation = ""
        self.layout = QGridLayout(self)
        t = 0
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-"]
        for row in range(4):
            for col in range(3):
                button = QPushButton(nums[t])
                t += 1
                button.clicked.connect(self.buttonClicked)
                self.layout.addWidget(button, row, col)
        self.setWindowTitle("Cowlculator")
        self.setGeometry(100, 100, 100, 100)
        self.setLayout(self.layout)
        self.show()

    def buttonClicked(self):
        clear = lambda: os.system('cls')
        clear()
        button = self.sender()
        global calculation
        calculation += button.text()
        try:
            print(calculation, "\n\n", "=" , eval(calculation))
        except:
            print(calculation)

app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
