import os
import sys  
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel

class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        global calculation
        calculation = ""
        L1 = QLabel("")
        L2 = QLabel("")
        self.layout = QGridLayout(self)
        t = 0
        nums = ["0", "1", "2", "+", "3", "4", "5", "-", "6", "7", "8", "*", "9", "(", ")", "/", ".", "<-", "",
         ""]
        for row in range(2, 7):
            for col in range(4):
                button = QPushButton(nums[t])
                t += 1
                button.clicked.connect(lambda: self.buttonClicked(L1, L2))
                self.layout.addWidget(button, row, col)
        self.layout.addWidget(L1)
        self.layout.addWidget(L2)
        self.setWindowTitle("Cowlculator")
        self.show()

    def buttonClicked(self, L1, L2):
        os.system('cls')
        global calculation
        if self.sender().text() == "<-": calculation = calculation[:-1]
        else: calculation += self.sender().text()
        try:
            L1.setText(calculation)
            L2.setText(str(eval(calculation)))
        except:
            L1.setText(calculation)
            L2.setText("Err")

app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
