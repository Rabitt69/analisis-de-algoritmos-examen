class Puesto:
    def __init__(self, codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo

# Lista principal
lista_puestos = []

# ---------------- FUNCIONES ----------------

def AgregaPuesto():
    codigo = int(input("Ingrese código: "))
    descripcion = input("Ingrese descripción: ")
    area = input("Ingrese área solicitante: ")
    plazas = int(input("Ingrese plazas requeridas: "))
    sueldo = float(input("Ingrese sueldo: "))

    # Validaciones
    if len(descripcion) < 3 or len(area) < 3:
        print("Error: textos deben tener mínimo 3 letras")
        return

    if codigo <= 0 or plazas <= 0 or sueldo <= 0:
        print("Error: valores numéricos deben ser mayores a 0")
        return

    # Búsqueda lineal para evitar duplicados
    for p in lista_puestos:
        if p.codigo == codigo or p.descripcion == descripcion or p.areaSolicitante == area:
            print("Error: datos duplicados")
            return

    nuevo = Puesto(codigo, descripcion, area, plazas, sueldo)
    lista_puestos.append(nuevo)
    print("Puesto agregado correctamente")

# -------------------------------------------

def MostrarTodo():
    if len(lista_puestos) == 0:
        print("No hay datos")
        return

    for p in lista_puestos:
        print(p.codigo, p.descripcion, p.areaSolicitante, p.plazasRequeridas, p.sueldo)

# -------------------------------------------

def ordenar_burbuja_codigo():
    n = len(lista_puestos)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_puestos[j].codigo < lista_puestos[j+1].codigo:
                aux = lista_puestos[j]
                lista_puestos[j] = lista_puestos[j+1]
                lista_puestos[j+1] = aux

def BorraPuesto():
    codigo = int(input("Ingrese código a eliminar: "))
    
    ordenar_burbuja_codigo()

    for i in range(len(lista_puestos)):
        if lista_puestos[i].codigo == codigo:
            lista_puestos.pop(i)
            print("Eliminado correctamente")
            return

    print("No encontrado")



def ordenar_insercion_sueldo():
    for i in range(1, len(lista_puestos)):
        aux = lista_puestos[i]
        j = i - 1
        while j >= 0 and lista_puestos[j].sueldo < aux.sueldo:
            lista_puestos[j+1] = lista_puestos[j]
            j -= 1
        lista_puestos[j+1] = aux

def BuscaSueldo():
    sueldo_buscar = float(input("Ingrese sueldo a buscar: "))
    
    ordenar_insercion_sueldo()

   
    izquierda = 0
    derecha = len(lista_puestos) - 1
    encontrado = -1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_puestos[medio].sueldo == sueldo_buscar:
            encontrado = medio
            break
        elif lista_puestos[medio].sueldo < sueldo_buscar:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    if encontrado == -1:
        print("No encontrado")
        return

    i = encontrado
    while i >= 0 and lista_puestos[i].sueldo == sueldo_buscar:
        print(lista_puestos[i].codigo, lista_puestos[i].descripcion)
        i -= 1

    i = encontrado + 1
    while i < len(lista_puestos) and lista_puestos[i].sueldo == sueldo_buscar:
        print(lista_puestos[i].codigo, lista_puestos[i].descripcion)
        i += 1



def ordenar_seleccion_total():
    n = len(lista_puestos)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            total_j = lista_puestos[j].plazasRequeridas * lista_puestos[j].sueldo
            total_max = lista_puestos[max_idx].plazasRequeridas * lista_puestos[max_idx].sueldo
            
            if total_j > total_max:
                max_idx = j

        aux = lista_puestos[i]
        lista_puestos[i] = lista_puestos[max_idx]
        lista_puestos[max_idx] = aux

def PuestosAContratar():
    monto = float(input("Ingrese monto total: "))
    
    ordenar_seleccion_total()

    acumulado = 0

    for p in lista_puestos:
        total = p.plazasRequeridas * p.sueldo
        
        if acumulado + total <= monto:
            print(p.codigo, p.descripcion, "Total:", total)
            acumulado += total
        else:
            break

# -------------------------------------------

# DATOS INICIALES (6 puestos)
lista_puestos.append(Puesto(1, "Programador", "TI", 2, 2500))
lista_puestos.append(Puesto(2, "Analista", "Finanzas", 1, 3000))
lista_puestos.append(Puesto(3, "Diseñador", "Marketing", 2, 2000))
lista_puestos.append(Puesto(4, "Soporte", "TI", 3, 1500))
lista_puestos.append(Puesto(5, "Supervisor", "Ventas", 1, 2800))
lista_puestos.append(Puesto(6, "Logistica", "Almacen", 2, 1800))

# ---------------- MENÚ ----------------

while True:
    print("\n1. Agregar Puesto")
    print("2. Mostrar Todo")
    print("3. Borrar Puesto")
    print("4. Buscar por Sueldo")
    print("5. Puestos a Contratar")
    print("6. Salir")

    op = input("Seleccione opción: ")

    if op == "1":
        AgregaPuesto()
    elif op == "2":
        MostrarTodo()
    elif op == "3":
        BorraPuesto()
    elif op == "4":
        BuscaSueldo()
    elif op == "5":
        PuestosAContratar()
    elif op == "6":
        print("Fin del programa")
        break
    else:
        print("Opción inválida")