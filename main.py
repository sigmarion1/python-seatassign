import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
import random

MAX_SEAT = 30
MAX_MAN = 30
MAX_WOMAN = 30



class MyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.stdArray = []
        self.delArray = []
        self.seatArray = []

        self.setWindowTitle("자리배치 프로그램 v1.0")

        self.setGeometry(800, 200, 800, 600)
        self.setFixedSize(1000, 800)

        self.principalLayout = QHBoxLayout(self)

        self.leftFrame = QFrame(self)
        # self.leftFrame.resize(1000,1000)
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

                self.lb.setText(str(i*5 + j + 1))
                self.lb.setStyleSheet("""
                    background-color: rgba(100, 255, 255, 0);
                    color: white;
                    font : 70px;
                    text-align: center;
                    border: 3px solid burlywood;
                    border-radius: 10px;
                    border-style: inset;
                """)
                self.lb.setFixedWidth(130)
                self.lb.setFixedHeight(70)
                self.lb.setAlignment(Qt.AlignCenter)
                self.lbArray.append(self.lb)
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
        self.sp1.setMaximum(MAX_MAN)

        self.lb2 = QLabel()
        self.lb2.setText("여학생")
        self.gridLayout.addWidget(self.lb2, 1, 0)

        self.sp2 = QSpinBox()
        self.gridLayout.addWidget(self.sp2, 1, 1)
        self.sp2.setValue(10)
        self.sp2.setSingleStep(1)
        self.sp2.setMinimum(0)
        self.sp2.setMaximum(MAX_WOMAN)

        self.lb3 = QLabel()
        self.lb3.setText("결번(/구분)")
        self.gridLayout.addWidget(self.lb3, 2, 0)

        self.le = QLineEdit()
        self.gridLayout.addWidget(self.le, 2, 1)

        self.verticalLayoutR.addLayout(self.gridLayout)

        self.bt1 = QPushButton()
        self.bt1.setText("자리배치")
        self.bt1.clicked.connect(self.set_button)
        self.verticalLayoutR.addWidget(self.bt1)

        self.spacerItem = QSpacerItem(100 , 700, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.verticalLayoutR.addSpacerItem(self.spacerItem)

        self.principalLayout.addLayout(self.verticalLayoutR)
        self.principalLayout.setSpacing(10)

    def set_button(self):
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()
        QTimer.singleShot(800, self.button_clicked);
        self.button_clicked()

    def button_clicked(self):

        self.init_array()
        self.parse_del()
        self.student_list()
        self.assign_seat()
        self.print_seat()

    def init_array(self):
        del self.stdArray[:]
        del self.delArray[:]
        del self.seatArray[:]

        for i in range(MAX_SEAT):
            self.seatArray.append(' ')

    def parse_del(self):
        delText = self.le.text()
        self.delArray = delText.split('/')
        print(self.delArray)

    def student_list(self):

        manval = self.sp1.value()
        womanval = self.sp2.value()

        print(manval)
        for i in range(manval):
            self.stdArray.append(str(i+1))

        for i in range(womanval):
            self.stdArray.append(str(i+21))

        for i in self.delArray:
            if self.stdArray.count(i):
                self.stdArray.remove(i)

        print(self.stdArray)

    def assign_seat(self):

        tempArray = []

        while self.stdArray:
            temp = random.choice(self.stdArray)
            self.stdArray.remove(temp)
            tempArray.append(temp)

        self.stdArray.extend(tempArray)

        print(self.stdArray)

    def print_seat(self):

        mcnt = len(self.stdArray)
        cnt = 0

        print(self.stdArray[0])
        for i in range(6):
            for j in range(5):
                if cnt < mcnt:
                    self.lbArray[i * 5 + j].setText(self.stdArray[cnt])
                    if int(self.stdArray[cnt]) <= 20:
                        self.lbArray[i * 5 + j].setStyleSheet("""
                            background-color: rgba(0, 173, 181, 100);
                            color: white;
                            font : 70px;
                            border-radius: 10px;
                        """)

                    else:
                        self.lbArray[i * 5 + j].setStyleSheet("""
                            background-color: rgba(252, 60, 60, 100);
                            color: white;
                            font : 70px;
                            border-radius: 10px;
                        """)
                else:
                    self.lbArray[i * 5 + j].setText('')
                    self.lbArray[i * 5 + j].setStyleSheet("""
                        background-color: rgba(252, 60, 60, 0);
                        color: white;
                        font : 70px;
                        border-radius: 10px;
                    """)

                cnt = cnt + 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()