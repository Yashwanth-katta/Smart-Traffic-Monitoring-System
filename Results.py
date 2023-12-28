from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Results(object):
    res = "------"

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(707, 752)
        Dialog.setStyleSheet("background-color: rgb(252, 255, 65);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 60, 231, 61))
        self.label.setStyleSheet("font: 15pt \"Courier\";")
        self.label.setObjectName("label")
        self.result = QtWidgets.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(40, 170, 601, 491))
        self.result.setStyleSheet("\n"
                                  "font: 25 14pt \"Malgun Gothic Semilight\";")
        f = open("res.txt", "r")
        Results.res = f.read()
        self.result.setText(Results.res)
        self.result.setObjectName("result")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        f.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Results"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Results()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
