import sys
from PyQt5.QtWidgets import *

import addmusic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PiMusic Audio Player")

        button = QPushButton("Add Musics")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        self.showMaximized()

    def button_clicked(self, s):
        print("click", s)

        dlg = addmusic.CustomDialog()
        if dlg.exec_():
            print("Music Selected")
        else:
            print("Canceled")

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()