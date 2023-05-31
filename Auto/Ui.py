import subprocess
from PyQt5.QtWidgets import QCommandLinkButton
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtWidgets import QWidget







class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1600,100,300,500)
        self.setFixedSize(300,500)
        self.setWindowTitle("SurveyBot")
        self.setStyleSheet("background: #141414;")
        self.show()
        self.ScreenText()
        self.Command()
        #self.subprocessVenv()
    def ScreenText(self):
        self.textLabel = QLabel(self)
        self.textLabel.setStyleSheet('color: #C4E0E5; font-family: Arial; font-size: 40px;')
        self.textLabel.setText("Survey Clone")
        self.textLabel.move(30,150)
        self.textLabel.show()
    def Command(self):
        self.commandButton = QCommandLinkButton("Activate",self)
        self.commandButton.setFixedSize(100,40)
        self.commandButton.clicked.connect(self.Script)
        self.commandButton.move(110,300)
        self.commandButton.setStyleSheet('color :#C4E0E5; font-size:15px;')
        self.commandButton.show()
    def Script(self):
        subprocess.run(["python3","/Users/Mac/Desktop/HtmlandCSSpractice/SurveyClone/Auto/Remote.py"])
app = QApplication([])
mainW = MainWindow()
mainW.show()
app.exec_()