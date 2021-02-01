# Principal
from modulos3 import *


def principal():
    v = []
    fd = "vector.dat"
    op = -1
    carga = False
    carga_2 = False
    while op != 9:
        op = menu()
        if op == 1:
            n = validar_pos(0)
            v = carga_vector(v,n)
            carga = True
            input("Vector Generado! Presiona cualquier tecla para continuar!")
            sep()
        elif op == 2:
            if len(v) != 0:
                v = ordenamientodirecto(v)
                mostrar(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 3:
            if len(v) != 0:
                punto3(v)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 4:
            if len(v) != 0:
                id = int(input("Ingrese id a buscar: "))
                res = busqueda_secuencial(v,id)
                if res != -1:
                    print("Id encontrado con exito!")
                    to_string(v[res])
                else:
                    print("El id ingresado no se ha encontrado")
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 5:
            if len(v) != 0:
                conteo = count(v)
                mostrar_matriz(v, conteo)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
        elif op == 6:
            if len(v) != 0:
                factura = generar_automaticamente2(v, conteo)
                crear_archivo(factura,fd)
                carga_2 = True
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
            sep()
        elif op == 7:
            if len(v) != 0:
                mostrar_archivo(fd)
                sep()
            else:
                print("Debe cargar los datos primero(opcion1)")
                sep()
            sep()
        elif op == 8:
            cadena = input("Ingrese cadena: ")
            extra(cadena)
            sep()
        elif op == 9:
            print("Gracias por utilizar el programa!")
            sep()


if __name__ == '__main__':
    principal()