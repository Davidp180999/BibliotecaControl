from collections import deque

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
        print("Error: El NIL/Código no puede estar vacío.")
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

    def sumar_copia(self):
        self.__copias += 1

    def restar_copia(self):
        if self.__copias > 0:
            self.__copias -= 1
            return True
        return False

    def mostrar_informacion(self):
        print("\n===== DATOS DEL LIBRO =====")
        print("NIL/Código:", self.__nil)
        print("Título:", self.__titulo)
        print("Autor:", self.__autor)
        print("Categoría:", self.__categoria)
        print("Copias Disponibles:", self.__copias)


class Prestamo:
    """Representa una solicitud/movimiento de préstamo de un libro."""
    contador = 0

    def __init__(self, usuario, libro):
        Prestamo.contador += 1
        self.__id = Prestamo.contador
        self.__usuario = usuario
        self.__libro = libro
        self.__estado = "Pendiente"

    def get_id(self):
        return self.__id

    def get_usuario(self):
        return self.__usuario

    def get_libro(self):
        return self.__libro

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def mostrar_informacion(self):
        print(f"Préstamo #{self.__id} | Estado: {self.__estado}")
        print(f"  Usuario: {self.__usuario.get_nombre()} ({self.__usuario.get_cod_usuario()})")
        print(f"  Libro: {self.__libro.get_titulo()} (NIL: {self.__libro.get_nil()})")


usuarioadmin = "Juan"
adminconta = "1234"

lista_bibliotecarios = []
lista_usuarios = []
lista_libros = []


cola_solicitudes = deque()
lista_prestamos_activos = []
pila_devoluciones = []
historial_prestamos = []


def login(rol):
    if rol == 1:

        admin = input("Ingrese su Usuario: ")
        contrasena = input("Ingrese su contrasena: ")

        if (usuarioadmin == admin) and (adminconta == contrasena):
            print("\n¡Bienvenido Administrador!")
            MenuAdmin()
            return
        else:
            print("Credenciales incorrectas.")
    elif rol == 2:
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

    elif rol == 3:
        if not lista_usuarios:
            print("\nError: No hay usuarios registrados en el sistema. Debe registrarse primero.")
            return
        usuario_input = input("Ingrese su Usuario: ")
        usucontra_input = input("Ingrese su contrasena: ")

        encontrado = False
        for usu in lista_usuarios:
            if (usu.get_usuario() == usuario_input and
                    usu.get_contrasena() == usucontra_input):
                encontrado = True
                print(f"\n¡Bienvenido/a {usu.get_nombre()}!")
                MenuUsu(usu)
                return
        if not encontrado:
            print("Credenciales incorrectas.")


def registrar_bibliotecario():
    print("\n===== REGISTRO DE BIBLIOTECARIO =====")
    while True:
        dpi = input("Ingrese DPI (13 dígitos): ").strip()
        if dpi.isdigit() and len(dpi) == 13:
            break
        print("Error: El DPI debe contener exactamente 13 números.")
    while True:
        nombre = input("Ingrese nombre completo: ").strip()
        if nombre != "":
            break
        print("Error: El nombre no puede estar vacío.")
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if 0 < edad <= 100:
                break
            print("Error: Edad inválida (debe estar entre 1 y 100).")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    while True:
        sexo = input("Ingrese sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            break
        print("Error: El sexo debe ser M o F.")

    while True:
        telefono = input("Ingrese teléfono (8 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 8:
            break
        print("Error: El teléfono debe contener exactamente 8 números.")
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
    while True:
        puesto = input("Ingrese puesto: ").strip()
        if puesto != "":
            break
        print("Error: El puesto no puede estar vacío.")

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
    while True:
        contrasena = input("Ingrese contraseña (mínimo 4 caracteres): ")
        if len(contrasena) >= 4:
            break
        print("Error: La contraseña debe tener al menos 4 caracteres.")

    nuevo = Bibliotecario(dpi, nombre, edad, sexo, telefono, codigo, puesto, usuario, contrasena)
    lista_bibliotecarios.append(nuevo)
    print("\n¡Bibliotecario registrado correctamente!")


def registrar_usuario():
    print("\n===== REGISTRO DE USUARIO =====")

    while True:
        dpi = input("Ingrese DPI (13 dígitos): ").strip()
        if dpi.isdigit() and len(dpi) == 13:
            break
        print("Error: El DPI debe contener exactamente 13 números.")

    while True:
        nombre = input("Ingrese nombre completo: ").strip()
        if nombre != "":
            break
        print("Error: El nombre no puede estar vacío.")

    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if 0 < edad <= 100:
                break
            print("Error: Edad inválida (debe estar entre 1 y 100).")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    while True:
        sexo = input("Ingrese sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            break
        print("Error: El sexo debe ser M o F.")

    while True:
        telefono = input("Ingrese teléfono (8 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 8:
            break
        print("Error: El teléfono debe contener exactamente 8 números.")

    while True:
        carrera = input("Ingrese carrera: ").strip()
        if carrera != "":
            break
        print("Error: La carrera no puede estar vacía.")
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
    while True:
        contrasena = input("Ingrese contraseña (mínimo 4 caracteres): ")
        if len(contrasena) >= 4:
            break
        print("Error: La contraseña debe tener al menos 4 caracteres.")

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

    while True:
        nil = input("Ingrese el NIL o Código del libro: ")
        if nil == "":
            print("Error: El código no puede estar vacío.")
            continue
        existe = any(libro.get_nil() == nil for libro in lista_libros)
        if existe:
            print("Error: Ya existe un libro registrado con ese código/nil.")
        else:
            break

    while True:
        titulo = input("Ingrese el título del libro: ")
        if titulo != "":
            break
        print("Error: El título no puede estar vacío.")

    while True:
        autor = input("Ingrese el autor del libro: ")
        if autor != "":
            break
        print("Error: El autor no puede estar vacío.")

    while True:
        categoria = input("Ingrese la categoría/género: ")
        if categoria != "":
            break
        print("Error: La categoría no puede estar vacía.")

    while True:
        try:
            copias = int(input("Ingrese la cantidad de copias: "))
            if copias > 0:
                break
            print("Error: Debe ingresar al menos 1 copia.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    nuevo_libro = Libro(nil, titulo, autor, categoria, copias)
    lista_libros.append(nuevo_libro)

    print(f"\n¡El libro '{nuevo_libro.get_titulo()}' fue registrado correctamente!")

def consultar_libros():
    print("\n===== LIBROS DISPONIBLES =====")
    if not lista_libros:
        print("No hay libros registrados todavía.")
        return
    disponibles = [l for l in lista_libros if l.get_copias() > 0]
    if not disponibles:
        print("No hay copias disponibles de ningún libro en este momento.")
    for libro in lista_libros:
        libro.mostrar_informacion()


def _buscar_libro_por_nil(nil):
    for libro in lista_libros:
        if libro.get_nil() == nil:
            return libro
    return None


def _buscar_usuario_por_codigo(cod_usuario):
    for usu in lista_usuarios:
        if usu.get_cod_usuario() == cod_usuario:
            return usu
    return None


def solicitar_prestamo(usuario_actual=None):
    print("\n===== SOLICITAR PRÉSTAMO =====")
    if not lista_libros:
        print("No hay libros registrados en el sistema.")
        return
    if not lista_usuarios:
        print("No hay usuarios registrados en el sistema.")
        return

    consultar_libros()

    nil = input("\nIngrese el NIL/Código del libro que desea solicitar: ").strip()
    libro = _buscar_libro_por_nil(nil)
    if libro is None:
        print("Error: No existe un libro con ese código.")
        return
    if libro.get_copias() <= 0:
        print("Lo sentimos, no hay copias disponibles de ese libro por el momento.")
        return

    if usuario_actual is not None:
        usuario = usuario_actual
    else:
        cod_usuario = input("Ingrese el código del usuario que solicita el préstamo: ").strip()
        usuario = _buscar_usuario_por_codigo(cod_usuario)
        if usuario is None:
            print("Error: No existe un usuario con ese código.")
            return

    nueva_solicitud = Prestamo(usuario, libro)
    cola_solicitudes.append(nueva_solicitud)
    print(f"\n¡Solicitud registrada! Turno en cola: {len(cola_solicitudes)}. "
          f"Un bibliotecario la atenderá en el orden de llegada.")


def atender_prestamos():
    print("\n===== ATENDER PRÉSTAMOS (COLA FIFO) =====")
    if not cola_solicitudes:
        print("No hay solicitudes pendientes en la cola.")
        return

    print(f"Hay {len(cola_solicitudes)} solicitud(es) en espera.")
    while cola_solicitudes:
        siguiente = cola_solicitudes[0]
        print("\nSiguiente en la fila:")
        siguiente.mostrar_informacion()
        respuesta = input("¿Atender esta solicitud? (s = sí, n = detenerse): ").strip().lower()
        if respuesta != "s":
            print("Se detuvo la atención de la cola. Las solicitudes restantes se conservan.")
            break

        solicitud = cola_solicitudes.popleft()
        libro = solicitud.get_libro()
        if libro.get_copias() <= 0:
            print(f"No hay copias disponibles de '{libro.get_titulo()}'. Solicitud cancelada.")
            solicitud.set_estado("Cancelado (sin copias)")
            historial_prestamos.append(solicitud)
            continue

        libro.restar_copia()
        solicitud.set_estado("Activo")
        lista_prestamos_activos.append(solicitud)
        historial_prestamos.append(solicitud)
        print(f"Préstamo #{solicitud.get_id()} entregado a {solicitud.get_usuario().get_nombre()}.")

    print("\nNo quedan más solicitudes por atender." if not cola_solicitudes else "")


def registrar_devolucion(usuario_actual=None):
    print("\n===== REGISTRAR DEVOLUCIÓN =====")
    activos = lista_prestamos_activos
    if usuario_actual is not None:
        activos = [p for p in lista_prestamos_activos if p.get_usuario() is usuario_actual]

    if not activos:
        print("No hay préstamos activos para devolver.")
        return

    print("Préstamos activos:")
    for p in activos:
        p.mostrar_informacion()

    try:
        id_prestamo = int(input("\nIngrese el número de préstamo (#) a devolver: "))
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return

    prestamo = next((p for p in activos if p.get_id() == id_prestamo), None)
    if prestamo is None:
        print("Error: No se encontró ese préstamo entre los activos.")
        return

    lista_prestamos_activos.remove(prestamo)
    prestamo.set_estado("Devuelto (pendiente de revisión)")
    pila_devoluciones.append(prestamo)
    print(f"\nSe registró la devolución del libro '{prestamo.get_libro().get_titulo()}'. "
          f"Queda pendiente de revisión por el bibliotecario.")


def revisar_devoluciones_pendientes():
    print("\n===== LIBROS DEVUELTOS PENDIENTES (PILA LIFO) =====")
    if not pila_devoluciones:
        print("No hay devoluciones pendientes de revisión.")
        return

    print(f"Hay {len(pila_devoluciones)} devolución(es) pendiente(s). Se revisan de la más reciente a la más antigua.")
    while pila_devoluciones:
        ultimo = pila_devoluciones[-1]
        print("\nÚltima devolución registrada:")
        ultimo.mostrar_informacion()
        respuesta = input("¿Revisar y reincorporar esta copia al inventario? (s = sí, n = detenerse): ").strip().lower()
        if respuesta != "s":
            print("Se detuvo la revisión. Las devoluciones restantes se conservan en la pila.")
            break

        prestamo = pila_devoluciones.pop()
        prestamo.get_libro().sumar_copia()
        prestamo.set_estado("Devuelto")
        print(f"Libro '{prestamo.get_libro().get_titulo()}' revisado y disponible nuevamente.")

    if not pila_devoluciones:
        print("\nNo quedan devoluciones pendientes.")


def buscar():
    print("\n===== BUSCAR =====")
    print("1. Buscar libro")
    print("2. Buscar usuario")
    try:
        opcion = int(input("Ingrese su opción: "))
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return

    if opcion == 1:
        termino = input("Ingrese título, autor o código del libro: ").strip().lower()
        resultados = [
            l for l in lista_libros
            if termino in l.get_titulo().lower()
            or termino in l.get_autor().lower()
            or termino in l.get_nil().lower()
        ]
        if not resultados:
            print("No se encontraron libros que coincidan con la búsqueda.")
        for libro in resultados:
            libro.mostrar_informacion()

    elif opcion == 2:
        termino = input("Ingrese nombre o código de usuario: ").strip().lower()
        resultados = [
            u for u in lista_usuarios
            if termino in u.get_nombre().lower()
            or termino in u.get_cod_usuario().lower()
        ]
        if not resultados:
            print("No se encontraron usuarios que coincidan con la búsqueda.")
        for usu in resultados:
            usu.mostrar_informacion()
    else:
        print("Opción no válida.")


def mostrar_reportes():
    print("\n===== REPORTES =====")
    print(f"Total de libros distintos registrados: {len(lista_libros)}")
    total_copias = sum(l.get_copias() for l in lista_libros)
    print(f"Total de copias disponibles actualmente: {total_copias}")
    print(f"Total de usuarios registrados: {len(lista_usuarios)}")
    print(f"Total de bibliotecarios registrados: {len(lista_bibliotecarios)}")
    print(f"Solicitudes en cola (pendientes de atender): {len(cola_solicitudes)}")
    print(f"Préstamos activos actualmente: {len(lista_prestamos_activos)}")
    print(f"Devoluciones pendientes de revisión: {len(pila_devoluciones)}")
    print(f"Movimientos totales en el historial: {len(historial_prestamos)}")

    if lista_libros:
        libro_mas_prestado = max(
            lista_libros,
            key=lambda l: sum(1 for p in historial_prestamos if p.get_libro() is l),
            default=None
        )
        veces = sum(1 for p in historial_prestamos if p.get_libro() is libro_mas_prestado)
        if libro_mas_prestado and veces > 0:
            print(f"Libro más solicitado: '{libro_mas_prestado.get_titulo()}' ({veces} vez/veces)")


def mostrar_mis_prestamos(usuario_actual):
    print(f"\n===== MIS PRÉSTAMOS ({usuario_actual.get_nombre()}) =====")
    activos = [p for p in lista_prestamos_activos if p.get_usuario() is usuario_actual]
    en_cola = [p for p in cola_solicitudes if p.get_usuario() is usuario_actual]
    historial = [p for p in historial_prestamos if p.get_usuario() is usuario_actual]

    if en_cola:
        print("\n-- Solicitudes en espera --")
        for p in en_cola:
            p.mostrar_informacion()

    if activos:
        print("\n-- Préstamos activos --")
        for p in activos:
            p.mostrar_informacion()

    if historial:
        print("\n-- Historial --")
        for p in historial:
            p.mostrar_informacion()

    if not en_cola and not activos and not historial:
        print("Aún no tiene préstamos registrados.")

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
                consultar_libros()
            case 5:
                solicitar_prestamo()
            case 6:
                atender_prestamos()
            case 7:
                registrar_devolucion()
            case 8:
                revisar_devoluciones_pendientes()
            case 9:
                buscar()
            case 10:
                mostrar_reportes()
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
                consultar_libros()
            case 4:
                solicitar_prestamo()
            case 5:
                atender_prestamos()
            case 6:
                registrar_devolucion()
            case 7:
                revisar_devoluciones_pendientes()
            case 8:
                buscar()
            case 9:
                mostrar_reportes()
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
        print("4. Registrar devolución de un libro")
        print("5. Salir")
        try:
            opcion = int(input("Ingrese su opcion: "))
        except ValueError:
            print("\n Error de entrada: Debe ingresar únicamente el número correspondiente a la opción elegida del 1 al 5")
            continue

        match opcion:
            case 1:
                consultar_libros()
            case 2:
                solicitar_prestamo(usuario_actual)
            case 3:
                mostrar_mis_prestamos(usuario_actual)
            case 4:
                registrar_devolucion(usuario_actual)
            case 5:
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