import sys
from all_criteria import Ui_Form as AllCriteriaWindow
from three_criteria import Ui_Form as ThreeCriteriaWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QTableWidgetItem, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import UTA_star
import FTopsis
import SWD_RSM

# Allows to display matplotlib charts on screen. 

class MatplotlibWidget(QWidget):
    def __init__(self, parent = None):
        super(MatplotlibWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axis = self.figure.add_subplot(111, projection='3d')

        self.layoutvertical = QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)

# Allows to switch between screens.

class Widgets:
    def __init__(self):
        self.s_widget = qtw.QStackedWidget()
        all_criteria = AllCriteriaWidget(self.s_widget)
        three_criteria = ThreeCriteriaWidget(self.s_widget)
        self.s_widget.addWidget(all_criteria)
        self.s_widget.addWidget(three_criteria)
        self.s_widget.setFixedSize(800, 800)
        self.s_widget.show()

# First screen contains methods for all criteria ranking.

class AllCriteriaWidget(QWidget, AllCriteriaWindow):
    def __init__(self, s_widget, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.three_criteria_button.clicked.connect(self.change_window)
        self.s_widget = s_widget
        self.setAttribute(qtc.Qt.WA_StyledBackground, True)

        self.table_widget.setColumnWidth(0, 100)
        self.table_widget.setColumnWidth(1, 70)
        self.table_widget.setColumnWidth(2, 70)
        self.table_widget.setColumnWidth(3, 70)
        self.table_widget.setColumnWidth(4, 80)
        self.table_widget.setColumnWidth(5, 100)
        self.table_widget.setColumnWidth(6, 70)
        self.table_widget.setColumnWidth(7, 80)
        self.table_widget.setColumnWidth(8, 60)
        self.table_widget.setColumnWidth(9, 80)
        self.table_widget.setColumnWidth(11, 120)
        self.table_widget.setColumnWidth(14, 80)
        self.table_widget.setColumnWidth(15, 60)

        self.actual_method = ''

        self.topsis_button.clicked.connect(self.set_topsis)
        self.rsm_button.clicked.connect(self.set_rms)
        self.uta_button.clicked.connect(self.set_uta_star)

        self.create_ranking.clicked.connect(self.calculate_ranking)
    
    # Calculates ranking based on selected properties and displays it.

    def calculate_ranking(self):
        if self.actual_method in ['Topsis', 'RMS', 'UTA_star']:
            n_rows = self.row_spinbox.value()
            fuel_preference = self.fuel_combobox.currentText()
            if self.actual_method == 'Topsis':
                if fuel_preference == 'Diesel':
                    df = FTopsis.ranking_to_dataframe_all(n_rows, True)
                    ranking = df.values
                    self.table_widget.setRowCount(n_rows)
                    self.display_ranking(ranking)
                else:
                    df = FTopsis.ranking_to_dataframe_all(n_rows, False)
                    ranking = df.values
                    self.table_widget.setRowCount(n_rows)
                    self.display_ranking(ranking)
            elif self.actual_method == 'RMS':
                if fuel_preference == 'Diesel':
                    df, classes = SWD_RSM.rsm([], True, n_rows)
                    ranking = df.values
                    self.table_widget.setRowCount(n_rows)
                    self.display_ranking(ranking)
                else:
                    df, classes = SWD_RSM.rsm([], False, n_rows)
                    ranking = df.values
                    self.table_widget.setRowCount(n_rows)
                    self.display_ranking(ranking)
            else:
                df = UTA_star.get_UTA_ranking_all_criteria(fuel_preference, n_rows)
                ranking = df.values
                self.table_widget.setRowCount(n_rows)
                self.display_ranking(ranking)
        else:
            QMessageBox.warning(self, "Błąd", "Nie wybrano metody!")

    def display_ranking(self, ranking):
        for row in range(len(ranking)):
            for col in range(len(ranking[0])):
                self.table_widget.setItem(row, col, QTableWidgetItem(str(ranking[row][col])))

    def change_window(self):
        self.s_widget.setCurrentIndex(self.s_widget.currentIndex() + 1)

    def set_topsis(self):
        self.actual_method = 'Topsis'

    def set_rms(self):
        self.actual_method = 'RMS'
    
    def set_uta_star(self):
        self.actual_method = 'UTA_star'

# Second screen contains methods for three criteria ranking.

class ThreeCriteriaWidget(QWidget, ThreeCriteriaWindow):
    def __init__(self, s_widget, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.all_criteria_button.clicked.connect(self.change_window)
        self.s_widget = s_widget
        self.setAttribute(qtc.Qt.WA_StyledBackground, True)
        self.init_widget()

        self.table_widget.setColumnWidth(0, 82)
        self.table_widget.setColumnWidth(1, 82)
        self.table_widget.setColumnWidth(2, 82)
        self.table_widget.setColumnWidth(3, 82)
        self.table_widget.setColumnWidth(4, 0)

        self.actual_method = ''

        self.first_criterion_combobox.currentTextChanged.connect(self.change_first_criterion)
        self.second_criterion_combobox.currentTextChanged.connect(self.change_second_criterion)
        self.third_criterion_combobox.currentTextChanged.connect(self.change_third_criterion)

        self.topsis_method.clicked.connect(self.set_topsis)
        self.rsm_method.clicked.connect(self.set_rms)
        self.uta_method.clicked.connect(self.set_uta_star)

        self.create_ranking.clicked.connect(self.calculate_and_display_ranking)

    # Calculates ranking based on selected properties and displays it, but this time for three criteria.

    def calculate_and_display_ranking(self):
        first_criterion = self.first_criterion_combobox.currentText()
        second_criterion = self.second_criterion_combobox.currentText()
        third_criterion = self.third_criterion_combobox.currentText()
        if first_criterion != second_criterion and second_criterion != third_criterion and third_criterion != first_criterion:
            if self.actual_method in ['Topsis', 'RMS', 'UTA_star']:
                criteria = [first_criterion, second_criterion, third_criterion]
                n_rows = self.max_rows_spinbox.value()
                if self.actual_method == 'Topsis':
                    df, classes = FTopsis.ranking_to_dataframe_three(criteria, n_rows)
                    ranking = df.values
                    self.table_widget.setRowCount(n_rows)
                    self.display_ranking(ranking)
                    self.display_chart(classes)
                elif self.actual_method == 'RMS':
                    df, classes = SWD_RSM.rsm(criteria, False, n_rows)
                    ranking = df.values
                    self.table_widget.setRowCount(n_rows)
                    self.display_ranking(ranking)
                    self.display_chart(classes)
                else:
                    df, classes = UTA_star.get_UTA_ranking_three_criteria(criteria, n_rows)
                    ranking = df.values
                    self.table_widget.setRowCount(n_rows)
                    self.display_ranking(ranking)
                    self.display_chart(classes)
            else:
                QMessageBox.warning(self, "Błąd", "Nie wybrano metody!")
        else:
            QMessageBox.warning(self, "Błąd", "Kryteria muszą być różne od siebie!")
    
    def display_ranking(self, ranking):
        for row in range(len(ranking)):
            for col in range(len(ranking[0])):
                self.table_widget.setItem(row, col, QTableWidgetItem(str(ranking[row][col])))

    # Displays chart on screen.

    def display_chart(self, classes):
        self.matplotlibwidget.axis.clear()
        colors = ['orange', 'green', 'red']
        for index, new_class in enumerate(classes):
            if index == 0:
                x = []
                y = []
                z = []
                for element in new_class:
                    x.append(element[0])
                    y.append(element[1])
                    z.append(element[2])
                self.matplotlibwidget.axis.scatter3D(x[0], y[0], z[0], color = 'black')
                self.matplotlibwidget.axis.scatter3D(x[1:], y[1:], z[1:], color = colors[0])
            else:
                x = []
                y = []
                z = []
                for element in new_class:
                    x.append(element[0])
                    y.append(element[1])
                    z.append(element[2])
                self.matplotlibwidget.axis.scatter3D(x, y, z, color = colors[index])
        self.matplotlibwidget.canvas.draw()

    def set_topsis(self):
        self.actual_method = 'Topsis'

    def set_rms(self):
        self.actual_method = 'RMS'
    
    def set_uta_star(self):
        self.actual_method = 'UTA_star'

    def change_window(self):
        self.s_widget.setCurrentIndex(self.s_widget.currentIndex() - 1)

    def change_first_criterion(self):
        new_criterion = self.first_criterion_combobox.currentText()
        self.table_widget.setHorizontalHeaderItem(1, QTableWidgetItem(new_criterion))

    def change_second_criterion(self):
        new_criterion = self.second_criterion_combobox.currentText()
        self.table_widget.setHorizontalHeaderItem(2, QTableWidgetItem(new_criterion))

    def change_third_criterion(self):
        new_criterion = self.third_criterion_combobox.currentText()
        self.table_widget.setHorizontalHeaderItem(3, QTableWidgetItem(new_criterion))

    def init_widget(self):
        self.matplotlibwidget = MatplotlibWidget()
        self.layoutvertical = QVBoxLayout(self.chart)
        self.layoutvertical.addWidget(self.matplotlibwidget)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    widgets = Widgets()
    app.exec_()