import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ImageUpload import ImageUpload


class Home(object):
    def uploadpic(self):
        try:
            self.Dialog2 = QtWidgets.QDialog()
            self.ui2 = ImageUpload()
            self.ui2.setupUi(self.Dialog2)
            self.Dialog2.show()
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(747, 498)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 748, 550))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 170, 0);\n""background-color: rgb(255, 170, 0);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(70, 20, 641, 81))
        self.label.setStyleSheet("font: 18pt \"Century Gothic\";\n" "color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.uploadimage = QtWidgets.QPushButton(self.tab_2)
        self.uploadimage.setGeometry(QtCore.QRect(290, 170, 190, 200))
        self.uploadimage.setStyleSheet("image: url(Images-icon.png);")
        self.uploadimage.setText("")
        self.uploadimage.setObjectName("uploadimage")
        #####################
        self.uploadimage.clicked.connect(self.uploadpic)
        #####################
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 641, 81))
        self.label_3.setStyleSheet("font: 18pt \"Century Gothic\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align =\"center\">Traffic Analysis Using Image "
                                                "AI</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog",
                                                                               "Home"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align =\"center\">Traffic Analysis Using "
                                                  "Image AI</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Options"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Home()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
