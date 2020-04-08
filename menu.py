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
        n_sub = QAction("Разность", self)
        n_mult = QAction("Умножение", self)
        n_div = QAction("Деление", self)
        n_mod = QAction("Деление с остатком", self)
        n_gcd = QAction("НОД", self)
        n_lcm = QAction("НОК", self)
        
        bar_elements = [n_sum, n_sub, n_mult, n_div, n_mod, n_gcd, n_lcm]
        bar_actions = [self.n_add_window, self.n_sub_window, self.n_mult_window, self.n_div_window,
                            self.n_mod_window, self.n_gcd_window, self.n_lcm_window]

        self.set_bar(natural, bar_elements, bar_actions)


        whole = menubar.addMenu("Целые числа")

        w_sum = QAction("Сумма", self)
        w_dif = QAction("Разность", self)
        w_mult = QAction("Умножение", self)
        w_div = QAction("Деление", self)
        w_mod = QAction("Деление с остатком", self)
        w_gcd = QAction("НОД", self)
        w_lcm = QAction("НОК", self)

        bar_elements = [w_sum, w_dif, w_mult, w_div, w_mod, w_gcd, w_lcm]
        bar_actions = [self.w_sum_window, self.w_dif_window, self.w_mult_window, self.w_div_window,
                            self.w_mod_window, self.w_gcd_window, self.w_lcm_window]

        self.set_bar(whole, bar_elements, bar_actions)


        rational = menubar.addMenu("Рациональные числа")
        polynoms = menubar.addMenu("Многочлены")

        self.setFixedSize(QSize(550, 350))
        self.move(300, 300)
        self.setWindowTitle("Компьютерная алгебра")
        
        self.show()

    
    # Заполняем окно для "Натурльные числа" по шаблону
    def fillNaturalWholeWindow(self, buttonName, actionFunc):
        self.clear_widgets()

        self.first_num_line = QLineEdit(self)
        self.second_num_line = QLineEdit(self)
        self.action_button = QPushButton(self)
        self.active_widgets = [self.first_num_line, self.second_num_line, self.action_button]

        self.first_num_line.move(20, 40)
        self.second_num_line.move(140, 40)
        self.action_button.move(270, 40)
        self.action_button.resize(200, 30)
        self.action_button.setText(buttonName)
        self.action_button.clicked.connect(partial(actionFunc, self))

        self.answer_field.move(41, 80)
        # Большая ширина, чтобы влезали ответы
        self.answer_field.resize(400, 30)

        self.show_widgets()

    # НАТУРАЛЬНЫЕ ==================================================================
    
    def n_add_window(self):
        self.fillNaturalWholeWindow("Вычислить сумму", handlers.naturals_sum)
        
    def n_sub_window(self):
        self.fillNaturalWholeWindow("Вычислить разность", handlers.naturals_sub)

    def n_mult_window(self):
        self.fillNaturalWholeWindow("Вычислить произведение", handlers.naturals_mult)

    def n_div_window(self):
        self.fillNaturalWholeWindow("Вычислить частное", handlers.naturals_div)

    def n_mod_window(self):
        self.fillNaturalWholeWindow("Вычислить остаток", handlers.naturals_mod)

    def n_gcd_window(self):
        self.fillNaturalWholeWindow("Вычислить НОД", handlers.naturals_gcd)

    def n_lcm_window(self):
        self.fillNaturalWholeWindow("Вычислить НОК", handlers.naturals_lcm)

    # ==============================================================================

    # ЦЕЛЫЕ ========================================================================

    def w_sum_window(self):
        self.fillNaturalWholeWindow("Вычислить сумму", handlers.whole_sum)

    def w_dif_window(self):
        self.fillNaturalWholeWindow("Вычислить разность", handlers.whole_dif)

    def w_mult_window(self):
        self.fillNaturalWholeWindow("Вычислить произведение", handlers.whole_mult)

    def w_div_window(self):
        self.fillNaturalWholeWindow("Вычислить частное", handlers.whole_div)

    def w_mod_window(self):
        self.fillNaturalWholeWindow("Вычислить остаток", handlers.whole_mod)

    def w_gcd_window(self):
        self.fillNaturalWholeWindow("Вычислить НОД", handlers.whole_gcd)

    def w_lcm_window(self):
        self.fillNaturalWholeWindow("Вычислить НОК", handlers.whole_lcm)


    # ==============================================================================


    def set_bar(self, bar, bar_elements, bar_actions):
        for idx in range(len(bar_elements)):
            bar.addAction(bar_elements[idx])
            bar_elements[idx].triggered.connect(bar_actions[idx])

    
    def set_actions(self, actions):
        self.fillNaturalWholeWindow("Вычислить НОК", handlers.naturals_lcm)


    def show_widgets(self):
        for widget in self.active_widgets:
            widget.show()


    def clear_widgets(self):
        for idx in range(len(self.active_widgets)):
            self.active_widgets[idx].deleteLater()
        self.active_widgets.clear()
        self.answer_field.clear()
    
    
    def showError(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = CalcWindow()
    sys.exit(app.exec_())
