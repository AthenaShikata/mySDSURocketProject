from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QPushButton
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt
import sys


def latchingButton(self, operation, buttonlabel, style, xpos, ypos, width, height): # toggle
    testVar = True
    self.button = QPushButton(buttonlabel,self)
    self.button.setGeometry(xpos,ypos,width,height)
    self.button.setStyleSheet(style)
    self.button.clicked.connect(operation)
    return self.button


def momentaryButton(self, operation, buttonlabel, style, xpos, ypos, width, height): # toggles on / off when x amount of time passes
    testVar = True
    self.button = QPushButton(buttonlabel,self)
    self.button.setGeometry(xpos,ypos,width,height)
    self.button.setStyleSheet(style)
    self.button.clicked.connect(operation)
    return self.button





class mainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle('NI GUI')
        self.setGeometry(200,200,1200,900)
        self.setWindowIcon(QIcon('National_Instruments.png'))

        style = 'font-size: 40px;'

        self.button1 = latchingButton(self,self.printme,'Button1', style, 200,200,288*2,100*2)
        self.button2 = latchingButton(self,self.printme2,'Button2',style, 200,500,288*2,100*2)

        #self.initUI()

    def printme(self,testVar):
        print('me')
        testVar =  not testVar
        print(testVar)
    def printme2(self,testVar):
        print('me2')
        testVar = not testVar


    def onClick(self):
        print("Click")
        self.button.setText('Clicked')
        self.button.setDisabled(True)

        
        


def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()