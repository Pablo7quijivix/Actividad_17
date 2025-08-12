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




