#print("prueba")

class Inventario:
    def __init__(self):
        #creamos la lista vacia ya inicializada, (encapsulamiento para poder manipular la lista)
        self.productos = []

#metodo de agregar producto a nuestro carrito
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f'Producto "{producto}" agregado.')

#metodo para eliminar productos de nuestro carrito
    def eliminar_producto(self, producto):
        try:
            self.productos.remove(producto)
            print(f'Producto "{producto}" eliminado.')
        except ValueError:
            #excepcion por si la lista esta vacia no tire "none" sino de otro intento de
            # hacer otra accion dentro del menu
            print(f'Error: El producto "{producto}" no está en el inventario.')

  #metodo de eliminar ultimo producto
    def eliminar_ultimo_producto(self):
        if self.productos:
            producto = self.productos.pop()
            print(f'Último producto "{producto}" eliminado.')
            return producto
        else:
            print("El inventario está vacío, no hay productos para eliminar.")
            return None

#metodo de busqueda de cualquier producto
    def buscar_producto(self, producto):
        try:
            indice = self.productos.index(producto)
            print(f'Producto "{producto}" encontrado en la posición {indice}.')
            return indice
        except ValueError:
            print(f'Producto "{producto}" no encontrado en el inventario.')
            return -1

#funcion para contar cuantos productos hay dentro de nuestra lista instanceada e incapsulada como un atributo
# para poder manipularla.
    def contar_producto(self, producto):
        cantidad = self.productos.count(producto)
        print(f'El producto "{producto}" aparece {cantidad} vez/veces en el inventario.')
        return cantidad

    # metodo para ordenar con metodo sort, de manera ascendente (cual fue el priemer producto al ultimo)
    def ordenar_productos(self):
        self.productos.sort()
        print("Inventario ordenado alfabéticamente.")

    # metodo de enlistar los productos dentro de nuestra lista
    # y una condicional por si el usuario elige esta opcion si aun nuestra lista esta vacia y no tire error.
    def listar_productos(self):
        if self.productos:
            print("\nProductos en inventario:")
            for i, producto in enumerate(self.productos):
                print(f"{i}: {producto}")
            print()
        else:
            print("El inventario está vacío.")

#funcion solo para mostrar el menu para llamarlo unicmaente cuando lo necesite
def mostrar_menu():
    print("""
--- MENÚ INVENTARIO ---
1. Agregar producto
2. Eliminar producto
3. Eliminar último producto agregado
4. Buscar producto
5. Contar producto
6. Ordenar productos
7. Mostrar todos los productos
8. Salir
""")
#instancio mi propia clase por asi decirlo, pq una clase es como una funcion master
# que esta compuesta por funciones pequeñas que se llaman "metodos"
#como la usamremos dentro del codigo, solo la llamaremos por la variable "inventario" pq
# ya le asignamos la clase así "inventario = Inventario()"
inventario = Inventario()

while True:
    mostrar_menu()
    try:
        opcion = int(input("Elige una opción (1-8): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
#dentro del match para evitar erroes de "DEDAZOS" usamos la funcion .strip() que unicamente
# sirve para eliminar espacios extras a ambos lados de una cadena, por si el usuario mete un space en una
# opcion, asi evitamos errores de comparacion por numero de espacios, si ese fuera el caso
    match opcion:
        case 1:
            producto = input("Nombre del producto a agregar: ").strip()
            if producto:
                inventario.agregar_producto(producto)
            else:
                print("El nombre no puede estar vacío.")

        case 2:
            producto = input("Nombre del producto a eliminar: ").strip()
            if producto:
                inventario.eliminar_producto(producto)
            else:
                print("El nombre no puede estar vacío.")

        case 3:
            inventario.eliminar_ultimo_producto()

        case 4:
            producto = input("Nombre del producto a buscar: ").strip()
            if producto:
                inventario.buscar_producto(producto)
            else:
                print("El nombre no puede estar vacío.")

        case 5:
            producto = input("Nombre del producto para contar: ").strip()
            if producto:
                inventario.contar_producto(producto)
            else:
                print("El nombre no puede estar vacío.")

        case 6:
            inventario.ordenar_productos()

        case 7:
            inventario.listar_productos()

        case 8:
            print("Saliendo del sistema... ¡Gracias!")
            break

        case _:
            print("Opción inválida, intenta nuevamente.")





