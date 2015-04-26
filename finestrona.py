# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\finestrona.ui'
#
# Created: Sun Apr 26 20:49:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 200)
        MainWindow.setMinimumSize(QtCore.QSize(420, 200))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 401, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cmbSaluti = QtGui.QComboBox(self.widget)
        self.cmbSaluti.setObjectName("cmbSaluti")
        self.horizontalLayout.addWidget(self.cmbSaluti)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtNome = QtGui.QLineEdit(self.widget)
        self.txtNome.setObjectName("txtNome")
        self.horizontalLayout_2.addWidget(self.txtNome)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btnSaluta = QtGui.QPushButton(self.widget)
        self.btnSaluta.setObjectName("btnSaluta")
        self.verticalLayout.addWidget(self.btnSaluta)
        self.lblSaluto = QtGui.QLabel(self.widget)
        self.lblSaluto.setObjectName("lblSaluto")
        self.verticalLayout.addWidget(self.lblSaluto)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Forma di saluto : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Nome : ", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSaluta.setText(QtGui.QApplication.translate("MainWindow", "Saluta", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSaluto.setText(QtGui.QApplication.translate("MainWindow", "Saluto :", None, QtGui.QApplication.UnicodeUTF8))

