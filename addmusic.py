from PyQt5.QtWidgets import *

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle("Music Selector")

        QBtn = QDialogButtonBox.Cancel | QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout
        self.formLayout = QFormLayout()
        message = QLabel("Select Music File From Computer Or Using A Link")
        self.formLayout.addWidget(message)
        self.formLayout.addRow('Select from Computer', QLineEdit())
        self.formLayout.addRow('Select from Link', QLineEdit())
        self.formLayout.addWidget(self.buttonBox)
        self.setLayout(self.formLayout)