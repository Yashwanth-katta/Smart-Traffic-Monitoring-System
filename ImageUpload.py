from PyQt5 import QtCore, QtGui, QtWidgets
from TrafficDetection import TrafficDetection
from TrafficDetection2 import TrafficDetection2
from Results import Results


class ImageUpload(object):
    def browseimage(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "C:\\Users\\paras\\proj"
                                                                                     "\\IMAGES",
                                                                "*.jpg")
            print(fileName)
            self.lineEdit.setText(fileName)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def process(self):
        try:
            fname = self.lineEdit.text()
            TrafficDetection.process(fname)
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def detectiondef(self):
        try:
            print("Load Images")
            TrafficDetection2.process()
            try:
                print("Displayb window")
                self.Dialog2z = QtWidgets.QDialog()
                self.ui2z = Results()
                self.ui2z.setupUi(self.Dialog2z)
                self.Dialog2z.show()
            except Exception as e:
                print("Error=" + e.args[0])
                tb = sys.exc_info()[2]
                print(tb.tb_lineno)
                print(e)
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 493)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 30, 91, 101))
        self.tableView.setStyleSheet("border-image: url(icons/imgup.png);")
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 70, 201, 71))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 75 16pt \"Agency FB\";\n"
                                 "")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 170, 280, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 170, 70, 50))
        self.pushButton.setStyleSheet("border-image: url(icons/upload.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browseimage)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 220, 100, 80))
        self.pushButton_2.setStyleSheet("border-image: url(icons/detection.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.process)
        self.Detection = QtWidgets.QPushButton(Dialog)
        self.Detection.setGeometry(QtCore.QRect(140, 340, 110, 100))
        self.Detection.setStyleSheet("border-image: url(icons/traffic-light.png);")
        self.Detection.setText("")
        self.Detection.setObjectName("Detection")
        self.Detection.clicked.connect(self.detectiondef)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Image Upload"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ImageUpload()
    ui.setupUi(Dialog)
    Dialog.show()
