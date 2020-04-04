from naturals import Natural

def parse_naturals(num1, num2):
    if num1 == "" or num2 == "":
        # Вывести диалог с ошибкой, пока не сделано
        return
    
    elif not num1.isdigit() or not num2.isdigit():
        # Вывести диалог с ошибкой, пока не сделано
        return

def naturals_sum(window):
    num1 = window.firstNumLine.text()
    num2 = window.secondNumLine.text()

    parse_naturals(num1, num2)

    a = Natural(num1)
    b = Natural(num2)
    ans = a + b

    window.answer_field.setText("Сумма: " + str(ans))


def naturals_sub(window):
    num1 = window.firstNumLine.text()
    num2 = window.secondNumLine.text()

    parse_naturals(num1, num2)

    a = Natural(num1)
    b = Natural(num2)

    # Если первое число меньше второго
    if a.COM_NN_D(b) == 1:
        # Вывести диалог с ошибкой, пока не сделано
        return

    ans = a - b

    window.answer_field.setText("Разность: " + str(ans))


def naturals_mult(window):
    num1 = window.firstNumLine.text()
    num2 = window.secondNumLine.text()

    parse_naturals(num1, num2)

    a = Natural(num1)
    b = Natural(num2)

    ans = a * b

    window.answer_field.setText("Произведение: " + str(ans))