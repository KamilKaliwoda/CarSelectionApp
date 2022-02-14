# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_criteria.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(240, 10, 471, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setAutoFillBackground(False)
        self.title_label.setStyleSheet("color: rgb(234, 234, 234);")
        self.title_label.setScaledContents(True)
        self.title_label.setWordWrap(False)
        self.title_label.setObjectName("title_label")
        self.three_criteria_button = QtWidgets.QPushButton(Form)
        self.three_criteria_button.setGeometry(QtCore.QRect(10, 10, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.three_criteria_button.setFont(font)
        self.three_criteria_button.setStyleSheet("background-color: rgb(170, 170, 170);\n"
"color: rgb(21, 21, 21);")
        self.three_criteria_button.setObjectName("three_criteria_button")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 781, 701))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.method_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.method_label.setFont(font)
        self.method_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.method_label.setObjectName("method_label")
        self.horizontalLayout.addWidget(self.method_label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topsis_button = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.topsis_button.setFont(font)
        self.topsis_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.topsis_button.setObjectName("topsis_button")
        self.verticalLayout_2.addWidget(self.topsis_button)
        self.rsm_button = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.rsm_button.setFont(font)
        self.rsm_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.rsm_button.setObjectName("rsm_button")
        self.verticalLayout_2.addWidget(self.rsm_button)
        self.uta_button = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.uta_button.setFont(font)
        self.uta_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.uta_button.setObjectName("uta_button")
        self.verticalLayout_2.addWidget(self.uta_button)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fuel_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.fuel_label.setFont(font)
        self.fuel_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.fuel_label.setObjectName("fuel_label")
        self.horizontalLayout_2.addWidget(self.fuel_label)
        self.fuel_combobox = QtWidgets.QComboBox(self.layoutWidget)
        self.fuel_combobox.setStyleSheet("background-color: rgb(170, 170, 170);\n"
"color: rgb(0, 0, 0);")
        self.fuel_combobox.setObjectName("fuel_combobox")
        self.fuel_combobox.addItem("")
        self.fuel_combobox.addItem("")
        self.horizontalLayout_2.addWidget(self.fuel_combobox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.max_rows_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.max_rows_label.setFont(font)
        self.max_rows_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.max_rows_label.setObjectName("max_rows_label")
        self.horizontalLayout_3.addWidget(self.max_rows_label)
        self.row_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.row_spinbox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 170);")
        self.row_spinbox.setMinimum(5)
        self.row_spinbox.setMaximum(100)
        self.row_spinbox.setSingleStep(5)
        self.row_spinbox.setObjectName("row_spinbox")
        self.horizontalLayout_3.addWidget(self.row_spinbox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.create_ranking = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_ranking.sizePolicy().hasHeightForWidth())
        self.create_ranking.setSizePolicy(sizePolicy)
        self.create_ranking.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.create_ranking.setFont(font)
        self.create_ranking.setAutoFillBackground(False)
        self.create_ranking.setStyleSheet("background-color: rgb(170, 170, 170);\n"
"color: rgb(0, 0, 0);")
        self.create_ranking.setObjectName("create_ranking")
        self.horizontalLayout_5.addWidget(self.create_ranking)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.table_widget = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_widget.setStyleSheet("background-color: rgb(170, 170, 170);\n"
"border-color: rgb(170, 170, 170);\n"
"selection-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(170, 170, 170);\n"
"color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 170, 170);\n"
"")
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(16)
        self.table_widget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.table_widget.setHorizontalHeaderItem(15, item)
        self.verticalLayout.addWidget(self.table_widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "Ranking dla wszystkich kryteriów"))
        self.three_criteria_button.setText(_translate("Form", "Ranking dla 3 kryteriów"))
        self.method_label.setText(_translate("Form", "Wybór metody"))
        self.topsis_button.setText(_translate("Form", "Fuzzy Topsis"))
        self.rsm_button.setText(_translate("Form", "Punktów odniesienia"))
        self.uta_button.setText(_translate("Form", "UTA Star "))
        self.fuel_label.setText(_translate("Form", "Preferowany rodzaj paliwa"))
        self.fuel_combobox.setItemText(0, _translate("Form", "Benzyna"))
        self.fuel_combobox.setItemText(1, _translate("Form", "Diesel"))
        self.max_rows_label.setText(_translate("Form", "Maksymalna ilość wierszy w rankingu"))
        self.create_ranking.setText(_translate("Form", "Wyznacz ranking"))
        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Marka i model"))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Rocznik"))
        item = self.table_widget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Cena"))
        item = self.table_widget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Przebieg"))
        item = self.table_widget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Moc silnika"))
        item = self.table_widget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Pojemność silnika"))
        item = self.table_widget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Spalanie"))
        item = self.table_widget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Masa"))
        item = self.table_widget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Paliwo"))
        item = self.table_widget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Ilość drzwi"))
        item = self.table_widget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Ilość miejsc"))
        item = self.table_widget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Pojemność bagażnika"))
        item = self.table_widget.horizontalHeaderItem(12)
        item.setText(_translate("Form", "Skrzynia biegów"))
        item = self.table_widget.horizontalHeaderItem(13)
        item.setText(_translate("Form", "Klimatyzacja"))
        item = self.table_widget.horizontalHeaderItem(14)
        item.setText(_translate("Form", "Gwarancja"))
        item = self.table_widget.horizontalHeaderItem(15)
        item.setText(_translate("Form", "Opinia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
