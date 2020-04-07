class Natural:

    def __init__(self, num):
        self.number = [int(i) for i in num]
        self.pos = len(self.num) - 1

    def __str__(self):
        return ''.join(map(str, self.num))

    """
    Автор: Мышкин Илья
    Назначение: сравнение натуральных
    """
    def COM_NN_D(self, oth):
        if self.pos > oth.pos:
            return 2
        elif self.pos < oth.pos:
            return 1
        else:
            for i in range(self.pos + 1):
                if self.num[i] > oth.num[i]:
                    return 2
                elif self.num[i] < oth.num[i]:
                    return 1
            return 0

    """
    Автор: Мышкин Илья
    Назначение: проверка на ноль
    """
    def NZER_N_B(self):
        if self.pos == 0 and self.num[0] == 0:
            return 0
        else:
            return 1

    """
    Автор: Мышкин Илья
    Назначение: добавление 1 к натуральному
    """
    def ADD_1N_N(self):
        self.num = self.num[::-1]  # если последвательность цифр уже перевернута, то удалить
        i = 0
        while self.num[i] + 1 > 9:
            if i + 1 > self.pos:
                self.num.append(0)
                self.pos += 1
            self.num[i] = 0
            i += 1
        self.num[i] += 1
        self.num = self.num[::-1]  # если последвательность цифр уже перевернута, то удалить

    """
    Автор: Мышкин Илья
    Назначение: сложение натуральных
    Каноническое название: ADD_NN_N
    """
    def __add__(self, other):
        self.num = self.num[::-1]  # если последвательность цифр уже перевернута, то удалить
        other.num = other.num[::-1]  # если последвательность цифр уже перевернута, то удалить
        res = Natural(self.num)

        if res.pos < other.pos:
            for i in range(other.pos - res.pos):
                res.num.append(0)
            res.pos = other.pos
        temp = 0

        for i in range(other.pos + 1):
            res.num[i] = res.num[i] + other.num[i] + temp
            if res.num[i] > 9:
                temp = 1
            else:
                temp = 0
            res.num[i] = res.num[i] % 10

        if res.pos == other.pos and temp == 1:
            res.num.append(0)
            res.pos += 1

        if res.pos > other.pos and temp == 1:
            j = other.pos + 1
            while res.num[j] + 1 > 9:
                if j + 1 > res.pos:
                    res.num.append(0)
                    res.pos += 1
                res.num[j] = 0
                j += 1
            res.num[j] += 1

        self.num = self.num[::-1]  # если последвательность цифр уже перевернута, то удалить
        other.num = other.num[::-1]  # если последвательность цифр уже перевернута, то
        res.num = res.num[::-1]
        return res

    """
    Автор: Пармузин Вадим
    Назначение: вычитание из большего натурального меньшего или равного
    Каноническое название: SUB_NN_N
    """
    def __sub__(self, oth):
        if self.COM_NN_D(oth) == 0:
            return Natural('0')
        elif self.COM_NN_D(oth) == 2:
            a = Natural(self.num)
            b = Natural(oth.num)
        else:
            b = Natural(self.num)
            a = Natural(oth.num)
        dif = a.pos - b.pos
        for i in range(b.pos, -1, -1):
            if a.num[i + dif] < b.num[i]:
                j = 1
                while a.num[i - j + dif] == 0:
                    a.num[i - j + dif] = 9
                    j += 1
                a.num[i - j + dif] -= 1
                a.num[i + dif] = a.num[i + dif] + 10 - b.num[i]
            else:
                a.num[i + dif] -= b.num[i]
        i = 0
        while a.num[i] == 0:
            del a.num[i]
            a.pos -= 1
        return a

    """
    Автор: Пармузин Вадим
    Назначение: умножение натурального на цифру
    """
    def MUL_ND_N(self, k):
        res = Natural(self.num)
        over = 0
        for i in range(self.pos, -1, -1):
            res.num[i] = res.num[i] * k + over
            q = 0
            while res.num[i] - q * 10 >= 0:
                q += 1
            over = q - 1
            res.num[i] = res.num[i] - 10 * over
        if over:
            res.num = [int(i) for i in str(over)] + res.num
            res.pos += len(str(over))
        return res

    """
    Автор: Пармузин Вадим
    Назначение: умножение натурального на 10^k
    """
    def MUL_Nk_N(self, numeric):
        return Natural(self.num + list('0' * numeric))

    """
    Автор: Пармузин Вадим
    Назначение: умножение натуральных
    Каноническое название: MUL_NN_N
    """
    def __mul__(self, oth):
        res = Natural('0')
        for i in range(oth.pos, -1, -1):
            res += (self.MUL_ND_N(oth.num[i])).MUL_Nk_N(oth.pos - i)
        return res

    """
    Автор: Медведев Олег
    Назначение: вычитание из натурального другого натурального, умноженного на цифру
    """
    def SUB_NDN_N(self, oth, k):
        # temp - результат сравнения натуральных чисел
        temp = self.COM_NN_D(oth.MUL_ND_N(k))
        # Если сравниваемые числа равны, нет смысла
        # в дальнейших вычислениях. Сразу возвращаем 0
        if temp == 0:
            return Natural('0')
        else:
            return self - oth.MUL_ND_N(k)

    """
    Автор: Медведев Олег
    Назначение: вычисление первой цифры деления, домноженное на 10^k, где k - номер позиции этой цифры
    """
    def DIV_NN_Dk(self, oth):
        # temp - натуральное число, состоящее из старших
        # разрядов делимого, количество которых
        # соответсвует разрядности делителя
        temp = Natural(self.num[:oth.pos + 1])
        # res - первая цифра деления
        res = 0
        flag = 0
        # Если temp меньше делителя, то добавляем
        # очередной разряд делимого
        if temp.COM_NN_D(oth) == 1:
            temp.num.append(self.num[oth.pos + 1])
            temp.pos += 1
            flag = 1
        # Вычитаем из temp делитель и увеличиваем res
        # до тех пор, пока temp больше делителя
        while temp.COM_NN_D(oth) != 1:
            # dif - рзность между разрядностью temp и делителя
            dif = temp.pos - oth.pos
            # Нахождение разности соответсвующих
            # разрядов temp и делителя, начиная с младшего разряда
            for i in range(oth.pos, -1, -1):
                # Если разряд temp меньше разряда делителя,
                # то занимаем 1 из следующего разряда temp
                if temp.num[i + dif] < oth.num[i]:
                    temp.num[i + dif] = 10 + temp.num[i + dif] - oth.num[i]
                    temp.num[i + dif - 1] -= 1
                else:
                    temp.num[i + dif] -= oth.num[i]
            # Если при вычитании старший разряд temp стал равен 0,
            # то удаляем его из списка
            if temp.num[0] == 0 and temp.pos:
                del temp.num[0]
                temp.pos -= 1
            res += 1
        # Номер позиции первой цифры деления, k, равен
        # k = self.pos - oth.pos - flag)
        return Natural(str(res)).MUL_Nk_N(self.pos - oth.pos - flag)

    """
    Автор: Медведев Олег
    Назначение: нахождение частного от деления
    Каноничное название: DIV_NN_N
    """
    def __floordiv__(self, oth):
        # temp_1 - остаток
        temp_1 = Natural(self.num)
        # res - частное
        res = Natural('0')
        # Осуществляем процесс деления столбиком,
        # пока остаток больше делителя
        while temp_1.COM_NN_D(oth) != 1:
            # temp_2 - очередная цифра частного,
            # домноженная на 10^k, где k - номер позиции этой цифры
            temp_2 = temp_1.DIV_NN_Dk(oth)
            res += temp_2
            # Так как модуль SUB_NDN_N подразумевает, что
            # второе натуральное число будет умножено на цифру,
            # то все нули из temp 2 переносим в делитель
            temp_1 = temp_1.SUB_NDN_N(Natural(oth.num + temp_2.num[1:]), temp_2.num[0])
        return Natural(str(res))

    """
    Автор: Медведев Олег
    Назначение: нахождение остатка от деления
    Каноничное название: MOD_NN_N
    """
    def __mod__(self, oth):
        # res - отстаток
        res = Natural(self.num)
        # Осуществляем процесс деления столбиком,
        # пока остаток больше делителя
        while res.COM_NN_D(oth) != 1:
            # temp - очередная цифра частного,
            # домноженная на 10^k, где k - номер позиции этой цифры
            temp = res.DIV_NN_Dk(oth)
            # Так как модуль SUB_NDN_N подразумевает, что
            # второе натуральное число будет умножено на цифру,
            # то все нули из temp 2 переносим в делитель
            res = res.SUB_NDN_N(Natural(oth.num + temp.num[1:]), temp.num[0])
        return res

    """
    Автор: Багиев Арслан
    Назначение: НОД двух чисел
    """
    def GCF_NN_N(self, oth):
        res = Natural(self.num)
        temp = Natural(oth.num)
        while temp.NZER_N_B():
            res, temp = temp, res % temp
        return res

    """
    Автор: Багиев Арслан
    Назначение: НОК двух чисел
    """
    def LCM_NN_N(self, oth):
        return self * oth // self.GCF_NN_N(oth)
