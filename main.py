import sys
from PyQt5.QtWidgets import QApplication,QWidget,QColorDialog,QPushButton
from PyQt5 import uic,QtGui,QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
import serial
import time
import os
import sunshine_ui
import img

mode_theme = 0
mode_music = 0
lvl_light = 0
lvl_tone = 0
color = (255,0,255)
ser = ''

serial_ports = []
current_serial_port = ""

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

import comp
class App(QtWidgets.QMainWindow,sunshine_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start()
        self.set_radiobutton()



    def start(self):

        self.setWindowTitle("sunshine")
        self.setWindowIcon(QIcon(':/acces/logo.ico'))
        self.setWindowIcon(QIcon(':/acces/logo.ico'))

        self.img_label_2.setPixmap(QPixmap(":/acces/mus.jpg"))
        self.img_label.setPixmap(QPixmap(":/acces/light.jpg"))
        self.button_collor.setIcon(QIcon(QPixmap(":/acces/choose_color.jpg")))

        self.button_collor.setToolTip('Opens color dialog')
        self.button_collor.clicked.connect(lambda :self._slotPOIColorSelectionTriggered())

        self.connect.clicked.connect(lambda:self.update_serial_ports())
        self.comboBox.currentIndexChanged.connect(lambda:self.set_combobox(self.comboBox.currentText()))

        self.verticalSlider.setMinimum(5)
        self.verticalSlider.setMaximum(127)
        self.verticalSlider.setValue(127)
        self.verticalSlider.valueChanged.connect(lambda: self.set_light(self.verticalSlider))

        self.verticalSlider_2.setMinimum(-1)
        self.verticalSlider_2.setMaximum(250)
        self.verticalSlider_2.valueChanged.connect(lambda: self.set_tone(self.verticalSlider_2))


        self.show()

    def set_radiobutton(self):
        self.radioButton1.setChecked(True)
        self.radioButton1_14.setChecked(True)

        self.check_radiobutton(self.radioButton1,1,self.click_color_theme)
        self.check_radiobutton(self.radioButton1_2, 2,self.click_color_theme)
        self.check_radiobutton(self.radioButton1_3, 3,self.click_color_theme)
        self.check_radiobutton(self.radioButton1_4, 4,self.click_color_theme)
        self.check_radiobutton(self.radioButton1_5, 5,self.click_color_theme)

        self.check_radiobutton(self.radioButton1_11, 1 ,self.click_music_theme)
        self.check_radiobutton(self.radioButton1_12, 2 ,self.click_music_theme)
        self.check_radiobutton(self.radioButton1_13, 3 ,self.click_music_theme)
        self.check_radiobutton(self.radioButton1_14, 4 ,self.click_music_theme)

    def set_light(self,slider):
        global ser
        global lvl_light
        lvl_light = slider.value()
        string = str(chr(lvl_light)).encode('ascii')
        if ser:
            print(string,ord(string))
            ser.write(str(chr(1)).encode('ascii'))
            time.sleep(0.001)
            ser.write(string)



    def set_tone(self, slider):
        global lvl_tone
        lvl_tone = slider.value()




    def set_combobox(self,newText):
        global current_serial_port
        global ser
        current_serial_port = newText

        try:
            ser = serial.Serial(current_serial_port, 9600)
        except serial.SerialException:
            print
            "failed to write to port %s" % current_serial_port
            sys.exit()


    def check_radiobutton(self,radiobutton,num,key):
        radiobutton.toggled.connect(lambda: key(radiobutton,num))

    def click_color_theme(self,radiobutton,num):
        global mode_theme
        if radiobutton.isChecked() == True:
            mode_theme = num

            global ser
            string = str(chr(mode_theme + 5)).encode('ascii')
            if ser:
                print(string, ord(string))
                ser.write(str(chr(2)).encode('ascii'))
                time.sleep(0.001)
                ser.write(string)


    def click_music_theme(self, radiobutton, num):
        global mode_music
        if radiobutton.isChecked() == True:
            mode_music = num


    def update_serial_ports(self):
        global serial_ports
        global current_serial_port
        serial_ports = comp.serial_ports()
        self.comboBox.clear()
        for port in serial_ports:
            self.comboBox.addItem(port)


    @QtCore.pyqtSlot()
    def _slotPOIColorSelectionTriggered(self):
        global color
        check_color = QColorDialog.getColor()

        self.label_right.setStyleSheet(f'color:{check_color.name()}')
        self.label_left.setStyleSheet(f'color:{check_color.name()}')

        color = check_color.getRgb()

        global ser


        if ser:

            print("chelnз")
            ser.write(str(chr(3)).encode('ascii'))
            time.sleep(0.002)
            ser.write(str(chr( checkUnits(color[0],1)) ).encode('ascii'))
            time.sleep(0.002)
            ser.write(str(chr(3)).encode('ascii'))
            time.sleep(0.002)
            ser.write(str(chr(checkUnits(color[0],2))).encode('ascii'))
            time.sleep(0.002)

            ser.write(str(chr(3)).encode('ascii'))
            time.sleep(0.002)
            ser.write(str(chr(checkUnits(color[1], 1))).encode('ascii'))
            time.sleep(0.002)
            ser.write(str(chr(3)).encode('ascii'))
            time.sleep(0.002)
            ser.write(str(chr(checkUnits(color[1], 2))).encode('ascii'))
            time.sleep(0.002)

            ser.write(str(chr(3)).encode('ascii'))
            time.sleep(0.002)
            ser.write(str(chr(checkUnits(color[2], 1))).encode('ascii'))
            time.sleep(0.002)
            ser.write(str(chr(3)).encode('ascii'))
            time.sleep(0.002)
            ser.write(str(chr(checkUnits(color[2], 2))).encode('ascii'))
            time.sleep(0.002)


def checkUnits(num,unit):
    if unit == 1: return int(num/10) + 5
    if unit == 2: return num - int(num / 10)*10 + 5


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.update_serial_ports()
    app.exec_()