import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGridLayout,
                                QMenu, QAction, QLineEdit, QLabel, QPushButton)
from PyQt5.QtCore import QSize
import handlers
from functools import partial

class CalcWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.active_widgets = []
        self.answer_field = QLabel(self)
        self.initWindow()
    
    def initWindow(self):
        menubar = self.menuBar()

        natural = menubar.addMenu("Натуральные числа")
        
        n_sum = QAction("Сумма", self)
        n_sum.triggered.connect(self.add_window)

        n_sub = QAction("Разность", self)
        n_sub.triggered.connect(self.sub_window)

        n_mult = QAction("Умножение", self)
        n_mult.triggered.connect(self.mult_window)

        n_div = QAction("Деление", self)
        n_mod = QAction("Деление с остатком", self)
        n_GCD = QAction("НОД", self)
        n_LCM = QAction("НОК", self)
        
        self.setBar(natural, [n_sum, n_sub, n_mult, n_div,
                                  n_mod, n_GCD, n_LCM])


        whole = menubar.addMenu("Целые числа")

        w_abs = QAction("Абсолютное значение", self)
        w_sum = QAction("Сумма", self)
        w_dif = QAction("Разность", self)
        w_mult = QAction("Умножение", self)
        w_div = QAction("Деление", self)
        w_mod = QAction("Деление с остатком", self)
        w_GCD = QAction("НОД", self)
        w_LCM = QAction("НОК", self)

        # НАДО ЧТО-ТО ДОБАВИТЬ
        self.setBar(whole, [w_abs, w_sum, w_dif, w_mult,
                                  w_div, w_mod, w_GCD, w_LCM])


        rational = menubar.addMenu("Рациональные числа")
        polynoms = menubar.addMenu("Многочлены")

        self.setFixedSize(QSize(550, 350))
        self.move(300, 300)
        self.setWindowTitle("Компьютерная алгебра")
        
        self.show()

    
    # Заполняем окно для "Натурльные числа" по шаблону
    def fillNaturalsWindow(self, buttonName, actionFunc):
        self.clearWidgets()

        self.firstNumLine = QLineEdit(self)
        self.secondNumLine = QLineEdit(self)
        self.actionButton = QPushButton(self)
        self.active_widgets = [self.firstNumLine, self.secondNumLine, self.actionButton]

        self.firstNumLine.move(20, 40)
        self.secondNumLine.move(140, 40)
        self.actionButton.move(260, 40)
        self.actionButton.resize(180, 30)
        self.actionButton.setText(buttonName)
        self.actionButton.clicked.connect(partial(actionFunc, self))

        self.answer_field.move(41, 80)
        # Большая ширина, чтобы влезали ответы
        self.answer_field.resize(400, 30)

        self.showWidgets()


    def add_window(self):
        self.fillNaturalsWindow("Вычислить сумму", handlers.naturals_sum)
        

    def sub_window(self):
        self.fillNaturalsWindow("Вычислить разность", handlers.naturals_sub)


    def mult_window(self):
        self.fillNaturalsWindow("Вычислить произведение", handlers.naturals_mult)


    def setBar(self, bar, objs):
        for obj in objs:
            bar.addAction(obj)

    
    def setActions(self, actions):
        pass


    def showWidgets(self):
        for widget in self.active_widgets:
            widget.show()


    def clearWidgets(self):
        for widget in self.active_widgets:
            del widget



if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = CalcWindow()
    sys.exit(app.exec_())
