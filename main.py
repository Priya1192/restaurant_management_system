# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 592)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 371, 51))
        self.label.setStyleSheet("font: 63 24pt \"Bookman Old Style\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 80, 901, 501))
        self.tabWidget.setStyleSheet("font: 63 10pt \"Bookman Old Style\";\n"
"background-color: rgb(200, 180, 196);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.t1_tw = QtWidgets.QTableWidget(self.tab)
        self.t1_tw.setGeometry(QtCore.QRect(340, 10, 451, 291))
        self.t1_tw.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.t1_tw.setAlternatingRowColors(True)
        self.t1_tw.setObjectName("t1_tw")
        self.t1_tw.setColumnCount(4)
        self.t1_tw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.t1_tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.t1_tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.t1_tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.t1_tw.setHorizontalHeaderItem(3, item)
        self.t1_pb_receipt = QtWidgets.QPushButton(self.tab)
        self.t1_pb_receipt.setGeometry(QtCore.QRect(340, 310, 156, 61))
        self.t1_pb_receipt.setStyleSheet("\n"
"background-color: rgb(255, 255, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.t1_pb_receipt.setObjectName("t1_pb_receipt")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 314, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.t1_l_fid = QtWidgets.QLabel(self.layoutWidget)
        self.t1_l_fid.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.t1_l_fid.setObjectName("t1_l_fid")
        self.gridLayout_3.addWidget(self.t1_l_fid, 0, 0, 1, 1)
        self.t1_le_fid = QtWidgets.QLineEdit(self.layoutWidget)
        self.t1_le_fid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t1_le_fid.setObjectName("t1_le_fid")
        self.gridLayout_3.addWidget(self.t1_le_fid, 0, 1, 1, 1)
        self.t1_l_fname = QtWidgets.QLabel(self.layoutWidget)
        self.t1_l_fname.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.t1_l_fname.setObjectName("t1_l_fname")
        self.gridLayout_3.addWidget(self.t1_l_fname, 1, 0, 1, 1)
        self.t1_le_fname = QtWidgets.QLineEdit(self.layoutWidget)
        self.t1_le_fname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t1_le_fname.setObjectName("t1_le_fname")
        self.gridLayout_3.addWidget(self.t1_le_fname, 1, 1, 1, 1)
        self.t1_l_price = QtWidgets.QLabel(self.layoutWidget)
        self.t1_l_price.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.t1_l_price.setObjectName("t1_l_price")
        self.gridLayout_3.addWidget(self.t1_l_price, 2, 0, 1, 1)
        self.t1_le_price = QtWidgets.QLineEdit(self.layoutWidget)
        self.t1_le_price.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t1_le_price.setObjectName("t1_le_price")
        self.gridLayout_3.addWidget(self.t1_le_price, 2, 1, 1, 1)
        self.t1_l_qty = QtWidgets.QLabel(self.layoutWidget)
        self.t1_l_qty.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.t1_l_qty.setObjectName("t1_l_qty")
        self.gridLayout_3.addWidget(self.t1_l_qty, 3, 0, 1, 1)
        self.t1_le_qty = QtWidgets.QLineEdit(self.layoutWidget)
        self.t1_le_qty.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t1_le_qty.setObjectName("t1_le_qty")
        self.gridLayout_3.addWidget(self.t1_le_qty, 3, 1, 1, 1)
        self.t1_pb_ATC = QtWidgets.QPushButton(self.layoutWidget)
        self.t1_pb_ATC.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.t1_pb_ATC.setObjectName("t1_pb_ATC")
        self.gridLayout_3.addWidget(self.t1_pb_ATC, 4, 1, 1, 1)
        self.t1_pb_GD = QtWidgets.QPushButton(self.layoutWidget)
        self.t1_pb_GD.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.t1_pb_GD.setObjectName("t1_pb_GD")
        self.gridLayout_3.addWidget(self.t1_pb_GD, 0, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(540, 310, 251, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 2, 0, 1, 1)
        self.t1_grandtotal = QtWidgets.QLabel(self.layoutWidget1)
        self.t1_grandtotal.setStyleSheet("\n"
"background-color: rgb(255, 255, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.t1_grandtotal.setAlignment(QtCore.Qt.AlignCenter)
        self.t1_grandtotal.setObjectName("t1_grandtotal")
        self.gridLayout_4.addWidget(self.t1_grandtotal, 2, 1, 1, 1)
        self.t1_displaytotal = QtWidgets.QLabel(self.layoutWidget1)
        self.t1_displaytotal.setStyleSheet("\n"
"background-color: rgb(255, 255, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.t1_displaytotal.setAlignment(QtCore.Qt.AlignCenter)
        self.t1_displaytotal.setObjectName("t1_displaytotal")
        self.gridLayout_4.addWidget(self.t1_displaytotal, 0, 1, 1, 1)
        self.t1_displaytax = QtWidgets.QLabel(self.layoutWidget1)
        self.t1_displaytax.setStyleSheet("\n"
"background-color: rgb(255, 255, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.t1_displaytax.setAlignment(QtCore.Qt.AlignCenter)
        self.t1_displaytax.setObjectName("t1_displaytax")
        self.gridLayout_4.addWidget(self.t1_displaytax, 1, 1, 1, 1)
        self.t1_pb_del_itm = QtWidgets.QPushButton(self.tab)
        self.t1_pb_del_itm.setGeometry(QtCore.QRect(800, 260, 91, 41))
        self.t1_pb_del_itm.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.t1_pb_del_itm.setObjectName("t1_pb_del_itm")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 10, 210, 26))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setStyleSheet("font: 63 10pt \"Bookman Old Style\";\n"
"font: 63 12pt \"Bookman Old Style\";\n"
"color: rgb(0, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(85, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.t1_le_ono = QtWidgets.QLineEdit(self.layoutWidget2)
        self.t1_le_ono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t1_le_ono.setObjectName("t1_le_ono")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.t1_le_ono)
        self.t1_pb_new_order = QtWidgets.QPushButton(self.tab)
        self.t1_pb_new_order.setGeometry(QtCore.QRect(800, 210, 91, 41))
        self.t1_pb_new_order.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 0);")
        self.t1_pb_new_order.setObjectName("t1_pb_new_order")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(70, 20, 311, 90))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.t2_le_fid = QtWidgets.QLineEdit(self.layoutWidget3)
        self.t2_le_fid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t2_le_fid.setObjectName("t2_le_fid")
        self.gridLayout.addWidget(self.t2_le_fid, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.t2_le_fname = QtWidgets.QLineEdit(self.layoutWidget3)
        self.t2_le_fname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t2_le_fname.setObjectName("t2_le_fname")
        self.gridLayout.addWidget(self.t2_le_fname, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.t2_pb_search = QtWidgets.QPushButton(self.layoutWidget3)
        self.t2_pb_search.setStyleSheet("font: 63 10pt \"Bookman Old Style\";\n"
"font: 63 12pt \"Bookman Old Style\";\n"
"color: rgb(0, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(85, 255, 255);")
        self.t2_pb_search.setObjectName("t2_pb_search")
        self.gridLayout.addWidget(self.t2_pb_search, 2, 1, 1, 1)
        self.t2_tw = QtWidgets.QTableWidget(self.tab_2)
        self.t2_tw.setGeometry(QtCore.QRect(70, 120, 311, 331))
        self.t2_tw.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t2_tw.setObjectName("t2_tw")
        self.t2_tw.setColumnCount(3)
        self.t2_tw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t2_tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t2_tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.t2_tw.setHorizontalHeaderItem(2, item)
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(450, 390, 341, 51))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t2_pb_VD = QtWidgets.QPushButton(self.layoutWidget4)
        self.t2_pb_VD.setStyleSheet("font: 63 10pt \"Bookman Old Style\";\n"
"font: 63 12pt \"Bookman Old Style\";\n"
"color: rgb(0, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 127);")
        self.t2_pb_VD.setObjectName("t2_pb_VD")
        self.horizontalLayout.addWidget(self.t2_pb_VD)
        self.t2_pb_reset = QtWidgets.QPushButton(self.layoutWidget4)
        self.t2_pb_reset.setStyleSheet("font: 63 10pt \"Bookman Old Style\";\n"
"font: 63 12pt \"Bookman Old Style\";\n"
"color: rgb(0, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.t2_pb_reset.setObjectName("t2_pb_reset")
        self.horizontalLayout.addWidget(self.t2_pb_reset)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget5 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget5.setGeometry(QtCore.QRect(230, 75, 461, 341))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.t3_le_price = QtWidgets.QLineEdit(self.layoutWidget5)
        self.t3_le_price.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t3_le_price.setObjectName("t3_le_price")
        self.gridLayout_2.addWidget(self.t3_le_price, 2, 1, 1, 2)
        self.t3_le_fid = QtWidgets.QLineEdit(self.layoutWidget5)
        self.t3_le_fid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t3_le_fid.setObjectName("t3_le_fid")
        self.gridLayout_2.addWidget(self.t3_le_fid, 0, 1, 1, 2)
        self.t3_le_fname = QtWidgets.QLineEdit(self.layoutWidget5)
        self.t3_le_fname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t3_le_fname.setObjectName("t3_le_fname")
        self.gridLayout_2.addWidget(self.t3_le_fname, 1, 1, 1, 2)
        self.t3_pb_del = QtWidgets.QPushButton(self.layoutWidget5)
        self.t3_pb_del.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.t3_pb_del.setObjectName("t3_pb_del")
        self.gridLayout_2.addWidget(self.t3_pb_del, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_4.setStyleSheet("font: 63 11pt \"Bookman Old Style\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.t3_pb_mod = QtWidgets.QPushButton(self.layoutWidget5)
        self.t3_pb_mod.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.t3_pb_mod.setObjectName("t3_pb_mod")
        self.gridLayout_2.addWidget(self.t3_pb_mod, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_6.setStyleSheet("font: 63 11pt \"Bookman Old Style\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.t3_pb_add = QtWidgets.QPushButton(self.layoutWidget5)
        self.t3_pb_add.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.t3_pb_add.setObjectName("t3_pb_add")
        self.gridLayout_2.addWidget(self.t3_pb_add, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_5.setStyleSheet("font: 63 11pt \"Bookman Old Style\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.t3_pb_reset = QtWidgets.QPushButton(self.layoutWidget5)
        self.t3_pb_reset.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.t3_pb_reset.setObjectName("t3_pb_reset")
        self.gridLayout_2.addWidget(self.t3_pb_reset, 4, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.t4_tw = QtWidgets.QTableWidget(self.tab_4)
        self.t4_tw.setGeometry(QtCore.QRect(370, 10, 421, 331))
        self.t4_tw.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t4_tw.setObjectName("t4_tw")
        self.t4_tw.setColumnCount(4)
        self.t4_tw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.t4_tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.t4_tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.t4_tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.t4_tw.setHorizontalHeaderItem(3, item)
        self.t4_total = QtWidgets.QLabel(self.tab_4)
        self.t4_total.setGeometry(QtCore.QRect(655, 350, 131, 69))
        self.t4_total.setStyleSheet("\n"
"background-color: rgb(255, 255, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.t4_total.setAlignment(QtCore.Qt.AlignCenter)
        self.t4_total.setObjectName("t4_total")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(580, 350, 67, 69))
        self.label_19.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.layoutWidget6 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 20, 291, 231))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_16.setStyleSheet("font: 63 11pt \"Bookman Old Style\";")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)
        self.t4_from = QtWidgets.QDateEdit(self.layoutWidget6)
        self.t4_from.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t4_from.setAlignment(QtCore.Qt.AlignCenter)
        self.t4_from.setCalendarPopup(False)
        self.t4_from.setDate(QtCore.QDate(2020, 1, 1))
        self.t4_from.setObjectName("t4_from")
        self.gridLayout_5.addWidget(self.t4_from, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_17.setStyleSheet("font: 63 11pt \"Bookman Old Style\";")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 1, 0, 1, 1)
        self.t4_to = QtWidgets.QDateEdit(self.layoutWidget6)
        self.t4_to.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t4_to.setAlignment(QtCore.Qt.AlignCenter)
        self.t4_to.setCalendarPopup(False)
        self.t4_to.setDate(QtCore.QDate(2020, 1, 1))
        self.t4_to.setObjectName("t4_to")
        self.gridLayout_5.addWidget(self.t4_to, 1, 1, 1, 1)
        self.t4_pb_GR = QtWidgets.QPushButton(self.layoutWidget6)
        self.t4_pb_GR.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.t4_pb_GR.setObjectName("t4_pb_GR")
        self.gridLayout_5.addWidget(self.t4_pb_GR, 2, 1, 1, 1)
        self.t4_pb_download = QtWidgets.QPushButton(self.layoutWidget6)
        self.t4_pb_download.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.t4_pb_download.setObjectName("t4_pb_download")
        self.gridLayout_5.addWidget(self.t4_pb_download, 2, 0, 1, 1)
        self.t4_tot_orders = QtWidgets.QLabel(self.tab_4)
        self.t4_tot_orders.setGeometry(QtCore.QRect(460, 350, 111, 69))
        self.t4_tot_orders.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.t4_tot_orders.setAlignment(QtCore.Qt.AlignCenter)
        self.t4_tot_orders.setObjectName("t4_tot_orders")
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(370, 350, 91, 69))
        self.label_20.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "XYZ RESTAURANT"))
        item = self.t1_tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Food Name"))
        item = self.t1_tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Unit Price"))
        item = self.t1_tw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.t1_tw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        self.t1_pb_receipt.setText(_translate("MainWindow", "Receipt"))
        self.t1_l_fid.setText(_translate("MainWindow", "Food ID"))
        self.t1_l_fname.setText(_translate("MainWindow", "Food Name"))
        self.t1_l_price.setText(_translate("MainWindow", "Price"))
        self.t1_l_qty.setText(_translate("MainWindow", "Quantity"))
        self.t1_pb_ATC.setText(_translate("MainWindow", "Add to Cart"))
        self.t1_pb_GD.setText(_translate("MainWindow", "Get details"))
        self.label_12.setText(_translate("MainWindow", "Total"))
        self.label_13.setText(_translate("MainWindow", "Tax"))
        self.label_14.setText(_translate("MainWindow", "Grand Total"))
        self.t1_grandtotal.setText(_translate("MainWindow", "0"))
        self.t1_displaytotal.setText(_translate("MainWindow", "0"))
        self.t1_displaytax.setText(_translate("MainWindow", "0"))
        self.t1_pb_del_itm.setText(_translate("MainWindow", "Delete Item"))
        self.label_11.setText(_translate("MainWindow", "Order No"))
        self.t1_pb_new_order.setText(_translate("MainWindow", "New Order"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Order"))
        self.label_3.setText(_translate("MainWindow", "Food Name"))
        self.label_2.setText(_translate("MainWindow", "Food ID"))
        self.t2_pb_search.setText(_translate("MainWindow", "Search"))
        item = self.t2_tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Food ID"))
        item = self.t2_tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Food Price"))
        item = self.t2_tw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Unit Price"))
        self.t2_pb_VD.setText(_translate("MainWindow", "View All Details"))
        self.t2_pb_reset.setText(_translate("MainWindow", "RESET"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Food Details"))
        self.t3_pb_del.setText(_translate("MainWindow", "Delete"))
        self.label_4.setText(_translate("MainWindow", "Food ID"))
        self.t3_pb_mod.setText(_translate("MainWindow", "Modify"))
        self.label_6.setText(_translate("MainWindow", "Unit Price"))
        self.t3_pb_add.setText(_translate("MainWindow", "Add"))
        self.label_5.setText(_translate("MainWindow", "Food Name"))
        self.t3_pb_reset.setText(_translate("MainWindow", "RESET"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Update Details"))
        item = self.t4_tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Year"))
        item = self.t4_tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Month"))
        item = self.t4_tw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total Orders"))
        item = self.t4_tw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sales Amount"))
        self.t4_total.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "Grand Total"))
        self.label_16.setText(_translate("MainWindow", "From Date"))
        self.t4_from.setDisplayFormat(_translate("MainWindow", "yyyy/MM"))
        self.label_17.setText(_translate("MainWindow", "To Date"))
        self.t4_to.setDisplayFormat(_translate("MainWindow", "yyyy/MM"))
        self.t4_pb_GR.setText(_translate("MainWindow", "Get Report"))
        self.t4_pb_download.setText(_translate("MainWindow", "Download"))
        self.t4_tot_orders.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "Total Orders"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
