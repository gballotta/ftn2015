__author__ = 'Giovanni'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from finestrona import Ui_MainWindow

formeDiSaluto = ["Ciao",
                 "Buongiorno",
                 "Buonasera",
                 "Buonanotte",
                 "Fatti fottere"]

class FinestraPrincipale(QMainWindow):
    def __init__(self, parent=None):
        super(FinestraPrincipale, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cmbSaluti.addItems(formeDiSaluto)
        self.ui.btnSaluta.clicked.connect(self.on_click)

    @Slot()
    def on_click(self):
        salutoScelto = formeDiSaluto[self.ui.cmbSaluti.currentIndex()]
        nomeScelto = self.ui.txtNome.text()
        stringaNuova = "Saluto : %s, %s" %(salutoScelto, nomeScelto)
        self.ui.lblSaluto.setText(stringaNuova)


app = QApplication(sys.argv)
finestra = FinestraPrincipale()
finestra.show()
app.exec_()