class Polynom:
    def __init__(self, coefs_dict={}):
        self.coefs_dict = coefs_dict


    """
    Автор:
    Назначение: сложение многочленов
    Каноническое название: ADD_PP_P
    """
    def __add__(self, other):
        pass


    """
    Автор:
    Назначение: вычитание многочленов
    Каноническое название: SUB_PP_P
    """
    def __sub__(self, other):
        pass


    """
    Автор:
    Назначение: умножение многочленов
    Каноническое название: MUL_PP_P
    """
    def __mult__(self, other):
        pass


    """
    Автор:
    Назначение: частное от деления многочленов
    Каноническое название: DIV_PP_P
    """
    def __truediv__(self, other):
        pass

    # не меняйте пожалуйста эту функцию, сделано для равенства операций / и //
    def __floordiv__(self, other):
        return self / other

    
    """
    Автор:
    Назначение: остаток от деления многочленов
    Каноническое название: MOD_PP_P
    """
    def __mod__(self, other):
        pass
