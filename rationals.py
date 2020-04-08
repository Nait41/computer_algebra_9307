from whole import Whole, TRANS_N_Z

class Rational:
    def __init__(self, numerator, denominator=Whole("1")):
        self.numerator = numerator
        self.denominator = denominator
    
    """
    Автор: Торопов Валентин
    Назначение: сокращение дроби
    """
    def RED_Q_Q(self):
        temp_numerator = self.numerator.ABS_Z_N()
        temp_denominator = self.denominator.ABS_Z_N()

        gcd = temp_numerator.GCF_NN_N(temp_denominator)

        temp_numerator //= gcd
        temp_denominator //= gcd
        new_rational = Rational(temp_numerator, temp_denominator)

        return new_rational


    """
    Автор: Торопов Валентин
    Назначение: проверка на целое
    """
    def INT_Q_B(self):
        return 1 if self.denominator == Whole("1") else 0


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
    Назначение: умножение дробей
    Каноническое название: MUL_QQ_Q
    """
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        new_rational = Rational(new_numerator, new_denominator)
        return new_rational

    
    """
    Автор: 
    Назначение: деление дробей
    Каноническое название: DIV_QQ_Q
    """
    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        new_rational = Rational(new_numerator, new_denominator)

        return new_rational

    """
    Автор: Арутюнян Самвел
    Назначение: деление дробей
    Каноническое название: DIV_QQ_Q
    """
    def __floordiv__(self, other):
        return self / other

    
    def __neg__(self):
        return Rational(self.numerator.MUL_ZM_Z(), self.denominator)

    
    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)


"""
Автор: Торопов Валентин
Назначение: преобразование из целого в дробное
"""
def TRANS_Z_Q(whole_number):
    new_rational = Rational(whole_number, Whole("1"))
    return new_rational


"""
Автор: Арутюнян Самвел
Назначение: преобразование из дробного в целое
"""
def TRANS_Q_Z(rational_number):
    # ПРОВЕРЯТЬ, РАВЕН ЛИ ЗНАМЕНАТЕЛЬ 1 ПЕРЕД ВЫЗОВОМ
    return rational_number.numerator
