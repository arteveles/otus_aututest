class A:
    VAR = "A"
    VAR2 = "A2"

    def method(self):
        print(self.VAR + self.VAR2)


""" Класс Б наследуется от класса А, 
    VAR - переопределяется объект класса"""


class B(A):
    VAR = "B"

    def method(self):
        print(self.VAR + self.VAR2)


class C(B, A):
    pass


class D(C):
    pass


"""Выясним из какого класса-предка вызываеются методы. Запишем в tuple"""
print(D.__mro__)

"""Выясним из какого класса-предка вызываеются методы. Запишем в list"""
print(D.mro())
