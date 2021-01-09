import sys
from PyQt5.QtWidgets import QApplication,QWidget,QColorDialog,QPushButton
from PyQt5 import uic,QtGui,QtCore
from PyQt5.QtGui import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QThread,QTimer
from PyQt5 import QtWidgets
import serial
import os
import sunshine_ui
import img
import time
import comp
from amplitude_level import AmplitudeLevel



audio_index = 3
mode_theme = 0
mode_music = 4
lvl_light = 0
lvl_tone = 100
color = (255,0,255)
ser = ''

serial_ports = []
current_serial_port = ""

audio_input = AmplitudeLevel()
fft_out = [0]*len(audio_input.get_fft())
flag_equalizer = False

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)


class AmplitudeLevel(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.old = 0


    def run(self):
        global audio_input
        global fft_out
        global lvl_tone
        while True:

            if mode_music != 4:

                a = int(audio_input.listen())

                amplitude_filter = mapping(a,6001 - lvl_tone,30)



                amplitude_filter= int(amplitude_filter * 1.5) +5

                if amplitude_filter>60:
                    amplitude_filter=60

                ser.write(str(chr(4)).encode('ascii'))
                ser.write(str(chr(amplitude_filter)).encode('ascii'))


class AmplitudeFFT(QThread):

    def __init__(self):
        QThread.__init__(self)



    def run(self):
        global audio_input
        global fft_out
        global flag_equalizer

        while True:
            if flag_equalizer:
                fft_out = audio_input.get_fft()

            time.sleep(0.06)








class App(QtWidgets.QMainWindow,sunshine_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.level_amplitude = AmplitudeLevel()
        self.level_amplitude.start()

        self.fft_amplitude = AmplitudeFFT()
        self.fft_amplitude.start()

        self.setupUi(self)
        self.start()
        self.set_radiobutton()
        self.timer = QTimer()
        self.timer.timeout.connect(self.set_equalizer)
        self.timer.start(30)



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
        self.comboBox.currentIndexChanged.connect(lambda:self.set_combobox_ser(self.comboBox.currentText()))

        self.comboBox_2.currentIndexChanged.connect(lambda: self.set_combobox_audio(self.comboBox_2.currentText()))

        self.verticalSlider.setMinimum(5)
        self.verticalSlider.setMaximum(127)
        self.verticalSlider.setValue(127)
        self.verticalSlider.valueChanged.connect(lambda: self.set_light(self.verticalSlider))

        self.verticalSlider_2.setMinimum(100)
        self.verticalSlider_2.setMaximum(6000)
        self.verticalSlider_2.setValue(1750)

        self.verticalSlider_2.valueChanged.connect(lambda: self.set_tone(self.verticalSlider_2))


        self.show()

    def set_radiobutton(self):
        self.radioButton1.setChecked(True)
        self.radioButton1_14.setChecked(True)

        self.radioButton1_15.setChecked(False)
        self.radioButton1_15.toggled.connect(lambda: self.equalizer_check())

        self.check_radiobutton(self.radioButton1,1,self.click_color_theme)
        self.check_radiobutton(self.radioButton1_2, 2,self.click_color_theme)
        self.check_radiobutton(self.radioButton1_3, 3,self.click_color_theme)
        self.check_radiobutton(self.radioButton1_4, 4,self.click_color_theme)
        self.check_radiobutton(self.radioButton1_5, 5,self.click_color_theme)

        self.check_radiobutton(self.radioButton1_11, 1 ,self.click_music_theme)
        self.check_radiobutton(self.radioButton1_12, 2 ,self.click_music_theme)
        self.check_radiobutton(self.radioButton1_13, 3 ,self.click_music_theme)
        self.check_radiobutton(self.radioButton1_14, 4 ,self.click_music_theme)

    def equalizer_check(self):
        global flag_equalizer
        global fft_out

        if flag_equalizer:
            fft_out = [0] * len(audio_input.get_fft())

        flag_equalizer = self.radioButton1_15.isChecked()

    def set_equalizer(self):
        global fft_out
        self.line_10.move(180,211 - mapping(fft_out[0],19000,200))
        self.line_10.resize(15, mapping(fft_out[0],19000,200))

        self.line_3.move(200, 211 - mapping(fft_out[1], 19000,200))
        self.line_3.resize(15, mapping(fft_out[1], 19000,200))

        self.line_4.move(220, 211 - mapping(fft_out[2], 19000,200))
        self.line_4.resize(15, mapping(fft_out[2], 19000,200))

        self.line_5.move(240, 211 - mapping(fft_out[3], 19000,200))
        self.line_5.resize(15, mapping(fft_out[3], 19000,200))

        self.line_6.move(260, 211 - mapping(fft_out[4], 19000,200))
        self.line_6.resize(15, mapping(fft_out[4], 19000,200))

        self.line_7.move(280, 211 - mapping(fft_out[5], 19000,200))
        self.line_7.resize(15, mapping(fft_out[5], 19000,200))

        self.line_8.move(300, 211 - mapping(fft_out[6], 19000,200))
        self.line_8.resize(15, mapping(fft_out[6], 19000,200))

        self.line_9.move(320, 211 - mapping(fft_out[7], 19000,200))
        self.line_9.resize(15, mapping(fft_out[7], 19000,200))

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




    def set_combobox_ser(self,newText):
        global current_serial_port
        global ser
        current_serial_port = newText

        try:
            ser = serial.Serial(current_serial_port, 9600)
        except serial.SerialException:
            print
            "failed to write to port %s" % current_serial_port
            sys.exit()

    def set_combobox_audio(self,index):
        global audio_index
        audio_index = index

    def update_audio(self):
        global audio_index
        self.comboBox_2.clear()
        inputs = audio_input.find_input_device()
        for input in inputs:
            if input['name'].find('микшер')!=-1 or input['name'].find('mix')!=-1:
                audio_index = input['index']
            self.comboBox_2.addItem(input['name'])




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

def mapping(num,max_cur,max_new): #start - 0
    coef = max_new/max_cur
    return int(coef*num)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle("Fusion")

    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))

    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(100, 0, 0))
    palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)


    ex = App()
    ex.update_serial_ports()
    ex.update_audio()
    app.exec_()