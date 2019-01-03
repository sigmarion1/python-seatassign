import sys
from PyQt5.QtWidgets import *
import random


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("자리배치 프로그램 v1.0")

        self.setGeometry(800, 200, 900, 700)
        # self.setFixedSize(1000, 800)

        self.principalLayout = QHBoxLayout(self)

        self.leftFrame = QFrame(self)
        self.leftFrame.resize(10,10)
        self.leftFrame.setObjectName("lf")
        self.leftFrame.setStyleSheet("""
            QFrame#lf{
            background-image: url(./classroom.png);
            }
        """)

        self.verticalLayoutL = QVBoxLayout(self.leftFrame)
        self.gridLayout = QGridLayout()

        self.gridLayout.setSpacing(20)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(6, 2)

        self.gridLayout.setRowStretch(0,20)
        self.gridLayout.setRowStretch(7,2)

        self.lbArray = list()

        for i in range(6):
            for j in range(5):
                self.lb = QLabel(self)
                self.lbArray.append(self.lb)
                self.lb.setText(str(i*5 + j))
                self.lb.setStyleSheet("""
                    background-color: rgba(100, 255, 255, 105);
                    color: white;
                    font : 70px;
                    text-align: center;
                    border: 3px solid green;
                    border-radius: 10px;
                    border-style: inset;
                """)

                self.gridLayout.addWidget(self.lb, i+1, j+1)


        self.verticalLayoutL.addLayout(self.gridLayout)
        self.verticalLayoutL.setSpacing(10)

        self.principalLayout.addWidget(self.leftFrame)

        self.verticalLayoutR = QVBoxLayout()
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)

        self.lb1 = QLabel()
        self.lb1.setText("남학생")
        self.gridLayout.addWidget(self.lb1, 0, 0)

        self.sp1 = QSpinBox()
        self.gridLayout.addWidget(self.sp1, 0, 1)
        self.sp1.setValue(10)
        self.sp1.setSingleStep(1)
        self.sp1.setMinimum(0)
        self.sp1.setMaximum(100)

        self.lb2 = QLabel()
        self.lb2.setText("여학생")
        self.gridLayout.addWidget(self.lb2, 1, 0)

        self.sp2 = QSpinBox()
        self.gridLayout.addWidget(self.sp2, 1, 1)
        self.sp2.setValue(10)
        self.sp2.setSingleStep(1)
        self.sp2.setMinimum(0)
        self.sp2.setMaximum(100)

        self.lb3 = QLabel()
        self.lb3.setText("결번(/구분)")
        self.gridLayout.addWidget(self.lb3, 2, 0)

        self.le = QLineEdit()
        self.gridLayout.addWidget(self.le, 2, 1)

        self.verticalLayoutR.addLayout(self.gridLayout)

        self.bt1 = QPushButton()
        self.bt1.setText("자리배치")
        self.bt1.clicked.connect(self.button_clicked)
        self.verticalLayoutR.addWidget(self.bt1)

        self.spacerItem = QSpacerItem(100 , 700, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.verticalLayoutR.addSpacerItem(self.spacerItem)

        self.principalLayout.addLayout(self.verticalLayoutR)
        self.principalLayout.setSpacing(10)



    def button_clicked(self):


        for i in range(6):
            for j in range(5):
                self.lbArray[i * 5 + j].setStyleSheet("""
                    background-color: yellow;
                    font: bold 40px;
                    """)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()