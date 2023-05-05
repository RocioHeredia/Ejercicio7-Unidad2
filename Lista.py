from ClassViajeros import ViajeroFrecuente
import csv


class Lista:

    def __init__(self):
        self.__lista = []

    def leer_arch(self):
        archivo = open("Viajeros.csv")
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            vf = fila
            viajero = ViajeroFrecuente(vf[0], vf[1], vf[2], vf[3], vf[4])
            self.__lista.append(viajero)
        archivo.close()
        return self.__lista

    def buscaviajero(self, num):
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].getnum() == num:
                return i

            i += 1

    def mostrar(self, pos):
        print(self.__lista[pos].gettodo())

    def almacenMemoria(self):
        print("Representacion del almacenamiento en memoria para la lista cargada con 4 viajeros.")
        for i in range(4):
            viajero = self.__lista[i]
            print(viajero.gettodo())

    def determinar_viajeros_con_mas_millas(self):
        mayor_millas = max(self.__lista)
        millas_acum_mayor = []
        for viajero in self.__lista:
            if viajero.get_millas() == mayor_millas.get_millas():
                millas_acum_mayor.append(viajero)
        print('Viajeros con mayor cantidad de millas acumuladas: ')
        for viajero in millas_acum_mayor:
            print(f"Nombre: {viajero.get_nom()}")

    def crear_instancia_con_sobrecarga_sumador(self):
        print('Acumular Millas')
        for viajero in self.__lista:
            viajero = viajero + 100
            print(f'Nombre: {viajero.get_nom()}\n Millas: {viajero.get_millas()}')

    def crear_instancia_con_sobrecarga_resta(self):
        print('\n Canjear Millas')
        for viajero in self.__lista:
            viajero = viajero - 100
            print(f'Nombre: {viajero.get_nom()}\n Millas:{viajero.get_millas()}')

    def comparacion_Cant_Millas(self):
        print('Comparacion con sobrecarga')
        for viajero in self.__lista:
            if 100 == viajero or viajero == 100:
                print(f"Nombre: {viajero.get_nom()}\nMillas: {viajero.get_millas()}")

    def sumador_por_derecha(self):
        print('\n Acumular Millas por derecha ')
        for viajero in self.__lista:
            viajero = 100 + viajero
            print(f'Nombre: {viajero.get_nom()}\n Millas: {viajero.get_millas()}')

    def resta_por_derecha(self):
        print('\n Canjear Millas por derecha')
        for viajero in self.__lista:
            viajero = 100 - viajero
            print(f'Nombre: {viajero.get_nom()}\n Milla: {viajero.get_millas()}')