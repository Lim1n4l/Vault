import Style.ui as ui
import functions.encrypt as ec
import functions.decrypt as dc
from PySide6 import QtWidgets as qt , QtGui as qg
def set_buttons(wd) :
  button1 = qt.QPushButton("Encrypt files" , wd)
  button1.setGeometry(250 , 200 , 160 , 50)
  button1.setStyleSheet("background-color:black ; color:white;")
  button1.setFont(qg.QFont("Arial" , 16))
  button2 = qt.QPushButton("Decrypt files" , wd)
  button2.setGeometry(250 , 300 , 160 , 50)
  button2.setStyleSheet("background-color:black ; color:white;")
  button2.setFont(qg.QFont("Arial" , 16))
  #==========buttons functions============#
  button1.clicked.connect(ec.encrypt)
  button2.clicked.connect(dc.decrypt)
