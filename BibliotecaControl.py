from collections import deque
from traceback import print_exc
class Persona:

    def __init__(self, dpi, nombre, edad, sexo, telefono):
        self.__dpi = ""
        self.__nombre = ""
        self.__edad = 0
        self.__sexo = ""
        self.__telefono = ""

        self.set_dpi(dpi)
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_sexo(sexo)
        self.set_telefono(telefono)


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

        if dpi.isdigit() and len(dpi) == 13:
            self.__dpi = dpi
            return True

        else:
            print("Error: El DPI debe contener exactamente 13 números.")
            return False

    def set_nombre(self, nombre):

        if nombre.strip() != "":
            self.__nombre = nombre.title()
            return True
        else:
            print("Error: El nombre no puede estar vacío.")
            return False

    def set_edad(self, edad):
            if 0 < edad <= 100:
                self.__edad = edad
                return True
            else:
                print("Error: Edad inválida.")
                return False

    def set_sexo(self, sexo):
        sexo = sexo.upper()

        if sexo in ["M", "F"]:
            self.__sexo = sexo
            return True
        else:
            print("Error: El sexo debe ser M o F.")
            return False

    def set_telefono(self, telefono):

        if telefono.isdigit() and len(telefono) == 8:
            self.__telefono = telefono
            return True
        else:
            print("Error: El teléfono debe contener 8 números.")
            return False

    def mostrar_informacion(self):

        print("\n----- DATOS PERSONALES -----")
        print("DPI:", self.__dpi)
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("Sexo:", self.__sexo)
        print("Teléfono:", self.__telefono)

class Bibliotecario(Persona):

    def __init__(self, dpi, nombre, edad, sexo, telefono,
                 codigo, puesto, usuario, contrasena):

        super().__init__(dpi, nombre, edad, sexo, telefono)

        self.__codigo = ""
        self.__puesto = ""
        self.__usuario = ""
        self.__contrasena = ""

        self.set_codigo(codigo)
        self.set_puesto(puesto)
        self.set_usuario(usuario)
        self.set_contrasena(contrasena)

    def get_codigo(self):
        return self.__codigo

    def get_puesto(self):
        return self.__puesto

    def get_usuario(self):
        return self.__usuario

    def get_contrasena(self):
        return self.__contrasena



    def set_codigo(self, codigo):

        if codigo.strip() != "":
            self.__codigo = codigo
            return True
        else:
            print("Error: El código no puede estar vacío.")
            return False

    def set_puesto(self, puesto):

        if puesto.strip() != "":
            self.__puesto = puesto.title()
            return True
        else:
            print("Error: El puesto no puede estar vacío.")
            return False

    def set_usuario(self, usuario):

        if usuario.strip() != "":
            self.__usuario = usuario
            return True
        else:
            print("Error: El usuario no puede estar vacío.")
            return False

    def set_contrasena(self, contrasena):

        if len(contrasena) >= 4:
            self.__contrasena = contrasena
            return True
        else:
            print("Error: La contraseña debe tener al menos 4 caracteres.")
            return False


    def mostrar_informacion(self):

        print("\n===== DATOS DEL BIBLIOTECARIO =====")
        super().mostrar_informacion()
        print("Código:", self.__codigo)
        print("Puesto:", self.__puesto)
        print("Usuario:", self.__usuario)

class Usuario(Persona):
    def __init__(self, dpi, nombre_com, edad, sexo, telefono, carrera,
                 cod_usuario, usuario, contrasena):
        super().__init__(dpi, nombre_com, edad, sexo, telefono)

        self.__carrera = ""
        self.__cod_usuario = ""
        self.__usuario = ""
        self.__contrasena = ""


        self.set_carrera(carrera)
        self.set_cod_usuario(cod_usuario)
        self.set_usuario(usuario)
        self.set_contrasena(contrasena)


    def get_cod_usuario(self):
        return self.__cod_usuario

    def get_carrera(self):
        return self.__carrera

    def get_usuario(self):
        return self.__usuario

    def get_contrasena(self):
        return self.__contrasena


    def set_cod_usuario(self, cod_usuario):
        if cod_usuario.strip() != "":
            self.__cod_usuario = cod_usuario
            return True
        else:
            print("Error: El código de usuario no puede estar vacío.")
            return False

    def set_carrera(self, carrera):
        if carrera.strip() != "":
            self.__carrera = carrera.title()
            return True
        else:
            print("Error: La carrera no puede estar vacía.")
            return False

    def set_usuario(self, usuario):
        if usuario.strip() != "":
            self.__usuario = usuario
            return True
        else:
            print("Error: El usuario no puede estar vacío.")
            return False

    def set_contrasena(self, contrasena):
        if len(contrasena) >= 4:
            self.__contrasena = contrasena
            return True
        else:
            print("Error: La contraseña debe tener al menos 4 caracteres.")
            return False

    def mostrar_informacion(self):
        print("\n===== DATOS DEL USUARIO =====")
        super().mostrar_informacion()
        print("Carrera:", self.__carrera)
        print("Código de Usuario:", self.__cod_usuario)
        print("Usuario:", self.__usuario)
#nil = numero intermo del libro
class Libro:
    def __init__(self, nil, titulo, autor, categoria, copias):
        self.__nil = ""
        self.__titulo = ""
        self.__autor = ""
        self.__categoria = ""
        self.__copias = 0

        self.set_nil(nil)
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_categoria(categoria)
        self.set_copias(copias)

    def get_nil(self):
        return self.__nil

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_categoria(self):
        return self.__categoria

    def get_copias(self):
        return self.__copias

    def set_nil(self, nil):
        if nil.strip() != "":
            self.__nil = nil.strip()
            return True
        print("Error: El ISBN/Código no puede estar vacío.")
        return False

    def set_titulo(self, titulo):
        if titulo.strip() != "":
            self.__titulo = titulo.strip().title()
            return True
        print("Error: El título no puede estar vacío.")
        return False

    def set_autor(self, autor):
        if autor.strip() != "":
            self.__autor = autor.strip().title()
            return True
        print("Error: El autor no puede estar vacío.")
        return False

    def set_categoria(self, categoria):
        if categoria.strip() != "":
            self.__categoria = categoria.strip().title()
            return True
        print("Error: La categoría no puede estar vacía.")
        return False

    def set_copias(self, copias):
        if isinstance(copias, int) and copias > 0:
            self.__copias = copias
            return True
        print("Error: La cantidad de copias debe ser un número entero mayor a 0.")
        return False

    def mostrar_informacion(self):
        print("\n===== DATOS DEL LIBRO =====")
        print("ISBN/Código:", self.__nil)
        print("Título:", self.__titulo)
        print("Autor:", self.__autor)
        print("Categoría:", self.__categoria)
        print("Copias Disponibles:", self.__copias)

usuarioadmin = "Juan"
adminconta = "1234"

lista_bibliotecarios = []
lista_usuarios = []
lista_libros = []

def login(rol):
    if rol == 1 :

        admin = input("Ingrese su Usuario: ")
        contrasena = input("Ingrese su contrasena: ")

        if (usuarioadmin == admin) and (adminconta == contrasena):
            print("\n¡Bienvenido Administrador!")
            MenuAdmin()
            return
        else:
            print("Credenciales incorrectas.")
    elif rol == 2 :
        if not lista_bibliotecarios:
            print(
                "\nError: No hay bibliotecarios registrados en el sistema. Inicie como Administrador para registrar uno.")
            return

        bibliotecario = input("Ingrese su Usuario: ")
        contrasenabiblio = input("Ingrese su contrasena: ")

        encontrado = False
        for biblio in lista_bibliotecarios:

            if (biblio.get_usuario() == bibliotecario and
                    biblio.get_contrasena() == contrasenabiblio):
                    encontrado = True
                    print(f"\n¡Bienvenido/a {biblio.get_nombre()}!")
                    MenuBiblioteca(biblio)
                    return

        if not encontrado:
            print("Credenciales incorrectas.")

    elif rol == 3 :
        if not lista_usuarios:
            print("\nError: No hay usuarios registrados en el sistema. Debe registrarse primero.")
            return
        usuario_input = input("Ingrese su Usuario: ")
        usucontra_input = input("Ingrese su contrasena: ")

        encontrado = False
        for usu in lista_usuarios:
            if (usu.get_usuario() ==  usuario_input and
                    usu.get_contrasena() == usucontra_input):
                encontrado = True
                print(f"\n¡Bienvenido/a {usu.get_nombre()}!")
                MenuUsu(usu)
                return
        if not encontrado:
            print("Credenciales incorrectas.")

def registrar_bibliotecario():
    print("\n===== REGISTRO DE BIBLIOTECARIO =====")

    # 1. Validar DPI (exactamente 13 dígitos)
    while True:
        dpi = input("Ingrese DPI (13 dígitos): ").strip()
        if dpi.isdigit() and len(dpi) == 13:
            break
        print("Error: El DPI debe contener exactamente 13 números.")

    # 2. Validar Nombre
    while True:
        nombre = input("Ingrese nombre completo: ").strip()
        if nombre != "":
            break
        print("Error: El nombre no puede estar vacío.")

    # 3. Validar Edad (mayor a 0 y menor o igual a 100)
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if 0 < edad <= 100:
                break
            print("Error: Edad inválida (debe estar entre 1 y 100).")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # 4. Validar Sexo (M o F)
    while True:
        sexo = input("Ingrese sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            break
        print("Error: El sexo debe ser M o F.")

    # 5. Validar Teléfono (exactamente 8 dígitos)
    while True:
        telefono = input("Ingrese teléfono (8 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 8:
            break
        print("Error: El teléfono debe contener exactamente 8 números.")

    # 6. Validar Código (Único)
    while True:
        codigo = input("Ingrese código del bibliotecario: ").strip()
        if codigo == "":
            print("Error: El código no puede estar vacío.")
            continue

        existe = any(biblio.get_codigo() == codigo for biblio in lista_bibliotecarios)
        if existe:
            print("Error: Ese código ya existe.")
        else:
            break

    # 7. Validar Puesto
    while True:
        puesto = input("Ingrese puesto: ").strip()
        if puesto != "":
            break
        print("Error: El puesto no puede estar vacío.")

    # 8. Validar Usuario (Único)
    while True:
        usuario = input("Ingrese nombre de usuario: ").strip()
        if usuario == "":
            print("Error: El usuario no puede estar vacío.")
            continue

        existe = any(biblio.get_usuario().lower() == usuario.lower() for biblio in lista_bibliotecarios)
        if existe:
            print("Error: Ese usuario ya está registrado.")
        else:
            break

    # 9. Validar Contraseña (mínimo 4 caracteres)
    while True:
        contrasena = input("Ingrese contraseña (mínimo 4 caracteres): ")
        if len(contrasena) >= 4:
            break
        print("Error: La contraseña debe tener al menos 4 caracteres.")

    # Crear y guardar el nuevo bibliotecario
    nuevo = Bibliotecario(dpi, nombre, edad, sexo, telefono, codigo, puesto, usuario, contrasena)
    lista_bibliotecarios.append(nuevo)
    print("\n¡Bibliotecario registrado correctamente!")

def registrar_usuario():
    print("\n===== REGISTRO DE USUARIO =====")

    # 1. DPI (13 dígitos)
    while True:
        dpi = input("Ingrese DPI (13 dígitos): ").strip()
        if dpi.isdigit() and len(dpi) == 13:
            break
        print("Error: El DPI debe contener exactamente 13 números.")

    # 2. Nombre completo
    while True:
        nombre = input("Ingrese nombre completo: ").strip()
        if nombre != "":
            break
        print("Error: El nombre no puede estar vacío.")

    # 3. Edad (1 a 100)
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if 0 < edad <= 100:
                break
            print("Error: Edad inválida (debe estar entre 1 y 100).")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # 4. Sexo (M/F)
    while True:
        sexo = input("Ingrese sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            break
        print("Error: El sexo debe ser M o F.")

    # 5. Teléfono (8 dígitos)
    while True:
        telefono = input("Ingrese teléfono (8 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 8:
            break
        print("Error: El teléfono debe contener exactamente 8 números.")

    # 6. Carrera
    while True:
        carrera = input("Ingrese carrera: ").strip()
        if carrera != "":
            break
        print("Error: La carrera no puede estar vacía.")

    # 7. Código de Usuario (Único)
    while True:
        cod_usuario = input("Ingrese código de usuario: ").strip()
        if cod_usuario == "":
            print("Error: El código no puede estar vacío.")
            continue

        existe = any(uso.get_cod_usuario() == cod_usuario for uso in lista_usuarios)
        if existe:
            print("Error: Ese código de usuario ya existe.")
        else:
            break

    # 8. Nombre de Usuario (Único)
    while True:
        usuario = input("Ingrese nombre de usuario para el sistema: ").strip()
        if usuario == "":
            print("Error: El usuario no puede estar vacío.")
            continue

        existe = any(uso.get_usuario().lower() == usuario.lower() for uso in lista_usuarios)
        if existe:
            print("Error: Ese nombre de usuario ya está registrado.")
        else:
            break

    # 9. Contraseña (mínimo 4 caracteres)
    while True:
        contrasena = input("Ingrese contraseña (mínimo 4 caracteres): ")
        if len(contrasena) >= 4:
            break
        print("Error: La contraseña debe tener al menos 4 caracteres.")

    # INSTANCIACIÓN: Aquí la función llama a la clase
    nuevo_usuario = Usuario(
        dpi,
        nombre,
        edad,
        sexo,
        telefono,
        carrera,
        cod_usuario,
        usuario,
        contrasena
    )

    lista_usuarios.append(nuevo_usuario)
    print("\n¡Usuario registrado correctamente!")

def registrar_libro():
    print("\n===== REGISTRO DE LIBRO =====")

    # 1. Validar nil / Código (Único)
    while True:
        nil = input("Ingrese el ISBN o Código del libro: ")
        if nil == "":
            print("Error: El código no puede estar vacío.")
            continue

        # Validar que no exista un libro con ese mismo nil
        existe = any(libro.get_nil() == nil for libro in lista_libros)
        if existe:
            print("Error: Ya existe un libro registrado con ese código/nil.")
        else:
            break

    # 2. Validar Título
    while True:
        titulo = input("Ingrese el título del libro: ")
        if titulo != "":
            break
        print("Error: El título no puede estar vacío.")

    # 3. Validar Autor
    while True:
        autor = input("Ingrese el autor del libro: ")
        if autor != "":
            break
        print("Error: El autor no puede estar vacío.")

    # 4. Validar Categoría
    while True:
        categoria = input("Ingrese la categoría/género: ")
        if categoria != "":
            break
        print("Error: La categoría no puede estar vacía.")

    # 5. Validar Cantidad de Copias
    while True:
        try:
            copias = int(input("Ingrese la cantidad de copias: "))
            if copias > 0:
                break
            print("Error: Debe ingresar al menos 1 copia.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # Instanciación e inserción a la lista
    nuevo_libro = Libro(nil, titulo, autor, categoria, copias)
    lista_libros.append(nuevo_libro)

    print(f"\n¡El libro '{nuevo_libro.get_titulo()}' fue registrado correctamente!")

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
                registrar_bibliotecario()

            case 2:
                registrar_usuario()
            case 3:
                registrar_libro()
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

def MenuBiblioteca(bibliotecario_actual):
    while True:
        print(f"\n -------- Biblioteca (Bibliotecario: {bibliotecario_actual.get_nombre()}) --------")
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
                registrar_usuario()
            case 2:
                registrar_libro()
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

def MenuUsu(usuario_actual):
    while True:
        print(f"\n -------- Biblioteca (Bienvenido: {usuario_actual.get_nombre()}) --------")
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
