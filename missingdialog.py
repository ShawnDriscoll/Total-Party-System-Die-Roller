# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'missingdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_missingDialog(object):
    def setupUi(self, missingDialog):
        missingDialog.setObjectName("missingDialog")
        missingDialog.resize(340, 230)
        missingDialog.setMinimumSize(QtCore.QSize(340, 230))
        missingDialog.setMaximumSize(QtCore.QSize(340, 230))
        self.aboutOKButton = QtWidgets.QPushButton(missingDialog)
        self.aboutOKButton.setGeometry(QtCore.QRect(130, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aboutOKButton.setFont(font)
        self.aboutOKButton.setObjectName("aboutOKButton")
        self.textLabel = QtWidgets.QLabel(missingDialog)
        self.textLabel.setGeometry(QtCore.QRect(20, 40, 301, 111))
        self.textLabel.setTextFormat(QtCore.Qt.RichText)
        self.textLabel.setScaledContents(False)
        self.textLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textLabel.setWordWrap(True)
        self.textLabel.setOpenExternalLinks(True)
        self.textLabel.setObjectName("textLabel")

        self.retranslateUi(missingDialog)
        QtCore.QMetaObject.connectSlotsByName(missingDialog)

    def retranslateUi(self, missingDialog):
        _translate = QtCore.QCoreApplication.translate
        missingDialog.setWindowTitle(_translate("missingDialog", "Missing Characters!"))
        self.aboutOKButton.setText(_translate("missingDialog", "OK"))
        self.textLabel.setText(_translate("missingDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">No characters found!</span></p><p align=\"center\"><span style=\" font-size:10pt;\">You need to first run a TPS CharGen app.</span></p><p align=\"center\"><span style=\" font-size:10pt;\">One can be downloaded from </span><a href=\"https://github.com/ShawnDriscoll/Planet-Matriarchy-RPG-CharGen\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a><span style=\" font-size:10pt;\">.</span></p><p align=\"center\"><span style=\" font-size:10pt;\">For help, email </span><a href=\"mailto:shawndriscoll@hotmail.com?subject=TPS DieRoller 0.4.1b [Missing Characters!]\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">shawndriscoll@hotmail.com</span></a></p></body></html>"))
