from PyQt6 import QtCore, QtGui, QtWidgets

from SubscribeWindow import subscriptions_list_copy, subscriptions_list

class Ui_UnsubscribeWindow(object):
    def setupUi(self, UnsubscribeWindow, client):

        self.client=client

        UnsubscribeWindow.setObjectName("UnsubscribeWindow")
        UnsubscribeWindow.resize(400, 191)
        self.label = QtWidgets.QLabel(UnsubscribeWindow)
        self.label.setGeometry(QtCore.QRect(100, 20, 191, 61))
        font = QtGui.QFont("bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(UnsubscribeWindow)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 51, 16))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(UnsubscribeWindow)
        self.lineEdit.setGeometry(QtCore.QRect(90, 100, 271, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(UnsubscribeWindow)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 121, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(lambda: self.on_unsubscribe_button())

        self.retranslateUi(UnsubscribeWindow)
        QtCore.QMetaObject.connectSlotsByName(UnsubscribeWindow)

    def retranslateUi(self, UnsubscribeWindow):
        _translate = QtCore.QCoreApplication.translate
        UnsubscribeWindow.setWindowTitle(_translate("UnsubscribeWindow", "MQTT Client"))
        self.label.setText(_translate("UnsubscribeWindow", "Subscription"))
        self.label_2.setText(_translate("UnsubscribeWindow", "Topic"))
        self.pushButton.setText(_translate("UnsubscribeWindow", "Unsubscribe"))

    def get_topic(self):
        topic = self.lineEdit.text()
        return topic

    def on_unsubscribe_button(self):
        topic = self.get_topic()
        self.client.unsubscribe([topic])
        res='topic: '+ topic +'\nQoS: '
        index = 0
        for sir in subscriptions_list_copy:
            if res in sir:
                subscriptions_list_copy.pop(index)
            index += 1

        for ceva in subscriptions_list_copy:
            subscriptions_list.append(ceva)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UnsubscribeWindow = QtWidgets.QWidget()
    ui = Ui_UnsubscribeWindow()
    ui.setupUi(UnsubscribeWindow)
    UnsubscribeWindow.show()
    sys.exit(app.exec())
