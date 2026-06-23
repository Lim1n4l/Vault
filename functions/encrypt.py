from cryptography.fernet import Fernet as fr
from PySide6 import QtWidgets as qt
import functions.key_check as ky
def open_df() :
  file_phat , _ = qt.QFileDialog.getOpenFileName(None , "choose file to encrypt")
  with open (file_phat , "rb") as df : # df = decrypted file
    ddata = df.read() # ddata = decrypted data
  return ddata
def encrypt() :
  data = open_df()
  ky.kc()
  with open(ky.kp , "rb") as k :
   key = k.read()
  cipher = fr(key)
  encrypted = cipher.encrypt(data)
  save_phat , _ = qt.QFileDialog.getSaveFileName(None , "save encrypted file")
  with open(save_phat + ".vlt" , "wb") as f :
    f.write(encrypted)




