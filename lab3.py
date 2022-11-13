import first_script
import second_script
import third_script
import iterator

from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


import sys
import os



class Window(QMainWindow):
    def read_directory(self,elem):
        directory=elem.split(",")
        with open(directory[1],"r") as f:
            text=f.read()
        text=text.split("\n")
        spisok=[]
        for element in text:
            for i in range(1,(len(element)//100)+1):
                if element[100*i-1]!=" ":
                    j=100*i-1
                    while element[j]!=" ":
                        j=j-1
                    element=element[:j]+"\n"+element[j:]
                else: element=element[:100*i-1]+"\n"+element[100*i-1:]
            spisok.append(element)

        self.title_opinion.clear()
        self.plus_opinion.clear()
        self.minus_opinion.clear()
        self.text_opinion.clear()
        
        self.title_opinion.setText(spisok[0])
        self.plus_opinion.setText(spisok[2])
        self.minus_opinion.setText(spisok[3])
        self.text_opinion.setText(spisok[4])

        self.title_opinion.adjustSize()
        self.plus_opinion.adjustSize()
        self.minus_opinion.adjustSize()
        self.text_opinion.adjustSize()
    
    def click_button_first_star(self):
        elem=str(next(self.iterat_1))
        if elem=="['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
            elem=str(next(self.iterat_1))
        self.read_directory(elem)

    
    
    def click_button_second_star(self):
        elem=str(next(self.iterat_2))
        if elem=="['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
            elem=str(next(self.iterat_2))
        self.read_directory(elem)


    def click_button_third_star(self):
        elem=str(next(self.iterat_3))
        if elem=="['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
            elem=str(next(self.iterat_3))
        self.read_directory(elem)


    def click_button_fourth_star(self):
        elem=str(next(self.iterat_4))
        if elem=="['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
            elem=str(next(self.iterat_4))
        self.read_directory(elem)


    def click_button_fifth_star(self):
        elem=str(next(self.iterat_5))
        if elem=="['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
            elem=str(next(self.iterat_5))
        self.read_directory(elem)

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize (800, 600)
    window.setObjectName("MainWindow")
    window.setStyleSheet(
        "#MainWindow{border-image:url(phon.jpg)}")
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    application()