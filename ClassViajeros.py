class ViajeroFrecuente:

    def __init__(self, num=0, dni='', nom='', ape='', milla=0):
        self.__num_viajero = int(num)
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ape
        self.__millas_acum = int(milla)

    def get_millas(self):
        return self.__millas_acum

    def acumularMillas(self, milla_re):
        self.__millas_acum += milla_re

    def canjearMillas(self, can):
        if self.__millas_acum >= can:
            self.__millas_acum -= can
        else:
            print('Error en la operación')

        return self.__millas_acum

    def getnum(self):
        return self.__num_viajero

    def gettodo(self):
        return self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum

    def get_nom(self):
        return self.__nombre

    def __gt__(self, viajero):
        return self.__millas_acum > viajero.__millas_acum

    def __add__(self, milla_Nueva):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido,
                                self.__millas_acum + milla_Nueva)

    def __sub__(self, millas):
        if self.__millas_acum > millas:
            return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido,
                                    self.__millas_acum - millas)
        else:
            print('Error en la opercion')

    def __eq__(self, milla):
        return self.get_millas() == milla

    def __radd__(self, mi):
        self.acumularMillas(mi)
        return self

    def __rsub__(self, mill):
        self.canjearMillas(mill)
        return self