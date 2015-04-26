__author__ = 'Giovanni'

# moduli

import sys
from PySide import QtCore, QtGui


# fine moduli

# classe Railer

class Railer(object):
    def __init__(self, lunghezza=1000, passofisso=10, passovariabile=90):
        self.lunghezza = lunghezza
        self.passofisso = passofisso
        self.passovariabile = passovariabile

    def setLunghezza(self, lunghezza):
        self.lunghezza = lunghezza

    def setPassoFisso(self, lunghezza):
        self.passofisso = lunghezza

    def setPassoVariabile(self, lunghezza):
        self.passovariabile = lunghezza

    def calcola(self):
        lunghezzaPerCalcolo = float(self.lunghezza - self.passofisso)
        totalePezzo = float(self.passofisso + self.passovariabile)
        numeroPezzi = lunghezzaPerCalcolo / totalePezzo
        numeroIdealePezzi = round(numeroPezzi)
        lunghezzaVariabile = (lunghezzaPerCalcolo / numeroIdealePezzi) - self.passofisso
        return {"numero": numeroIdealePezzi,
                "fisso": self.passofisso,
                "variabile": lunghezzaVariabile,
                "totale": (self.passofisso + lunghezzaVariabile)}

# fine classe


# UI

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 280)
        MainWindow.setMinimumSize(QtCore.QSize(300, 280))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 279, 233))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spnLunghezza = QtGui.QSpinBox(self.widget)
        self.spnLunghezza.setMinimumSize(QtCore.QSize(60, 0))
        self.spnLunghezza.setMinimum(10)
        self.spnLunghezza.setMaximum(99999)
        self.spnLunghezza.setSingleStep(1)
        self.spnLunghezza.setProperty("value", 300)
        self.spnLunghezza.setObjectName("spnLunghezza")
        self.gridLayout.addWidget(self.spnLunghezza, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spnFisso = QtGui.QSpinBox(self.widget)
        self.spnFisso.setMinimumSize(QtCore.QSize(60, 0))
        self.spnFisso.setMinimum(1)
        self.spnFisso.setMaximum(99999)
        self.spnFisso.setSingleStep(1)
        self.spnFisso.setProperty("value", 300)
        self.spnFisso.setObjectName("spnFisso")
        self.gridLayout.addWidget(self.spnFisso, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.spnVariabile = QtGui.QSpinBox(self.widget)
        self.spnVariabile.setMinimumSize(QtCore.QSize(60, 0))
        self.spnVariabile.setMinimum(1)
        self.spnVariabile.setMaximum(99999)
        self.spnVariabile.setSingleStep(1)
        self.spnVariabile.setProperty("value", 300)
        self.spnVariabile.setObjectName("spnVariabile")
        self.gridLayout.addWidget(self.spnVariabile, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btnCalcola = QtGui.QPushButton(self.widget)
        self.btnCalcola.setMinimumSize(QtCore.QSize(0, 45))
        self.btnCalcola.setObjectName("btnCalcola")
        self.verticalLayout.addWidget(self.btnCalcola)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.txtNumeroPezzi = QtGui.QLineEdit(self.widget)
        self.txtNumeroPezzi.setMinimumSize(QtCore.QSize(80, 0))
        self.txtNumeroPezzi.setObjectName("txtNumeroPezzi")
        self.gridLayout_2.addWidget(self.txtNumeroPezzi, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.txtLunghezzaTotale = QtGui.QLineEdit(self.widget)
        self.txtLunghezzaTotale.setMinimumSize(QtCore.QSize(80, 0))
        self.txtLunghezzaTotale.setObjectName("txtLunghezzaTotale")
        self.gridLayout_2.addWidget(self.txtLunghezzaTotale, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.txtLunghezzaFissa = QtGui.QLineEdit(self.widget)
        self.txtLunghezzaFissa.setMinimumSize(QtCore.QSize(80, 0))
        self.txtLunghezzaFissa.setObjectName("txtLunghezzaFissa")
        self.gridLayout_2.addWidget(self.txtLunghezzaFissa, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.txtLunghezzaVariabile = QtGui.QLineEdit(self.widget)
        self.txtLunghezzaVariabile.setMinimumSize(QtCore.QSize(80, 0))
        self.txtLunghezzaVariabile.setObjectName("txtLunghezzaVariabile")
        self.gridLayout_2.addWidget(self.txtLunghezzaVariabile, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Ftn - Utilities - Railer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Lunghezza totale da suddividere :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Lunghezza pezzo fisso : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Lunghezza pezzo variabile : ", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCalcola.setText(QtGui.QApplication.translate("MainWindow", "Calcola", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Numero totale Elementi : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Lunghezza totale elemento :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Lunghezza fissa :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Lunghezza variabile : ", None, QtGui.QApplication.UnicodeUTF8))

# fine ui

# finestra

class FinestraDiDialogo(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(FinestraDiDialogo, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCalcola.clicked.connect(self.calcola)

    def calcola(self):
        rlr = Railer()
        rlr.setLunghezza(self.ui.spnLunghezza.value())
        rlr.setPassoFisso(self.ui.spnFisso.value())
        rlr.setPassoVariabile(self.ui.spnVariabile.value())
        risultati = rlr.calcola()
        self.ui.txtLunghezzaFissa.setText(unicode(risultati['fisso']))
        self.ui.txtLunghezzaTotale.setText(unicode(risultati['totale']))
        self.ui.txtLunghezzaVariabile.setText(unicode(risultati['variabile']))
        self.ui.txtNumeroPezzi.setText(unicode(risultati['numero']))


# fine finestra

# app

app = QtGui.QApplication(sys.argv)
mainWindow = FinestraDiDialogo()
mainWindow.show()
app.exec_()

# fine app