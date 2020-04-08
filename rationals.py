from whole import Whole, TRANS_N_Z

class Rational:
    # По умолчанию знаменатель = 1
    def __init__(self, numerator, denominator=Whole("1")):
        self.numerator = numerator
        self.denominator = denominator
    
    """
    Автор: Арутюнян Самвел
    Назначение: преобразование из дробного в целое
    """
    def TRANS_Q_Z(self):
        # ПРОВЕРЯТЬ, РАВЕН ЛИ ЗНАМЕНАТЕЛЬ 1 ПЕРЕД ВЫЗОВОМ
        return self.numerator


    """
    Автор: Арутюнян Самвел
    Назначение: сложение дробей
    Каноническое название: ADD_QQ_Q
    """
    def __add__(self, other):
        print(other.numerator)
        new_denominator = TRANS_N_Z(self.denominator.LCM_ZZ_Z(other.denominator))
        coef1, coef2 = new_denominator // self.denominator, new_denominator // other.denominator

        self.numerator *= coef1
        other.numerator *= coef2

        new_numerator = self.numerator + other.numerator

        new_rational = Rational(new_numerator, new_denominator)
        return new_rational


    """
    Автор: Арутюнян Самвел
    Назначение: вычитание дробей
    Каноническое название: SUB_QQ_Q
    """
    def __sub__(self, other):
        new_rational = self + (-other)
        return new_rational


    """
    Автор: Арутюнян Самвел
    Назначение: деление дробей
    Каноническое название: MUL_QQ_Q
    """
    def __mult__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        new_rational = Rational(new_numerator, new_denominator)
        return new_rational

    
    def __neg__(self):
        return Rational(self.numerator.MUL_ZM_Z(), self.denominator)

    
    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)
