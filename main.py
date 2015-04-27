__author__ = 'Giovanni'

import MaxPlus
from PySide import QtCore, QtGui
from ftn.utilities_railer import FinestraDiDialogo

app = QtGui.QApplication.instance()

if not app:
    app = QtGui.QApplication([])

mainWindow = FinestraDiDialogo()
mainWindow.show()
app.exec_()

