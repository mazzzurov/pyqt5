from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
main = QWidget()
main.setWindowTitle('Simple Calculator')
main.resize(200, 500)

btn_1 = QPushButton('1')
btn_2 = QPushButton('2')
btn_3 = QPushButton('3')
btn_4 = QPushButton('4')
btn_5 = QPushButton('5')
btn_6 = QPushButton('6')
btn_7 = QPushButton('7')
btn_8 = QPushButton('8')
btn_9 = QPushButton('9')
btn_0 = QPushButton('0')

btn_plus = QPushButton('+')
btn_minus = QPushButton('-')
btn_umn = QPushButton('*')
btn_del = QPushButton(':')

layout_main = QHBoxLayout(spacing = 0)

layout_btn1 = QVBoxLayout(spacing = 0)
layout_btn1.addStretch(50)
layout_btn1.addWidget(btn_3)
layout_btn1.addWidget(btn_2)
layout_btn1.addWidget(btn_1)


layout_btn2 = QVBoxLayout(spacing = 0)
layout_btn2.addStretch(50)
layout_btn2.addWidget(btn_6)
layout_btn2.addWidget(btn_5)
layout_btn2.addWidget(btn_4)

layout_btn3 = QVBoxLayout(spacing = 0)
layout_btn3.addStretch(50)
layout_btn3.addWidget(btn_9)
layout_btn3.addWidget(btn_8)
layout_btn3.addWidget(btn_7)

layout_btn4 = QVBoxLayout()
layout_btn4.addStretch(50)
layout_btn4.addWidget(btn_plus)
layout_btn4.addWidget(btn_minus)
layout_btn4.addWidget(btn_umn)
layout_btn4.addWidget(btn_del)

layout_main.addLayout(layout_btn1)
layout_main.addLayout(layout_btn2)
layout_main.addLayout(layout_btn3)
layout_main.addLayout(layout_btn4)

main.setLayout(layout_main)
main.show()
app.exec_()
