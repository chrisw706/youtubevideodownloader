# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YouTubeDownloaderGui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_YouTubeDownloader(object):
    def setupUi(self, YouTubeDownloader):
        YouTubeDownloader.setObjectName("YouTubeDownloader")
        YouTubeDownloader.resize(680, 219)
        YouTubeDownloader.setMinimumSize(QtCore.QSize(680, 219))
        YouTubeDownloader.setMaximumSize(QtCore.QSize(680, 219))
        YouTubeDownloader.setStatusTip("")
        YouTubeDownloader.setIconSize(QtCore.QSize(25, 24))
        self.centralwidget = QtWidgets.QWidget(YouTubeDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 30, 491, 31))
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 140, 47, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 92, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 90, 491, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 140, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        YouTubeDownloader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(YouTubeDownloader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 21))
        self.menubar.setObjectName("menubar")
        YouTubeDownloader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(YouTubeDownloader)
        self.statusbar.setObjectName("statusbar")
        YouTubeDownloader.setStatusBar(self.statusbar)

        self.retranslateUi(YouTubeDownloader)
        QtCore.QMetaObject.connectSlotsByName(YouTubeDownloader)

    def retranslateUi(self, YouTubeDownloader):
        _translate = QtCore.QCoreApplication.translate
        YouTubeDownloader.setWindowTitle(_translate("YouTubeDownloader", "You Tube Downloader"))
        self.lineEdit.setPlaceholderText(_translate("YouTubeDownloader", "   Enter YouTube URL"))
        self.label.setText(_translate("YouTubeDownloader", "You Tube URL:"))
        self.pushButton.setText(_translate("YouTubeDownloader", "Output Folder Path:"))
        self.pushButton_2.setText(_translate("YouTubeDownloader", "Download"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YouTubeDownloader = QtWidgets.QMainWindow()
    ui = Ui_YouTubeDownloader()
    ui.setupUi(YouTubeDownloader)
    YouTubeDownloader.show()
    sys.exit(app.exec_())
