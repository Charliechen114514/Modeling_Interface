# Form implementation generated from reading ui file 'reminderprocesswindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ReminderProcessWindow(object):
    def setupUi(self, ReminderProcessWindow):
        ReminderProcessWindow.setObjectName("ReminderProcessWindow")
        ReminderProcessWindow.resize(550, 478)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ReminderProcessWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sthFunShow = QtWidgets.QTextBrowser(parent=ReminderProcessWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sthFunShow.setFont(font)
        self.sthFunShow.setObjectName("sthFunShow")
        self.verticalLayout_2.addWidget(self.sthFunShow)
        self.widget = QtWidgets.QWidget(parent=ReminderProcessWindow)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.exportProcessTextEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.exportProcessTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.exportProcessTextEdit.setObjectName("exportProcessTextEdit")
        self.verticalLayout.addWidget(self.exportProcessTextEdit)
        self.exportProgressBar = QtWidgets.QProgressBar(parent=self.widget)
        self.exportProgressBar.setMinimumSize(QtCore.QSize(0, 50))
        self.exportProgressBar.setProperty("value", 0)
        self.exportProgressBar.setObjectName("exportProgressBar")
        self.verticalLayout.addWidget(self.exportProgressBar)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(ReminderProcessWindow)
        QtCore.QMetaObject.connectSlotsByName(ReminderProcessWindow)

    def retranslateUi(self, ReminderProcessWindow):
        _translate = QtCore.QCoreApplication.translate
        ReminderProcessWindow.setWindowTitle(_translate("ReminderProcessWindow", "Form"))
