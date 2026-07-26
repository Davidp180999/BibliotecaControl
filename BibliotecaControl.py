from collections import deque
from traceback import print_exc
class Persona:
    def __init__(self, dpi, nombre_com, edad, sexo, telefono):
        self.__dpi = dpi
        self.__nombre = nombre_com
        self.__edad = edad
        self.__sexo = sexo
        self.__telefono = telefono

    def get_dpi(self):
        return self.__dpi
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_sexo(self):
        return self.__sexo
    def get_telefono(self):
        return self.__telefono

    def set_dpi(self, dpi):
        if len(dpi) == 13:
            self.__dpi = dpi
        else:
            print("Dpi invalida")
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_edad(self, edad):
        if edad > 0 and edad < 100:
            self.__edad = edad
        else:
            print("Edad invalida")
    def set_sexo(self, sexo):
        self.__sexo = sexo
    def set_telefono(self, telefono):
        if len(telefono) == 8:
            self.__telefono = telefono
        else:
            print("Telefono invalido")

    def mostrar_informacion(self):
        print("DPI:", self.__dpi)
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("Sexo:", self.__sexo)
        print("Teléfono:", self.__telefono)

class Bibliotecario(Persona):

    def __init__(self, dpi, nombre, edad, sexo, telefono,
                 codigo, puesto, usuario, contrasena):
        super().__init__(dpi, nombre, edad, sexo, telefono)

        self.__codigo = codigo
        self.__puesto = puesto
        self.__usuario = usuario
        self.__contrasena = contrasena

    def get_codigo(self):
        return self.__codigo

    def get_puesto(self):
        return self.__puesto

    def get_usuario(self):
        return self.__usuario

    def get_contrasena(self):
        return self.__contrasena

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_puesto(self, puesto):
        self.__puesto = puesto

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena


    def mostrar_informacion(self):
        print("----- DATOS DEL BIBLIOTECARIO -----")
        print("DPI:", self.get_dpi())
        print("Nombre:", self.get_nombre())
        print("Edad:", self.get_edad())
        print("Sexo:", self.get_sexo())
        print("Teléfono:", self.get_telefono())
        print("Código:", self.__codigo)
        print("Puesto:", self.__puesto)
        print("Usuario:", self.__usuario)

class Usuario(Persona):
    def __init__(self, dpi, nombre_com, edad, sexo, telefono, carrera,
                 cod_usuario, usuario, contrasena):
        super().__init__(dpi, nombre_com, edad, sexo, telefono)

        self.__cod_usuario = cod_usuario
        self.__carrera = carrera
        self.__usuario = usuario
        self.__contrasena = contrasena

    def get_cod_usuario(self):
            return self.__cod_usuario
    def get_carrera(self):
            return self.__carrera
    def get_usuario(self):
        return self.__usuario
    def get_contrasena(self):
        return self.__contrasena

    def set_cod_usuario(self, cod_usuario):
        self.__cod_usuario = cod_usuario
    def set_carrera(self, carrera):
        self.__carrera = carrera
    def set_usuario(self, usuario):
        self.__usuario = usuario
    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Carrera:", self.__carrera)
        print("Codigo de Usuario:", self.__cod_usuario)
        print("Usuario: ", self.__usuario)



usuarioadmin = "Juan"
adminconta = "1234"

lista_bibliotecarios = []
lista_usuarios = []

def login(rol):
    if rol == 1 :


        admin = input("Ingrese su Usuario: ")
        contrasena = input("Ingrese su contrasena: ")

        if (usuarioadmin == admin) and (adminconta == contrasena):
            MenuAdmin()
            return
        else:
            print("Credenciales incorrectas.")
    elif rol == 2 :

        bibliotecario = input("Ingrese su Usuario: ")
        contrasenabiblio = input("Ingrese su contrasena: ")

        encontrado = False
        for biblio in lista_bibliotecarios:

            if (biblio.get_usuario() == bibliotecario and
                    biblio.get_contrasena() == contrasenabiblio):
                encontrado = True
                MenuBiblioteca()
                return
        if not encontrado:
            print("Credenciales incorrectas.")

    elif rol == 3 :
        usuario_input = input("Ingrese su Usuario: ")
        usucontra_input = input("Ingrese su contrasena: ")

        encontrado = False
        for uso in lista_usuarios:
            if (uso.get_usuario() ==  usuario_input and
                    uso.get_contrasena() == usucontra_input):
                encontrado = True
                MenuUsu()
                return
        if not encontrado:
            print("Credenciales incorrectas.")



def MenuAdmin():
    while True:
        print("\n -------- Biblioteca --------")
        print("1. Registrar Bibliotecario")
        print("2. Registrar Usuario")
        print("3. Registrar Libro")
        print("4. Consultar libros disponibles")
        print("5. Solicitar un Préstamo")
        print("6. Atender préstamos en el orden de llegada (cola)")
        print("7. Registrar la devolución de un libro.")
        print("8. Revisar los libros devueltos pendientes (pila).")
        print("9. Buscar usuarios o libros.")
        print("10. Mostrar reportes.")
        print("11. salir.")
        try:
            opcion = int(input("Ingrese su opcion: "))
        except ValueError:
            print("\nError de entrda: Debe ingresar únicamente el número correspondiente a la opción elegida del 1 al 11. \n")
            continue

        match opcion:
            case 1:

                break
            case 2:
                break
            case 3:
                break
            case 4:
                break
            case 5:
                break
            case 8:
                break
            case 9:
                break
            case 10:

                break
            case 11:
                print("Hasta Pronto")
                break
            case _:

                print("Opción no válida.")
def MenuBiblioteca():
    while True:
        print("\n -------- Biblioteca --------")
        print("1. Registrar Usuario")
        print("2. Registrar Libro")
        print("3. Consultar libros disponibles")
        print("4. Solicitar un Préstamo")
        print("5. Atender préstamos en el orden de llegada (cola)")
        print("6. Registrar la devolución de un libro.")
        print("7. Revisar los libros devueltos pendientes (pila).")
        print("8. Buscar usuarios o libros.")
        print("9. Mostrar reportes.")
        print("10. salir.")
        try:
            opcion = int(input("Ingrese su opcion: "))
        except ValueError:
            print("\n Error de entrada: Debe ingresar únicamente el número correspondiente a la opción elegida del 1 al 10.")
            continue

        match opcion:
            case 1:

                break
            case 2:
                break
            case 3:
                break
            case 4:
                break
            case 5:
                break
            case 8:
                break
            case 9:
                break
            case 10:
                print("Hasta Pronto")
                break
            case _:
                print("Opción no válida.")

def MenuUsu():
    while True:
        print("\n -------- Biblioteca --------")
        print("1. Consultar Libros disponible")
        print("2. Solicitar un libro")
        print("3. Consultar Mis Préstamos")
        print("4. Salir")
        try:
            opcion = int(input("Ingrese su opcion: "))
        except ValueError:
            print("\n Error de entrada: Debe ingresar únicamente el número correspondiente a la opción elegida del 1 al 4")
            continue

        match opcion:
            case 1:
                break
            case 2:
                break
            case 3:
                break
            case 4:
                print("Hasta Pronto")
                break
            case _:
                print("Opcion Invalidad")
while True:
        print("\n -------- Biblioteca Los Altos --------")
        print("1. Administrador")
        print("2. Bibliotecario")
        print("3. Usuario")
        print("4. Salir")
        try:
            opcion = int(input("Ingrese su opcion: "))
        except ValueError:
            print("\n Error de entrada: Debe ingresar únicamente el número correspondiente a la opción elegida (1, 2, 3 o 4). \n")
            continue

        match opcion:
            case 1:
                login(1)
            case 2:
                login(2)
            case 3:
                login(3)
            case 4:
                print("Hasta Pronto")
                break
            case _:
                print("\n Opción no válida. Elija un número del 1 al 4. \n")

