# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\python project\VS\UI\basicUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 939, 737))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PtShowWidget = MatplotlibWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PtShowWidget.sizePolicy().hasHeightForWidth())
        self.PtShowWidget.setSizePolicy(sizePolicy)
        self.PtShowWidget.setMinimumSize(QtCore.QSize(600, 400))
        self.PtShowWidget.setObjectName("PtShowWidget")
        self.verticalLayout.addWidget(self.PtShowWidget)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.PtInputTableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PtInputTableWidget.sizePolicy().hasHeightForWidth())
        self.PtInputTableWidget.setSizePolicy(sizePolicy)
        self.PtInputTableWidget.setMinimumSize(QtCore.QSize(0, 60))
        self.PtInputTableWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.PtInputTableWidget.setObjectName("PtInputTableWidget")
        self.PtInputTableWidget.setColumnCount(0)
        self.PtInputTableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.PtInputTableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(13)
        self.gridLayout.setObjectName("gridLayout")
        self.PtSetListView = QtWidgets.QListView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PtSetListView.sizePolicy().hasHeightForWidth())
        self.PtSetListView.setSizePolicy(sizePolicy)
        self.PtSetListView.setMinimumSize(QtCore.QSize(300, 650))
        self.PtSetListView.setObjectName("PtSetListView")
        self.gridLayout.addWidget(self.PtSetListView, 0, 0, 1, 2)
        self.VectorShowCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.VectorShowCheckBox.setObjectName("VectorShowCheckBox")
        self.gridLayout.addWidget(self.VectorShowCheckBox, 1, 0, 1, 1)
        self.CoordinateRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.CoordinateRadioButton.setObjectName("CoordinateRadioButton")
        self.gridLayout.addWidget(self.CoordinateRadioButton, 1, 1, 1, 1)
        self.PtAddButton = QtWidgets.QPushButton(self.layoutWidget)
        self.PtAddButton.setObjectName("PtAddButton")
        self.gridLayout.addWidget(self.PtAddButton, 2, 0, 1, 1)
        self.PtDelButton = QtWidgets.QPushButton(self.layoutWidget)
        self.PtDelButton.setObjectName("PtDelButton")
        self.gridLayout.addWidget(self.PtDelButton, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.VectorShowCheckBox.setText(_translate("MainWindow", "Show Pt Vector"))
        self.CoordinateRadioButton.setText(_translate("MainWindow", "show CS"))
        self.PtAddButton.setText(_translate("MainWindow", "Pt Add"))
        self.PtDelButton.setText(_translate("MainWindow", "Pt Del"))

from UI.MatplotlibWidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

