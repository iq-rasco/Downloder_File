from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from os import path
import urllib.request
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 316)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 20, 381, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 80, 301, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 21))
        self.label.setIndent(24)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 101, 21))
        self.label_2.setIndent(14)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(544, 82, 71, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 220, 181, 41))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(220, 152, 391, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Enter URL"))
        self.label_2.setText(_translate("MainWindow", "Save Location"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Start Download"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        
    
      

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.handel_UI()
        self.Handel_Buttun()
        self.setStyleSheet(
            """
            
                /* Dark mode styles */
                QWidget {
                    background-color: #333;
                    color: white;
                }

                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 10px;
                    margin: 5px;
                }

                QPushButton:hover {
                    background-color: #2582c4;
                }

                QLabel {
                    font-size: 12px;
                    font-weight: bold;
                    color: white;
                }

                QLineEdit {
                    border: 1px solid #555;
                    padding: 5px;
                    margin: 5px;
                    color: white;
                    background-color: #444;
                }

                   QProgressBar {
                    border: 1px solid #555;
                    background-color: #444;
                    height: 20px;
                    margin: 5px;
                    color: white;
                    
                    }
            """
        )
        
        
        
        
    
    def handel_UI(self):
        self.setWindowTitle('Downloader')
        self.setFixedSize(700, 400)
        
    def Handel_Buttun(self):      
        self.pushButton_2.clicked.connect(self.Handel_dwonload)
        self.pushButton.clicked.connect(self.Handel_Browse)
        
        
        
    def Handel_Browse(self):
        save_location = QFileDialog.getSaveFileName(self, caption="Save as", directory="", filter="All Files (*.*);;Text Files (*.txt);;CSV Files (*.csv);;All Files (*)")
        text = str(save_location)
        name = (text[2:].split(',')[0].replace("'", ""))
        self.lineEdit_2.setText(name)
        
        
        
    def Handel_prgress(self, blocknum, blocksize, totalsize):
        percent = (blocknum * blocksize / totalsize) * 100
        self.progressBar.setValue(int(percent))
        QApplication.processEvents() #not respoding


    def Handel_dwonload(self):
        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()  # Assuming lineEdit_2 contains the save location
        
        if not url or not save_location:
            QMessageBox.warning(self, "Warning", "Please enter both URL and save location.")
            return
        
        try:
            urllib.request.urlretrieve(url, save_location, self.Handel_prgress)
            QMessageBox.information(self, "Download Completed", "The download is finished.")
            self.progressBar.setValue(0)
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
          
        
        
