from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Channelup.clicked.connect(lambda: self.ChanDisplay(1))
        self.Channeldown.clicked.connect(lambda: self.ChanDisplay(0))
        self.Volumeup.clicked.connect(lambda: self.VolDisplay(1))
        self.Volumedown.clicked.connect(lambda: self.VolDisplay(0))
        self.Mute.clicked.connect(lambda: self.Muted())
        self.Power.clicked.connect(lambda: self.Pow())
        
        
    def Muted(self):
        temp = self.Powr.text()
        if temp == 'True':
            self.Volume.setText('0')
        
        
        
            
    def Pow(self):
        temp = self.Powr.text()
        if temp == '':
            self.Powr.setText('True')
            self.Channel.setText('1')
            self.Volume.setText('1')
        elif temp == 'True':
            self.Powr.setText('False')
            self.Channel.setText('')
            self.Volume.setText('')
        elif temp == 'False':
            self.Powr.setText('True')
            self.Channel.setText('1')
            self.Volume.setText('1')
            
    def ChanDisplay(self,val):
        temp = self.Powr.text()
        if temp == 'False':
            self.Channel.setText('')
        if temp == 'True':
            if val == 1:
                chan = int(self.Channel.text())
                chan +=1
                if chan == 61:
                    chan = 1
                self.Channel.setText(f'{chan}')
            elif val == 0:
                chan = int(self.Channel.text())
                chan -= 1
                if chan == 0:
                    chan = 60
                self.Channel.setText(f'{chan}')
                    
    def VolDisplay(self,val):
        temp = self.Powr.text()
        if temp == 'True':
            if val == 1:
                try:
                    vol = int(self.Volume.text())
                    vol +=1
                    if vol == 61:
                        vol = 1
                    self.Volume.setText(f'{vol}')
                except:
                    vol = 1
                    self.Volume.setText(f'{vol}')
            elif val == 0:
                try:
                    vol = int(self.Volume.text())
                    vol -= 1
                    if vol < 1:
                        vol = 60
                    self.Volume.setText(f'{vol}')
                except:
                    vol = 1
                    self.Volume.setText(f'{vol}')
        
#     def clear(self):
#         self.Food_2.setText('')
#         self.Drink_2.setText('')
#         self.Dessert_2.setText('')
#         self.Output.setText('')
#         self.radio10.setChecked(True)
