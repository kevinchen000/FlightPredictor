# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlightPredictorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
##from dask_ml.wrappers import Incremental
##from sklearn.preprocessing import StandardScaler, OneHotEncoder
##from sklearn.model_selection import train_test_split
##from sklearn.neural_network import MLPClassifier
import pickle
import sys, os
#from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from multiprocessing import freeze_support
freeze_support()

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


##Load saved Encoded models to be used for remainder of code#####
infile_encPD = open(resource_path('encPD'), 'rb')
loaded_encPD = pickle.load(infile_encPD)
infile_encDA = open(resource_path('encDA'), 'rb')
loaded_encDA = pickle.load(infile_encDA)
infile_encCP = open(resource_path('encCP'), 'rb')
loaded_encCP = pickle.load(infile_encCP)

####Load saved ML models to be used for remainder of code######
infile_mlpPD = open(resource_path('mlpPD'), 'rb')
loaded_mlpPD = pickle.load(infile_mlpPD)
infile_mlpDA = open(resource_path('mlpDA'), 'rb')
loaded_mlpDA = pickle.load(infile_mlpDA)
infile_mlpCP = open(resource_path('mlpCP'), 'rb')
loaded_mlpCP = pickle.load(infile_mlpCP)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(640, 410)
        MainWindow.setMinimumSize(QtCore.QSize(640, 410))
        MainWindow.setMaximumSize(QtCore.QSize(640, 410))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(10, 10, 401, 61))
        self.Logo.setObjectName("Logo")
        self.GroupTitle = QtWidgets.QLabel(self.centralwidget)
        self.GroupTitle.setGeometry(QtCore.QRect(410, 10, 221, 41))
        self.GroupTitle.setObjectName("GroupTitle")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 621, 351))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 601, 61))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.UserInput = QtWidgets.QGroupBox(self.groupBox)
        self.UserInput.setGeometry(QtCore.QRect(10, 60, 341, 271))
        self.UserInput.setObjectName("UserInput")
        self.label_4 = QtWidgets.QLabel(self.UserInput)
        self.label_4.setGeometry(QtCore.QRect(10, 31, 131, 20))
        self.label_4.setObjectName("label_4")
        self.DepartureAirport = QtWidgets.QComboBox(self.UserInput)
        self.DepartureAirport.setGeometry(QtCore.QRect(120, 30, 201, 22))
        self.DepartureAirport.setObjectName("DepartureAirport")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.DepartureAirport.addItem("")
        self.label_6 = QtWidgets.QLabel(self.UserInput)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 131, 20))
        self.label_6.setObjectName("label_6")
        self.DepartureDate = QtWidgets.QDateEdit(self.UserInput)
        self.DepartureDate.setGeometry(QtCore.QRect(120, 110, 201, 22))
        self.DepartureDate.setDate(QtCore.QDate(2020, 1, 1))
        self.DepartureDate.setObjectName("DepartureDate")
        self.ArrivalAirport = QtWidgets.QComboBox(self.UserInput)
        self.ArrivalAirport.setEnabled(False)
        self.ArrivalAirport.setGeometry(QtCore.QRect(120, 60, 201, 22))
        self.ArrivalAirport.setObjectName("ArrivalAirport")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.ArrivalAirport.addItem("")
        self.label_7 = QtWidgets.QLabel(self.UserInput)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 131, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.UserInput)
        self.label_8.setGeometry(QtCore.QRect(10, 140, 131, 20))
        self.label_8.setObjectName("label_8")
        self.DepartureTime = QtWidgets.QTimeEdit(self.UserInput)
        self.DepartureTime.setGeometry(QtCore.QRect(120, 140, 201, 22))
        self.DepartureTime.setObjectName("DepartureTime")
        self.label_9 = QtWidgets.QLabel(self.UserInput)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 131, 20))
        self.label_9.setObjectName("label_9")
        self.Airline = QtWidgets.QComboBox(self.UserInput)
        self.Airline.setGeometry(QtCore.QRect(120, 180, 201, 22))
        self.Airline.setObjectName("Airline")
        self.Airline.addItem("")
        self.Airline.addItem("")
        self.Airline.addItem("")
        self.Airline.addItem("")
        self.Airline.addItem("")
        self.Airline.addItem("")
        self.Airline.addItem("")
        self.Airline.addItem("")
        self.Airline.addItem("")
        self.Airline.addItem("")
        self.Calculate = QtWidgets.QPushButton(self.UserInput)
        self.Calculate.setGeometry(QtCore.QRect(240, 230, 81, 31))
        self.Calculate.setObjectName("Calculate")
        self.label_10 = QtWidgets.QLabel(self.UserInput)
        self.label_10.setGeometry(QtCore.QRect(100, 229, 131, 31))
        self.label_10.setObjectName("label_10")
        self.Results = QtWidgets.QGroupBox(self.groupBox)
        self.Results.setGeometry(QtCore.QRect(370, 60, 241, 271))
        self.Results.setObjectName("Results")
        self.DelayPercent = QtWidgets.QProgressBar(self.Results)
        self.DelayPercent.setGeometry(QtCore.QRect(10, 40, 221, 31))
        self.DelayPercent.setAutoFillBackground(False)
        self.DelayPercent.setProperty("value", 0)
        self.DelayPercent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DelayPercent.setTextVisible(True)
        self.DelayPercent.setOrientation(QtCore.Qt.Horizontal)
        self.DelayPercent.setInvertedAppearance(False)
        self.DelayPercent.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.DelayPercent.setObjectName("DelayPercent")
        self.label_11 = QtWidgets.QLabel(self.Results)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 131, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Results)
        self.label_12.setGeometry(QtCore.QRect(10, 120, 151, 21))
        self.label_12.setObjectName("label_12")
        self.CancellationPercent = QtWidgets.QProgressBar(self.Results)
        self.CancellationPercent.setGeometry(QtCore.QRect(10, 140, 221, 31))
        self.CancellationPercent.setMaximum(10)
        self.CancellationPercent.setProperty("value", 0)
        self.CancellationPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.CancellationPercent.setObjectName("CancellationPercent")
        self.label_13 = QtWidgets.QLabel(self.Results)
        self.label_13.setGeometry(QtCore.QRect(10, 80, 91, 25))
        self.label_13.setObjectName("label_13")
        self.label_2 = QtWidgets.QLabel(self.Results)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 231, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.DelayAmount = QtWidgets.QTextBrowser(self.Results)
        self.DelayAmount.setGeometry(QtCore.QRect(120, 81, 111, 25))
        self.DelayAmount.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.DelayAmount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DelayAmount.setFrameShape(QtWidgets.QFrame.Box)
        self.DelayAmount.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DelayAmount.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DelayAmount.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.DelayAmount.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.DelayAmount.setDocumentTitle("")
        self.DelayAmount.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.DelayAmount.setLineWrapColumnOrWidth(0)
        self.DelayAmount.setOverwriteMode(False)
        self.DelayAmount.setAcceptRichText(True)
        self.DelayAmount.setObjectName("DelayAmount")
        self.Semester = QtWidgets.QLabel(self.centralwidget)
        self.Semester.setGeometry(QtCore.QRect(410, -10, 221, 41))
        self.Semester.setObjectName("Semester")
        self.GroupTitle.raise_()
        self.groupBox.raise_()
        self.Semester.raise_()
        self.Logo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/icons8-add-file-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/icons8-trash-can-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionClose.setIcon(icon1)
        self.actionClose.setObjectName("actionClose")
        self.actionTutorial = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/icons8-file-invoice-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTutorial.setIcon(icon2)
        self.actionTutorial.setObjectName("actionTutorial")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Calculate.clicked.connect(self.on_click)
        #self.show()

    import ResourceFiles_FlightPredictor_GUI

    def on_click(self):
        dateString = self.DepartureDate.text()
        timeString = self.DepartureTime.text()
        airlineIndex = self.Airline.currentIndex()
        airportIndex = self.DepartureAirport.currentIndex()
        c = self.Airline.itemText(airlineIndex)
        d = self.DepartureAirport.itemText(airportIndex)
        cList = c.split(" ")
        c = cList[0]
        dList = d.split(" ")
        d = dList[0]

        aList = dateString.split("/")
        a = aList[0]
        if aList[0] == "1" or aList[0] == "01":
            a = int(aList[1])
        if aList[0] == "2" or aList[0] == "02":
            a = 31 + int(aList[1])
        if aList[0] == "3" or aList[0] == "03":
            a = 59 + int(aList[1])
        if aList[0] == "4" or aList[0] == "04":
            a = 90 + int(aList[1])
        if aList[0] == "5" or aList[0] == "05":
            a = 120 + int(aList[1])
        if aList[0] == "6" or aList[0] == "06":
            a = 151 + int(aList[1])
        if aList[0] == "7" or aList[0] == "07":
            a = 181 + int(aList[1])
        if aList[0] == "8" or aList[0] == "08":
            a = 212 + int(aList[1])
        if aList[0] == "9" or aList[0] == "09":
            a = 243 + int(aList[1])
        if aList[0] == "10":
            a = 273 + int(aList[1])
        if aList[0] == "11":
            a = 304 + int(aList[1])
        if aList[0] == "12":
            a = 334 + int(aList[1])

        bList = timeString.split(":")
        b = bList[0]
        b = int(b)

        dateList = list(range(1, 366))
        timeList = list(range(1, 25))
        carrierList = ['AS', 'G4', 'AA', 'DL', '2F', 'B6', 'HA', 'WN', 'NK', 'NA']
        airportList = ['ATL', 'DEN', 'DFW', 'EWR', 'HNL', 'JFK', 'LAS', 'LAX', 'OGG', 'SEA', 'SFO']

        if a in dateList and b in timeList and c in carrierList and d in airportList and int(aList[0]) < 13 and int(
                aList[1]) < 32:
            predPD = [[a, b, c, d]]
            predPD = loaded_encPD.transform(predPD)
            newProbMLP_PD = loaded_mlpPD.predict_proba(predPD)
            newProbPD = newProbMLP_PD

            predDA = [[a, b, c, d]]
            predDA = loaded_encDA.transform(predDA)
            newProbMLP_DA = loaded_mlpDA.predict(predDA)
            prenewProbDA = newProbMLP_DA
            if prenewProbDA == -1:
                newProbDA = '<=30min early'
            elif prenewProbDA == 0:
                newProbDA = '<=30min delay'
            else:
                newProbDA = '>30min delay'

            predCP = [[a, b, c, d]]
            predCP = loaded_encCP.transform(predCP)
            newProbMLP_CP = loaded_mlpCP.predict_proba(predCP)
            newProbCP = newProbMLP_CP

            str(newProbDA)

            self.DelayPercent.setProperty("value", int(round(newProbPD[0][1] * 100,0)))
            self.DelayAmount.setText(newProbDA)
            self.CancellationPercent.setProperty("value", int(round(newProbCP[0][1] * 100,0)))

        else:
            self.DelayPercent.setProperty("value", 0)
            self.DelayAmount.setText("NA")
            self.CancellationPercent.setProperty("value", 0)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Images/Logo.png\"/></p></body></html>"))
        self.GroupTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">AME 505 - Group 7</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Hello and welcome to the Flight Delay Predictor and Cancellation Calculator. Please enter your depature airport, the date and time of the desired flight, and the carrier you prefer. Once ready, hit calculate and see your results on the right.</p></body></html>"))
        self.UserInput.setTitle(_translate("MainWindow", "User Input"))
        self.label_4.setText(_translate("MainWindow", "Departure Airport:"))
        self.DepartureAirport.setItemText(0, _translate("MainWindow", "ATL - Atlanta International"))
        self.DepartureAirport.setItemText(1, _translate("MainWindow", "DEN - Denver International "))
        self.DepartureAirport.setItemText(2, _translate("MainWindow", "DFW - Dallas/Fort Worth International"))
        self.DepartureAirport.setItemText(3, _translate("MainWindow", "EWR - Newark International"))
        self.DepartureAirport.setItemText(4, _translate("MainWindow", "HNL - Honolulu International"))
        self.DepartureAirport.setItemText(5, _translate("MainWindow", "JFK - John F. Kennedy International"))
        self.DepartureAirport.setItemText(6, _translate("MainWindow", "LAX - Los Angeles International"))
        self.DepartureAirport.setItemText(7, _translate("MainWindow", "OGG - Kahului Regional"))
        self.DepartureAirport.setItemText(8, _translate("MainWindow", "SEA - Seattle International"))
        self.DepartureAirport.setItemText(9, _translate("MainWindow", "SFO - San Francisco International"))
        self.label_6.setText(_translate("MainWindow", "Arrival Airport:"))
        self.ArrivalAirport.setItemText(0, _translate("MainWindow", "ATL - Atlanta International"))
        self.ArrivalAirport.setItemText(1, _translate("MainWindow", "DEN - Denver International "))
        self.ArrivalAirport.setItemText(2, _translate("MainWindow", "DFW - Dallas/Fort Worth International"))
        self.ArrivalAirport.setItemText(3, _translate("MainWindow", "EWR - Newark International"))
        self.ArrivalAirport.setItemText(4, _translate("MainWindow", "HNL - Honolulu International"))
        self.ArrivalAirport.setItemText(5, _translate("MainWindow", "JFK - John F. Kennedy International"))
        self.ArrivalAirport.setItemText(6, _translate("MainWindow", "LAX - Los Angeles International"))
        self.ArrivalAirport.setItemText(7, _translate("MainWindow", "OGG - Kahului Regional"))
        self.ArrivalAirport.setItemText(8, _translate("MainWindow", "SEA - Seattle International"))
        self.ArrivalAirport.setItemText(9, _translate("MainWindow", "SFO - San Francisco International"))
        self.label_7.setText(_translate("MainWindow", "Departure Date:"))
        self.label_8.setText(_translate("MainWindow", "Departure Time: "))
        self.label_9.setText(_translate("MainWindow", "Preferred Carrier:"))
        self.Airline.setItemText(0, _translate("MainWindow", "2F - Frontier "))
        self.Airline.setItemText(1, _translate("MainWindow", "AA - American "))
        self.Airline.setItemText(2, _translate("MainWindow", "AS - Alaska"))
        self.Airline.setItemText(3, _translate("MainWindow", "B6 - Jet Blue"))
        self.Airline.setItemText(4, _translate("MainWindow", "DL - Delta"))
        self.Airline.setItemText(5, _translate("MainWindow", "G4 - Allegiant Air"))
        self.Airline.setItemText(6, _translate("MainWindow", "HA - Hawaiian"))
        self.Airline.setItemText(7, _translate("MainWindow", "NK - Spirit"))
        self.Airline.setItemText(8, _translate("MainWindow", "NA - United"))
        self.Airline.setItemText(9, _translate("MainWindow", "WN - Southwest"))
        self.Calculate.setText(_translate("MainWindow", "Calculate"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Press When Ready:</p></body></html>"))
        self.Results.setTitle(_translate("MainWindow", "Results"))
        self.DelayPercent.setFormat(_translate("MainWindow", "%p%"))
        self.label_11.setText(_translate("MainWindow", "Delay Likelihood:"))
        self.label_12.setText(_translate("MainWindow", "Cancellation Likelihood:"))
        self.CancellationPercent.setFormat(_translate("MainWindow", "%v%"))
        self.label_13.setText(_translate("MainWindow", "Delay Amount:"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Above is the predicted likelihood that the flight selected will be delayed or cancelled.</p></body></html>"))
        self.DelayAmount.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">0</span></p></body></html>"))
        self.DelayAmount.setPlaceholderText(_translate("MainWindow", "None"))
        self.Semester.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Spring 2020</p></body></html>"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
