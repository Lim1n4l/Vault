import Style.buttons as bt
import Style.ui as ui
import Style.background as bk
from PySide6 import QtWidgets as qt
app = qt.QApplication()
window = ui.Ui()
bk.set_background(window)
bt.set_buttons(window)
window.show()
app.exec() 