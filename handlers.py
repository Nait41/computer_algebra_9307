from naturals import Natural
from whole import Whole

def parse_naturals(window, num1, num2):
    if num1 == "" or num2 == "":
        window.showError("Одно из полей пусто")
        return 0
    
    elif not num1.isdigit() or not num2.isdigit():
        window.showError("Одно из чисел содержит недопустимые символы")
        return 0

    return 1

def parse_wholes(window, num1, num2):
    if num1 == "" or num2 == "":
        window.showError("Одно из полей пусто")
        return 0
    
    if (num1[0] == "-" and not num1[1:].isdigit()) or (not num1[0] == "-" and not num1.isdigit()):
        window.showError("Одно из чисел содержит недопустимые символы")
        return 0
    
    if (num2[0] == "-" and not num2[1:].isdigit()) or (not num2[0] == "-" and not num2.isdigit()):
        window.showError("Одно из чисел содержит недопустимые символы")
        return 0

    return 1


def exctract_natural_numbers(window):
    num1 = window.first_num_line.text()
    num2 = window.second_num_line.text()

    error_code = parse_naturals(window, num1, num2)
    # Если ошибка, то возвращаем просто (0, 0)
    if not error_code:
        return 0, 0

    a = Natural(num1)
    b = Natural(num2)

    return a, b


def exctract_whole_numbers(window):
    num1 = window.first_num_line.text()
    num2 = window.second_num_line.text()

    error_code = parse_wholes(window, num1, num2)
    # Если ошибка, то возвращаем просто (0, 0)
    if not error_code:
        return 0, 0

    a = Whole(num1)
    b = Whole(num2)

    return a, b



def naturals_sum(window):
    a, b = exctract_natural_numbers(window)
    if (a, b) == (0, 0):
        return

    ans = a + b
    window.answer_field.setText("Сумма: " + str(ans))


def naturals_sub(window):
    a, b = exctract_natural_numbers(window)
    if (a, b) == (0, 0):
        return

    if a.COM_NN_D(b) == 1:
        window.showError("Второе число должно быть меньше первого")
        return

    ans = a - b
    window.answer_field.setText("Разность: " + str(ans))


def naturals_mult(window):
    a, b = exctract_natural_numbers(window)
    if (a, b) == (0, 0):
        return

    ans = a * b
    window.answer_field.setText("Произведение: " + str(ans))


def naturals_div(window):
    a, b = exctract_natural_numbers(window)
    if (a, b) == (0, 0):
        return

    if a.COM_NN_D(b) == 1:
        window.showError("Второе число должно быть меньше первого")
        return

    ans = a // b
    window.answer_field.setText("Частное: " + str(ans))


def naturals_mod(window):
    a, b = exctract_natural_numbers(window)
    if (a, b) == (0, 0):
        return

    if a.COM_NN_D(b) == 1:
        window.showError("Второе число должно быть меньше первого")
        return

    ans = a % b
    window.answer_field.setText("Отстаток от деления: " + str(ans))


def naturals_gcd(window):
    a, b = exctract_natural_numbers(window)
    if (a, b) == (0, 0):
        return

    ans = a.GCF_NN_N(b)
    window.answer_field.setText("НОД: " + str(ans))


def naturals_lcm(window):
    a, b = exctract_natural_numbers(window)
    if (a, b) == (0, 0):
        return

    ans = a.LCM_NN_N(b)
    window.answer_field.setText("НОК: " + str(ans))


def whole_sum(window):
    a, b = exctract_whole_numbers(window)
    if (a, b) == (0, 0):
        return

    ans = a + b
    window.answer_field.setText("Сумма: " + str(ans))


def whole_dif(window):
    a, b = exctract_whole_numbers(window)
    if (a, b) == (0, 0):
        return

    ans = a - b
    window.answer_field.setText("Разность: " + str(ans))


def whole_mult(window):
    a, b = exctract_whole_numbers(window)
    if (a, b) == (0, 0):
        return

    ans = a * b
    window.answer_field.setText("Произведение: " + str(ans))

def whole_div(window):
    a, b = exctract_whole_numbers(window)
    if (a, b) == (0, 0):
        return

    # Если b <= 0, или a < 0, или a < b
    if b.POZ_Z_D() in [0, 1] or a.POZ_Z_D() in [0, 1] or a.ABS_Z_N().COM_NN_D(b.ABS_Z_N()) == 1:
        window.showError("Первое число должно быть положительным, второе число должно быть больше первого")
        return

    ans = a // b
    window.answer_field.setText("Частное: " + str(ans))


def whole_mod(window):
    a, b = exctract_whole_numbers(window)
    if (a, b) == (0, 0):
        return

    # Если b <= 0, или a < 0, или a < b
    if b.POZ_Z_D() in [0, 1] or a.POZ_Z_D() in [0, 1] or a.ABS_Z_N().COM_NN_D(b.ABS_Z_N()) == 1:
        window.showError("Первое число должно быть положительным, второе число должно быть больше первого")
        return

    ans = a % b
    window.answer_field.setText("Остаток: " + str(ans))


def whole_gcd(window):
    a, b = exctract_whole_numbers(window)
    if (a, b) == (0, 0):
        return

    a, b = a.ABS_Z_N(), b.ABS_Z_N()
    ans = a.GCF_NN_N(b)
    window.answer_field.setText("НОД: " + str(ans))


def whole_lcm(window):
    a, b = exctract_whole_numbers(window)
    if (a, b) == (0, 0):
        return

    a, b = a.ABS_Z_N(), b.ABS_Z_N()
    ans = a.LCM_NN_N(b)
    window.answer_field.setText("НОК: " + str(ans))
