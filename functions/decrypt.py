import functions.key_check as ky
from cryptography.fernet import Fernet as fr
from PySide6 import QtWidgets as qt 
def open_ef() :
  file_phat , _ = qt.QFileDialog.getOpenFileName(None , "choose file to decrypt")
  with open (file_phat , "rb") as ef : # ef = encrypted file
    edata = ef.read() # edata = encrypted data
    return edata
def decrypt() :
  edata = open_ef()
  with open( ky.kp , "rb") as k :
    key = k.read()
  cipher = fr (key)
  data = cipher.decrypt(edata)
  save_phat , _ = qt.QFileDialog.getSaveFileName(None , "save decrypted file")
  with open(save_phat , "wb") as d :
    d.write(data)
