from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QPushButton
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt
import sys

# https://www.youtube.com/watch?v=92zx_U9Nzf4

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tutorialNum = 4
        # 1 Label and Pic
        # 2 Verticle Box Layout
        # 3 Grid Box Layout
        # 4 Button
        # 5 

        self.setWindowTitle('pyqt5 test')
        self.setGeometry(200,200,1200,900)
        self.setWindowIcon(QIcon('Chloe Gmail Profile Picture.jpg'))

        if self.tutorialNum == 1:
            label = QLabel('Hello',self)
            label.setFont(QFont('Arial',40))
            label.setGeometry(5,5,500,200)
            label.setStyleSheet('color: #FF0099;'
                                'background-color: Black;'
                                'font-weight: bold;'
                                'font-style: italic;'
                                'text-decoration: underline;')
            label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

            pic = QLabel(self)
            pic.setGeometry(0,300,500,500)
            pixmap = QPixmap('Chloe Gmail Profile Picture.jpg')
            pic.setPixmap(pixmap)
            pic.setScaledContents(True)
            pic.setGeometry((self.width()-pic.width()) // 2,(self.height()-pic.height()) // 2,pic.width(),pic.height())

        if self.tutorialNum == 4:
            self.button = QPushButton("Click Me!",self)
            #self.label = QLabel("Hello",self)
        
        
        self.initUI()

    def initUI(self):
        if self.tutorialNum == 2 or self.tutorialNum == 3:
            centralWidget = QWidget()
            self.setCentralWidget(centralWidget)

            label1 = QLabel('Number 1',self)
            label1.setStyleSheet('background-color: red;')
            label2 = QLabel('Number 2',self)
            label2.setStyleSheet('background-color: yellow;')
            label3 = QLabel('Number 3',self)
            label3.setStyleSheet('background-color: green;')
            label4 = QLabel('Number 4',self)
            label4.setStyleSheet('background-color: blue;')
            label5 = QLabel('Number 5',self)
            label5.setStyleSheet('background-color: purple;')

        if self.tutorialNum == 2:
            vbox = QVBoxLayout()
            vbox.addWidget(label1)
            vbox.addWidget(label2)
            vbox.addWidget(label3)
            vbox.addWidget(label4)
            vbox.addWidget(label5)
            centralWidget.setLayout(vbox)

        if self.tutorialNum == 3:
            grid = QGridLayout()
            grid.addWidget(label1,0,0)
            grid.addWidget(label2,0,1)
            grid.addWidget(label3,1,2)
            grid.addWidget(label4,2,0)
            grid.addWidget(label5,2,2)
            centralWidget.setLayout(grid)

        if self.tutorialNum == 4:
            self.button.setGeometry(200,200,288*2,100*2)
            self.button.setStyleSheet('font-size: 40px;')
            self.button.clicked.connect(self.onClick)
            self.label.setGeometry(200, 500, 250, 150)
            self.label.setStyleSheet('font-size: 50px;')
        
    def onClick(self):
        
        if self.tutorialNum == 4:
            print("Click")
            self.button.setText('Clicked')
            self.button.setDisabled(True)
            self.label.setText('Good Bye')




def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()