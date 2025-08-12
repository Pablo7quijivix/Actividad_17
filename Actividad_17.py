#print("prueba")

class Inventario:
    def __init__(self):
        #creamos la lista vacia ya inicializada, (encapsulamiento para poder manipular la lista)
        self.productos = []

#funcion de agregar producto a nuestro carrito
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f'Producto "{producto}" agregado.')

#funcion para eliminar productos de nuestro carrito
    def eliminar_producto(self, producto):
        try:
            self.productos.remove(producto)
            print(f'Producto "{producto}" eliminado.')
        except ValueError:
            #excepcion por si la lista esta vacia no tire "none" sino de otro intento de
            # hacer otra accion dentro del menu
            print(f'Error: El producto "{producto}" no está en el inventario.')
