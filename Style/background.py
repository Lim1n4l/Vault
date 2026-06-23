import Style.ui as ui
from PySide6 import QtWidgets as qt , QtGui as qg
import os
def set_background(wd) :
  base_dir = os.path.dirname(os.path.abspath(__file__))
  parts = base_dir.split(os.sep)
  parts.remove("Style")
  p = os.sep.join(parts)
  img = os.path.join(p , "img" , "lock.png") # background phat
  bg = qt.QLabel(wd)
  bg.setPixmap(qg.QPixmap(img))
  bg.setScaledContents(True)
  