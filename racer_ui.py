# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.auth_link = QtWidgets.QLineEdit(self.centralwidget)
        self.auth_link.setGeometry(QtCore.QRect(20, 40, 351, 20))
        self.auth_link.setObjectName("auth_link")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.label.setObjectName("label")
        self.check_link = QtWidgets.QPushButton(self.centralwidget)
        self.check_link.setGeometry(QtCore.QRect(380, 40, 75, 23))
        self.check_link.setObjectName("check_link")
        self.win_text = QtWidgets.QLabel(self.centralwidget)
        self.win_text.setGeometry(QtCore.QRect(20, 310, 47, 13))
        self.win_text.setObjectName("win_text")
        self.win_count = QtWidgets.QLabel(self.centralwidget)
        self.win_count.setGeometry(QtCore.QRect(70, 309, 61, 16))
        self.win_count.setObjectName("win_count")
        self.loose_text = QtWidgets.QLabel(self.centralwidget)
        self.loose_text.setGeometry(QtCore.QRect(169, 309, 71, 16))
        self.loose_text.setObjectName("loose_text")
        self.loose_count = QtWidgets.QLabel(self.centralwidget)
        self.loose_count.setGeometry(QtCore.QRect(240, 311, 47, 13))
        self.loose_count.setObjectName("loose_count")
        self.box_text = QtWidgets.QLabel(self.centralwidget)
        self.box_text.setGeometry(QtCore.QRect(319, 309, 91, 16))
        self.box_text.setObjectName("box_text")
        self.box_count = QtWidgets.QLabel(self.centralwidget)
        self.box_count.setGeometry(QtCore.QRect(420, 312, 47, 13))
        self.box_count.setObjectName("box_count")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setEnabled(True)
        self.start_btn.setGeometry(QtCore.QRect(90, 360, 75, 23))
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setEnabled(True)
        self.stop_btn.setGeometry(QtCore.QRect(280, 360, 75, 23))
        self.stop_btn.setObjectName("stop_btn")
        self.racing_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.racing_radio.setGeometry(QtCore.QRect(20, 250, 82, 17))
        self.racing_radio.setObjectName("racing_radio")
        self.box_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.box_radio.setGeometry(QtCore.QRect(20, 270, 82, 17))
        self.box_radio.setObjectName("box_radio")
        self.auth_text_status = QtWidgets.QLabel(self.centralwidget)
        self.auth_text_status.setGeometry(QtCore.QRect(140, 10, 231, 16))
        self.auth_text_status.setText("")
        self.auth_text_status.setObjectName("auth_text_status")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(120, 140, 91, 22))
        self.spinBox_2.setMinimum(100)
        self.spinBox_2.setMaximum(999999)
        self.spinBox_2.setProperty("value", 650000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 271, 16))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(20, 140, 91, 22))
        self.spinBox.setMinimum(50000)
        self.spinBox.setMaximum(999999)
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 200, 351, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 131, 16))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ссылка"))
        self.check_link.setText(_translate("MainWindow", "Проверить"))
        self.win_text.setText(_translate("MainWindow", "Побед:"))
        self.win_count.setText(_translate("MainWindow", "0"))
        self.loose_text.setText(_translate("MainWindow", "Поражений:"))
        self.loose_count.setText(_translate("MainWindow", "0"))
        self.box_text.setText(_translate("MainWindow", "Коробок найдено:"))
        self.box_count.setText(_translate("MainWindow", "0"))
        self.start_btn.setText(_translate("MainWindow", "Старт"))
        self.stop_btn.setText(_translate("MainWindow", "Стоп"))
        self.racing_radio.setText(_translate("MainWindow", "Гонки"))
        self.box_radio.setText(_translate("MainWindow", "Коробки"))
        self.label_2.setText(_translate("MainWindow", "Диапазон ID такси для поиска коробок"))
        self.label_3.setText(_translate("MainWindow", "Настройки"))
        self.lineEdit.setText(_translate("MainWindow", "583795,604169,576950,599525,605143,601459,601172,583236,605961,606802,605400,547861,603020,589267,605922,575144,602607,547429,603817,604851,604399,606717, 554595, 549442, 15264, 332162, 572163, 4889, 284643, 605021, 549191, 587055, 604115,329121, 604453, 588744,283097,572133,606673,604076,597350,257326,606440,598011, 553349, 256166, 301437, 530951, 20282, 606015, 606439, 462639,590760,603733,602853,602593,590281,256163,601688,128127,319721,173473,594432,606595"))
        self.label_4.setText(_translate("MainWindow", "ID такси для гонок"))
        self.label_5.setText(_translate("MainWindow", "Режим работы:"))
