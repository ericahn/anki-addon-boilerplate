from aqt import mw
from aqt.qt import *


class MainMenu(QDialog):
    def __init__(self):
        QDialog.__init__(self, mw, Qt.Window)
        mw.setupDialogGC(self)