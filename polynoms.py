class Polynom:
    def __init__(self, coefs_dict={}):
        self.coefs_dict = coefs_dict
    """
    Автор: Артем
    Назначение: умножение многочлена на x^k
    Каноническое название: MUL_Pxk_P
    """
    def MUL_Pxk_P(polynom1, num):
    polynom2=dict()
    for key in polynom1:
        polynom2[key]=ADD_QQ_Q(polynom1[key], num)
    return polynom2

    """
    Автор: Артем
    Назначение: умножение многочлена на рациональное число
    Каноническое название: MUL_PQ_P
    """
    def MUL_PQ_P(polynom1, num):
    polynom2=dict()
    for key in polynom1:
        polynom2[key]=MULL_QQ_Q(polynom1[key], num)
    return polynom2

    """
    Автор: Артем
    Назначение: сложение многочленов
    Каноническое название: ADD_PP_P
    """
    def __add__(polynom1, polynom2):
        polynom3=dict()
        if len(polynom1)>len(polynom2):
            for key in polynom1:
                polynom3[key]=polynom1[key]
                if key in polynom2:
                    polynom3[key]=ADD_QQ_Q(polynom3[key],polynom2[key])
        else:
            for key in polynom2:
                polynom3[key]=polynom2[key]
                if key in polynom1:
                    polynom3[key]=ADD_QQ_Q(polynom3[key],polynom1[key])
        return polynom3

    """
    Автор: Артем
    Назначение: вычитание многочленов
    Каноническое название: SUB_PP_P
    """
    def __sub__(polynom1, polynom2):
        polynom3=dict()
        if len(polynom1)>len(polynom2):
            for key in polynom1:
                polynom3[key]=polynom1[key]
                if key in polynom2:
                    polynom3[key]=SUB_QQ_Q(polynom3[key],polynom2[key])
        else:
            for key in polynom2:
                polynom3[key]=polynom2[key]
                if key in polynom1:
                    polynom3[key]=SUB_QQ_Q(polynom3[key],polynom1[key])
        return polynom3

    """
    Автор: 
    Назначение: умножение многочленов
    Каноническое название: MUL_PP_P
    """
    def __mul__(self, other):
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
