from naturals import Natural

class Whole:
    def __init__(self, number_str):
        self.sign = 0
        self.natural_repr = None

        if number_str[0] == "-":
            self.natural_repr = Natural(number_str[1:])
            self.sign = 1
        else:
            self.natural_repr = Natural(number_str)

    def __str__(self):
        return str(self.natural_repr) if not self.sign else "-" + str(self.natural_repr)

    """
    Автор: Багиев Арслан
    Назначение: абсолютная величина
    """
    def ABS_Z_N(self):
        return self.natural_repr

    """
    Автор: Багиев Арслан
    Назначение: определение положительности
    """
    def POZ_Z_D(self):
        if not self.natural_repr.number[0]:
            return 0
        elif self.sign == 1:
            return 1
        elif self.sign == 0:
            return 2

    """
    Автор: Левицкий Дмитрий
    Назначение: умножение на -1
    """
    def MUL_ZM_Z(self):
        if self.sign:
            self.sign = 0
        else:
            self.sign = 1

    """
    Автор: Левицкий Дмитрий
    Назначение: сложение целых
    Каноническое название: ADD_ZZ_Z
    """
    def __add__(self, another):
        first = self.ABS_Z_N()
        second = another.ABS_Z_N()
        if (self.POZ_Z_D() == 2 and another.POZ_Z_D() == 2) or (self.POZ_Z_D() == 1 and another.POZ_Z_D() == 1):
            res = TRANS_N_Z(first + second)
            if self.POZ_Z_D() == 1 and another.POZ_Z_D() == 1:
                res.MUL_ZM_Z()
        elif first.COM_NN_D(second) == 2:
            res = TRANS_N_Z(first - second)
            if self.POZ_Z_D() == 1:
                res.MUL_ZM_Z()
        elif first.COM_NN_D(second) == 1:
            res = TRANS_N_Z(second - first)
            if another.POZ_Z_D() == 1:
                res.MUL_ZM_Z()
        else:
            res = TRANS_N_Z(Natural("0"))
        return res

    """
    Автор: Левицкий Дмитрий
    Назначение: вычитание целых
    Каноническое название: SUB_ZZ_Z
    """
    def __sub__(self, another):
        first = self.ABS_Z_N()
        second = another.ABS_Z_N()
        if (self.POZ_Z_D() == 2 and another.POZ_Z_D() == 1) or (self.POZ_Z_D() == 1 and another.POZ_Z_D() == 2):
            res = TRANS_N_Z(first + second)
            if self.POZ_Z_D() == 1 and another.POZ_Z_D() == 2:
                res.MUL_ZM_Z()
        elif first.COM_NN_D(second) == 2:
            res = TRANS_N_Z(first - second)
            if another.POZ_Z_D() == 1:
                res.MUL_ZM_Z()
        elif first.COM_NN_D(second) == 1:
            res = TRANS_N_Z(second - first)
            if self.POZ_Z_D() == 1:
                res.MUL_ZM_Z()
        else:
            res = Whole("0")
        return res

    """
    Автор: Левицкий Дмитрий
    Назначение: умножение целых
    Каноническое название: MUL_ZZ_Z
    """
    def __mul__(self, another):
        first = self.ABS_Z_N()
        second = another.ABS_Z_N()
        res = TRANS_N_Z(first * second)
        if (self.POZ_Z_D() == 2 and another.POZ_Z_D() == 1) or (self.POZ_Z_D() == 1 and another.POZ_Z_D() == 2):
            if res.natural_repr.number[0]:
                res.MUL_ZM_Z()
        return res

    """
    Автор: Левицкий Дмитрий
    Назначение: частное от деления целого на натуральное
    Каноническое название: DIV_ZZ_Z
    """
    def __floordiv__(self, another):
        first = self.ABS_Z_N()
        second = another.ABS_Z_N()
        res = TRANS_N_Z(first // second)
        if (self.POZ_Z_D() == 2 and another.POZ_Z_D() == 1) or (self.POZ_Z_D() == 1 and another.POZ_Z_D() == 2):
            if res.natural_repr.number[0]:
                res.MUL_ZM_Z()
        return res

    """
    Автор: Левицкий Дмитрий
    Назначение: остаток от деления целого на натуральное
    Каноническое название: MOD_ZZ_Z
    """
    def __mod__(self, another):
        first = self.ABS_Z_N()
        second = another.ABS_Z_N()
        if self.POZ_Z_D() == 1:
            res = TRANS_N_Z((second - first % second) % second)
        else:
            res = TRANS_N_Z(first % second)
        return res

"""
Автор: Левицкий Дмитрий/Арутюнян Самвел
Назначение: перевод из натуральных в целые
"""
def TRANS_N_Z(natural_number):
    new_whole = Whole(str(natural_number))
    return new_whole


"""
Автор: Левицкий Дмитрий/Арутюнян Самвел
Назначение: перевод из целых в натуральные
"""
def TRANS_Z_N(whole_number):
    new_natural = whole_number.natural_repr
    return new_natural
