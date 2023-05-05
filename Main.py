from Lista import Lista


def menu():
    print('Opciones')
    print('a- Consultar Cantidad de Millas.')
    print('b- Acumular Millas.')
    print('c- Canjear Millas.')
    print('d- Salir')


def FuncionOpciones(opc, lis, posi):
    while opc <= 'c':
        if lis:
            if opc == 'a':
                print('Cantidad de millas acumuladas: {}'.format(p[posi].get_millas()))

            elif opc == 'b':
                a = int(input('Ingrese millas para acumularlas con las demas: '))
                p[posi].acumularMillas(a)
                print('Millas acumuladas: {}'.format(p[posi].get_millas()))
            elif opc == 'c':
                can = int(input('Ingrese millas para canjearlas con las demas: '))
                p[posi].canjearMillas(can)
                print('Millas acumuladas despues del canje: {}'.format(p[posi].get_millas()))

        opc = input('Ingrese otra opcion:')


if __name__ == '__main__':
    m = Lista()
    p = m.leer_arch()
    #while True:
     #   num = int(input('Ingrese numero del viajero:'))
      #  pos = m.buscaviajero(num)
       # if pos is not None:
        #    menu()
         #   op = input('Ingrese su opcion:')
          #  FuncionOpciones(op, p, pos)
       # else:
        #    print('Viajero no encontrado')
        #break
    #m.almacenMemoria()
    #m.determinar_viajeros_con_mas_millas()
    #m.crear_instancia_con_sobrecarga_sumador()
    #m.crear_instancia_con_sobrecarga_resta()

    m.comparacion_Cant_Millas()
    m.sumador_por_derecha()
    m.resta_por_derecha()