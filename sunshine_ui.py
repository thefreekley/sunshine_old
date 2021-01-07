# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sunshine.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 900)
        MainWindow.setMinimumSize(QtCore.QSize(400, 900))
        MainWindow.setMaximumSize(QtCore.QSize(400, 900))
        MainWindow.setStyleSheet("#left_area{\n"
"    background:black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 720))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.left_area = QtWidgets.QMdiArea(self.centralwidget)
        self.left_area.setGeometry(QtCore.QRect(0, -51, 21, 931))
        self.left_area.setStyleSheet("#tfk{\n"
"color:white;\n"
"}")
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.left_area.setBackground(brush)
        self.left_area.setObjectName("left_area")
        self.tfk = QtWidgets.QLabel(self.centralwidget)
        self.tfk.setGeometry(QtCore.QRect(1, 832, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setBold(True)
        font.setWeight(75)
        self.tfk.setFont(font)
        self.tfk.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tfk.setAutoFillBackground(False)
        self.tfk.setStyleSheet("#tfk{\n"
" color:white;\n"
" width:20px;\n"
"align-text:center;\n"
"margin-left:2px;\n"
"} ")
        self.tfk.setObjectName("tfk")
        self.big_label = QtWidgets.QLabel(self.centralwidget)
        self.big_label.setGeometry(QtCore.QRect(41, 0, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(-1)
        self.big_label.setFont(font)
        self.big_label.setAutoFillBackground(False)
        self.big_label.setStyleSheet("#big_label {\n"
"    font-size:45px;\n"
"}")
        self.big_label.setObjectName("big_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(43, 80, 3, 276))
        self.line.setStyleSheet("#line{\n"
"    width:1px;\n"
"    background:black;\n"
"    border:0px;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.back = QtWidgets.QMdiArea(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(10, 0, 400, 901))
        self.back.setStyleSheet("#back{\n"
"    z-index:0;\n"
"}")
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.back.setBackground(brush)
        self.back.setObjectName("back")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(300, 80, 22, 270))
        palette = QtGui.QPalette()
        self.verticalSlider.setPalette(palette)
        self.verticalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #999999;\n"
"height: 18px;\n"
"\n"
"border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 18px;\n"
" background-image: url(:/slider-knob.png)\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"background: lightgrey;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QSlider::sub-page:qlineargradient {\n"
"background: blue;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-left-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"}")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(360, 80, 22, 270))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        self.verticalSlider_2.setPalette(palette)
        self.verticalSlider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #999999;\n"
"height: 18px;\n"
"\n"
"border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 18px;\n"
" background-image: url(:/slider-knob.png)\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"background: lightgrey;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QSlider::sub-page:qlineargradient {\n"
"background: blue;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-left-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"}")
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.img_label = QtWidgets.QLabel(self.centralwidget)
        self.img_label.setGeometry(QtCore.QRect(268, 80, 31, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(34)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.img_label.sizePolicy().hasHeightForWidth())
        self.img_label.setSizePolicy(sizePolicy)
        self.img_label.setSizeIncrement(QtCore.QSize(13, 0))
        self.img_label.setStyleSheet("#img_label{\n"
"background-image:url(:/newPrefix/light.jpg);\n"
"}")
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        self.img_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.img_label_2.setGeometry(QtCore.QRect(330, 80, 31, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(34)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.img_label_2.sizePolicy().hasHeightForWidth())
        self.img_label_2.setSizePolicy(sizePolicy)
        self.img_label_2.setSizeIncrement(QtCore.QSize(13, 0))
        self.img_label_2.setStyleSheet("#img_label_2{\n"
"background-image:url(:/mus/mus.jpg);\n"
"}")
        self.img_label_2.setText("")
        self.img_label_2.setObjectName("img_label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(50, 70, 231, 301))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    border:0;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1.setGeometry(QtCore.QRect(0, 10, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(20)
        self.radioButton1.setFont(font)
        self.radioButton1.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:       2px;\n"
"    margin-right:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"}")
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton1_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1_2.setGeometry(QtCore.QRect(0, 70, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(20)
        self.radioButton1_2.setFont(font)
        self.radioButton1_2.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:       2px;\n"
"    margin-right:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"}")
        self.radioButton1_2.setObjectName("radioButton1_2")
        self.radioButton1_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1_3.setGeometry(QtCore.QRect(0, 130, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(20)
        self.radioButton1_3.setFont(font)
        self.radioButton1_3.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:       2px;\n"
"    margin-right:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"}")
        self.radioButton1_3.setObjectName("radioButton1_3")
        self.radioButton1_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1_4.setGeometry(QtCore.QRect(0, 190, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(20)
        self.radioButton1_4.setFont(font)
        self.radioButton1_4.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:       2px;\n"
"    margin-right:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"}")
        self.radioButton1_4.setObjectName("radioButton1_4")
        self.radioButton1_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1_5.setGeometry(QtCore.QRect(0, 250, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(20)
        self.radioButton1_5.setFont(font)
        self.radioButton1_5.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:       2px;\n"
"    margin-right:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"}")
        self.radioButton1_5.setObjectName("radioButton1_5")
        self.button_collor = QtWidgets.QToolButton(self.groupBox)
        self.button_collor.setGeometry(QtCore.QRect(108, 246, 31, 36))
        self.button_collor.setStyleSheet("#button_collor{\n"
"background-image:url(:/choose_color/choose_color.jpg);\n"
"border:0px;\n"
"shadow-box:0px;\n"
"width:20px;\n"
"heigth:20px;\n"
"}")
        self.button_collor.setText("")
        self.button_collor.setObjectName("button_collor")
        self.label_right = QtWidgets.QLabel(self.groupBox)
        self.label_right.setGeometry(QtCore.QRect(140, 243, 47, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_right.setFont(font)
        self.label_right.setStyleSheet("#label_right{\n"
"color:black;\n"
"}")
        self.label_right.setObjectName("label_right")
        self.label_left = QtWidgets.QLabel(self.groupBox)
        self.label_left.setGeometry(QtCore.QRect(92, 243, 16, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_left.setFont(font)
        self.label_left.setStyleSheet("#label_left{\n"
"color:black;\n"
"}")
        self.label_left.setObjectName("label_left")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 447, 361, 411))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    border:0;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton1_11 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton1_11.setGeometry(QtCore.QRect(0, 10, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(20)
        self.radioButton1_11.setFont(font)
        self.radioButton1_11.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:       2px;\n"
"    margin-right:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"}")
        self.radioButton1_11.setObjectName("radioButton1_11")
        self.radioButton1_12 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton1_12.setGeometry(QtCore.QRect(0, 70, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(20)
        self.radioButton1_12.setFont(font)
        self.radioButton1_12.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:       2px;\n"
"    margin-right:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"}")
        self.radioButton1_12.setObjectName("radioButton1_12")
        self.radioButton1_13 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton1_13.setGeometry(QtCore.QRect(0, 130, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(20)
        self.radioButton1_13.setFont(font)
        self.radioButton1_13.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:       2px;\n"
"    margin-right:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"}")
        self.radioButton1_13.setObjectName("radioButton1_13")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(0, 270, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Nexa Light")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("#comboBox{\n"
"    background:black;\n"
"    color:white;\n"
"    shadow:0px;\n"
"   border: 1px solid black;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  background-color: #373e4e;\n"
"  padding: 10px;\n"
"  /*selection-background-color: rgb(39, 44, 54); */\n"
"}\n"
"QComboBox::drop-down \n"
"{\n"
"    \n"
"    shadow:0px;\n"
"\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.big_label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.big_label_3.setGeometry(QtCore.QRect(0, 240, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(16)
        self.big_label_3.setFont(font)
        self.big_label_3.setAutoFillBackground(False)
        self.big_label_3.setStyleSheet("#big_label_2 {\n"
"    font-size:45px;\n"
"}")
        self.big_label_3.setObjectName("big_label_3")
        self.connect = QtWidgets.QPushButton(self.groupBox_2)
        self.connect.setGeometry(QtCore.QRect(220, 270, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.connect.setFont(font)
        self.connect.setStyleSheet("#connect{\n"
" border:0px;\n"
"background:white;\n"
"}\n"
"\n"
"#connect:pressed{\n"
"background:black;\n"
"color:white;\n"
"}")
        self.connect.setObjectName("connect")
        self.big_label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.big_label_4.setGeometry(QtCore.QRect(110, 376, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(-1)
        self.big_label_4.setFont(font)
        self.big_label_4.setAutoFillBackground(False)
        self.big_label_4.setStyleSheet("#big_label_4 {\n"
"    font-size:18px;\n"
"}")
        self.big_label_4.setObjectName("big_label_4")
        self.radioButton1_14 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton1_14.setGeometry(QtCore.QRect(0, 190, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(20)
        self.radioButton1_14.setFont(font)
        self.radioButton1_14.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:       2px;\n"
"    margin-right:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"}")
        self.radioButton1_14.setObjectName("radioButton1_14")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(0, 330, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Nexa Light")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("#comboBox_2{\n"
"    background:black;\n"
"    color:white;\n"
"    shadow:0px;\n"
"   border: 1px solid black;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  background-color: #373e4e;\n"
"  padding: 10px;\n"
"  /*selection-background-color: rgb(39, 44, 54); */\n"
"}\n"
"QComboBox::drop-down \n"
"{\n"
"    \n"
"    shadow:0px;\n"
"\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.big_label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.big_label_5.setGeometry(QtCore.QRect(0, 300, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(16)
        self.big_label_5.setFont(font)
        self.big_label_5.setAutoFillBackground(False)
        self.big_label_5.setStyleSheet("#big_label_2 {\n"
"    font-size:45px;\n"
"}")
        self.big_label_5.setObjectName("big_label_5")
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(200, 10, 15, 211))
        self.line_3.setStyleSheet("#line_3{\n"
"    width:1px;\n"
"    background:black;\n"
"    border:0px;\n"
"}")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.groupBox_2)
        self.line_4.setGeometry(QtCore.QRect(220, 10, 15, 211))
        self.line_4.setStyleSheet("#line_4{\n"
"    width:1px;\n"
"    background:black;\n"
"    border:0px;\n"
"}")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.groupBox_2)
        self.line_5.setGeometry(QtCore.QRect(240, 10, 15, 211))
        self.line_5.setStyleSheet("#line_5{\n"
"    width:1px;\n"
"    background:black;\n"
"    border:0px;\n"
"}")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.groupBox_2)
        self.line_6.setGeometry(QtCore.QRect(260, 10, 15, 211))
        self.line_6.setStyleSheet("#line_6{\n"
"    width:1px;\n"
"    background:black;\n"
"    border:0px;\n"
"}")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.groupBox_2)
        self.line_7.setGeometry(QtCore.QRect(280, 10, 15, 211))
        self.line_7.setStyleSheet("#line_7{\n"
"    width:1px;\n"
"    background:black;\n"
"    border:0px;\n"
"}")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.groupBox_2)
        self.line_8.setGeometry(QtCore.QRect(300, 10, 15, 211))
        self.line_8.setStyleSheet("#line_8{\n"
"    width:1px;\n"
"    background:black;\n"
"    border:0px;\n"
"}")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.groupBox_2)
        self.line_9.setGeometry(QtCore.QRect(320, 10, 15, 211))
        self.line_9.setStyleSheet("#line_9{\n"
"    width:1px;\n"
"    background:black;\n"
"    border:0px;\n"
"}")
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.groupBox_2)
        self.line_10.setGeometry(QtCore.QRect(180, 10, 15, 211))
        self.line_10.setStyleSheet("#line_10{\n"
"    width:1px;\n"
"    background:black;\n"
"    border:0px;\n"
"}")
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.groupBox_2)
        self.line_11.setGeometry(QtCore.QRect(179, 220, 158, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 230, 157, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adderley Bold")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adderley")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adderley")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adderley")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adderley")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adderley")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adderley")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adderley")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(337, 234, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Adderley")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(180, 184, 156, 51))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton1_15 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton1_15.setGeometry(QtCore.QRect(-4, 29, 235, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(20)
        self.radioButton1_15.setFont(font)
        self.radioButton1_15.setStyleSheet("QRadioButton {\n"
"\n"
"}\n"
"\n"
"#radioButton1_15::indicator {\n"
"    width:                  160px;\n"
"    height:                 4px;\n"
"    border-radius:       1px;\n"
"    margin-right:8px;\n"
"}\n"
"\n"
"#radioButton1_15::indicator:checked {\n"
"    background-color:       black;\n"
"    border:                 1px solid white;\n"
"}\n"
"\n"
"#radioButton1_15::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 1px solid black;\n"
"}")
        self.radioButton1_15.setText("")
        self.radioButton1_15.setObjectName("radioButton1_15")
        self.big_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.big_label_2.setGeometry(QtCore.QRect(41, 380, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(-1)
        self.big_label_2.setFont(font)
        self.big_label_2.setAutoFillBackground(False)
        self.big_label_2.setStyleSheet("#big_label_2 {\n"
"    font-size:45px;\n"
"}")
        self.big_label_2.setObjectName("big_label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(42, 460, 3, 211))
        self.line_2.setStyleSheet("#line_2{\n"
"    width:1px;\n"
"    background:black;\n"
"    border:0px;\n"
"}")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.back.raise_()
        self.left_area.raise_()
        self.big_label.raise_()
        self.line.raise_()
        self.tfk.raise_()
        self.verticalSlider.raise_()
        self.verticalSlider_2.raise_()
        self.img_label.raise_()
        self.img_label_2.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.big_label_2.raise_()
        self.line_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tfk.setText(_translate("MainWindow", "TFK"))
        self.big_label.setText(_translate("MainWindow", "COLOR THEME"))
        self.radioButton1.setText(_translate("MainWindow", "Rainbow"))
        self.radioButton1_2.setText(_translate("MainWindow", "fire"))
        self.radioButton1_3.setText(_translate("MainWindow", "fireplase"))
        self.radioButton1_4.setText(_translate("MainWindow", "circular rainbow"))
        self.radioButton1_5.setText(_translate("MainWindow", "color"))
        self.label_right.setText(_translate("MainWindow", "▶"))
        self.label_left.setText(_translate("MainWindow", "◀"))
        self.radioButton1_11.setText(_translate("MainWindow", "to the bottom"))
        self.radioButton1_12.setText(_translate("MainWindow", "to the top"))
        self.radioButton1_13.setText(_translate("MainWindow", "by tone"))
        self.big_label_3.setText(_translate("MainWindow", "COMP:"))
        self.connect.setText(_translate("MainWindow", "update"))
        self.big_label_4.setText(_translate("MainWindow", "Sunshine 2021"))
        self.radioButton1_14.setText(_translate("MainWindow", "none"))
        self.big_label_5.setText(_translate("MainWindow", "audio input:"))
        self.label_8.setText(_translate("MainWindow", "20"))
        self.label_7.setText(_translate("MainWindow", "64"))
        self.label_6.setText(_translate("MainWindow", "125"))
        self.label_5.setText(_translate("MainWindow", "250"))
        self.label_4.setText(_translate("MainWindow", "500"))
        self.label_3.setText(_translate("MainWindow", "1k"))
        self.label_2.setText(_translate("MainWindow", "2k"))
        self.label.setText(_translate("MainWindow", "3k"))
        self.label_9.setText(_translate("MainWindow", "Hz"))
        self.big_label_2.setText(_translate("MainWindow", "MUSIC THEME"))

