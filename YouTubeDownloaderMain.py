import sys
from YouTubeDownloaderGui import Ui_YouTubeDownloader
from pytube import YouTube

from PyQt5 import QtCore, QtGui, QtWidgets

class RunThread(QtCore.QThread):
    processing = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def __init__(self,parent = None):
        super(RunThread,self).__init__(parent)
        self.url_path = ''
        self.outputpath = ''

    def run(self):
        self.isrunning = True
        while self.isrunning:
            self.processing.emit()
            YouTube(self.url_path).streams.first().download(self.outputpath)
            self.isrunning = False
        self.finished.emit()

class MainWindow_EXEC():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_YouTubeDownloader()
        self.ui.setupUi(MainWindow)
        self.path = None
        self.start_window = None

        self.ui.pushButton_2.clicked.connect(self.getfile)
        self.ui.pushButton.clicked.connect(self.outputpath)

        MainWindow.show()
        sys.exit(app.exec_())

    def outputpath(self):
        self.path = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.lineEdit_2.setText(self.path)

    def getfile(self):
        url_path = self.ui.lineEdit.text()
        self.runThread = RunThread()
        self.runThread.url_path = url_path
        self.runThread.outputpath = self.path
        self.runThread.start()
        self.runThread.processing.connect(self.downloading)
        self.runThread.finished.connect(self.finisheddownloading)

    def downloading(self):
        self.runThread.quit()
        self.start_window = QtWidgets.QMessageBox()
        self.start_window.setIcon(QtWidgets.QMessageBox.Information)
        self.start_window.setWindowTitle("Processing")
        self.start_window.setText("Processing              ")
        self.start_window.exec()

    def finisheddownloading(self):
        self.runThread.quit()
        self.start_window.setWindowTitle("Download finished")
        self.start_window.setText("Download Complete")
        self.ui.lineEdit.setText('')





if __name__ == "__main__":
    MainWindow_EXEC()
