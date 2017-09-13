class Nota:
    def __init__(self):
        self.id = 0 #SACAR?
        self.titulo = ""
        self.texto = ""
        self.fecha = "" #SACAR?


class Block:
    def __init__(self):
        self.notas = []

    def listarNotas(self):
        import sqlite3
        from tabulate import tabulate
        with sqlite3.connect('block2.db') as base:
            cursor = base.cursor()
            cursor.execute('SELECT BLOCK2.ID, BLOCK2.TITULO, BLOCK2.FECHA FROM BLOCK2 WHERE BLOCK2.ESTADO = "ACTIVO";')
            listaDatos = list(cursor.fetchall())
            print("Listado de notas del block")
            print(tabulate(listaDatos, headers = ["ID", "Titulo", "Fecha de creacion"], tablefmt = "grid"))
            print("")

    def agregarNota(self):
        import sqlite3
        with sqlite3.connect('block2.db') as base:
            n = Nota()
            n.titulo = input("Ingrese título: ")
            n.texto = input("Ingrese texto: ")
            base.execute('''INSERT INTO BLOCK2 (TITULO, TEXTO) VALUES ("{}", "{}");'''.format(n.titulo, n.texto))
            base.commit()
            print("Nota agregada")

    def modificarNota(self):
        import sqlite3
        from tabulate import tabulate
        with sqlite3.connect('block2.db') as base:
            cursor = base.cursor()
            dato = input("Ingresar ID de la nota a modificar: ")
            cursor.execute('SELECT BLOCK2.ID, BLOCK2.TITULO, BLOCK2.TEXTO FROM BLOCK2 WHERE BLOCK2.ESTADO = "ACTIVO" AND BLOCK2.ID = ("{}");'.format(dato))
            itemAModificar = list(cursor.fetchall())
            print("nota a modificar:")
            print(tabulate(itemAModificar, headers = ["ID", "Titulo", "Fecha de creacion"], tablefmt = "grid"))
            print("")

            #FUNCIONES?!

            opcion = True
            while opcion:
                print("""      Modificar nota:
                                1 - Modificar titulo
                                2 - Modificar texto
                                3 - Volver""")
                opcion = input("Seleccionar opcion: ")
                if opcion == "1":
                    print("Titulo actual: ", itemAModificar[0][1])
                    nuevoTitulo = (input("Ingresar nombre nuevo o modificado: ")).upper()
                    cursor.execute(
                        '''UPDATE BLOCK2 SET TITULO = ("{}") WHERE ID = ("{}");'''.format(nuevoTitulo, dato))
                    base.commit()
                    input("Titulo modificado.Seguir")  # OJO CAMBIAR
                elif opcion == "2":
                    print("Texto actual: ", itemAModificar[0][2])
                    nuevoTexto = (input("Ingresar texto nuevo o modificado: ")).upper()
                    cursor.execute(
                        '''UPDATE BLOCK2 SET TEXTO = ("{}") WHERE ID = ("{}");'''.format(nuevoTexto, dato))
                    base.commit()
                    input("Texto modificado.Seguir")  # OJO CAMBIAR
                elif opcion == "3":
                        self.mostrarMenu()
                elif opcion != "":
                    print("\n Opcion invalida. Reintentar")

    def borrarNota(self):
        import sqlite3
        from tabulate import tabulate
        with sqlite3.connect('block2.db') as base:
            cursor = base.cursor()
            dato = input("Ingresar ID de la nota a borrar: ")
            cursor.execute(
                'SELECT BLOCK2.ID, BLOCK2.TITULO, BLOCK2.TEXTO FROM BLOCK2 WHERE BLOCK2.ESTADO = "ACTIVO" AND BLOCK2.ID = ("{}");'.format(dato))
            itemAModificar = list(cursor.fetchall())
            print("Nota a borrar:")
            print(tabulate(itemAModificar, headers = ["ID", "Titulo", "Fecha de creacion"], tablefmt = "grid"))
            print("")
            input("Borrar nota? (S/N)")
            input("La accion no puede deshacerse. continuar? (S/N)")
            input("Esta absolutamente seguro de que quiere borrar la nota? (S/N)")
            cursor.execute('''UPDATE BLOCK2 SET ESTADO = "INACTIVO" WHERE ID = ("{}");'''.format(dato))
            base.commit()
            input("La nota ha sido borrada. Continuar")

    def buscarNota(self):
        pass

    def salir(self):
        exit()


class Menu:
    def __init__(self):
        self.miBlock = Block()
        self.funciones = {
            "1": Block.listarNotas,
            "2": Block.agregarNota,
            "3": Block.modificarNota,
            "4": Block.borrarNota,
            "5": Block.buscarNota,
            "6": Block.salir
        }

    def mostrarMenu(self):
        while True:
            print("Ingrese opción:")
            print("""
                1. Listar notas
                2. Agregar Nota
                3. Modificar Nota
                4. Borrar Nota
                5. Buscar Nota
                6. Salir
            """)
            opc = self.ingresarOpcion()
            if opc == "1":
                self.funciones["1"]
                #Block.listarNotas(self)
            if opc == "2":
                self.funciones["2"]
                #Block.agregarNota(self)
            if opc == "3":
                self.funciones["3"]
                #Block.modificarNota(self)
            if opc == "4":
                self.funciones["4"]
                #Block.borrarNota(self)
            if opc == 6:
                self.funciones["6"]
                #Block.salir()
            else:
                funcion = self.funciones[opc]

                if funcion:
                    funcion(self)

    def ingresarOpcion(self):
        return input("ingrese opción >")

if __name__ == '__main__':
    mnu = Menu()
    mnu.mostrarMenu()