
from colorama import Fore


#Clase producto  

class Producto():
    def __init__(self,name_producto, precio ,stock, codigo):
        self.name = name_producto
        self.precio = precio
        self.stock = stock
        self.codigo = codigo
        self.historial = []

    def cambio_stock(self, cambio):
        self.stock = cambio  
        self.historial.append((f"nuevo cambio al stock: {cambio}"))                               
    def valor_total(self):
        return print(f"valor total stock {self.stock * self.precio}")
    
    
    def __str__(self):
        return f"nombre del producto : '{self.name}'\nStock del producto : '{self.stock}'\nhistorial de cambios : '{self.historial}' \ncodigo de barras {self.codigo}"


# Creando primer producto
producto1 = Producto("Patata",1000,10,10001111111)
producto2 = Producto("arroz",200,1,100001011010101)
print(producto1) # imprimiendo el método mágico del __str__ 
"""
producto1.cambio_stock(20)
producto1.valor_total()
"""


print("##################################")#Esto es solo un separador para que se distinga 




class Inventario():
    def __init__(self):
        self.inventari = {
            #Le puse inventari por que no tengo imaginacion profe
            }
        
    """
    aqui se guarda el nuevo producto, con la clave que es su codigo y el valor que es el objeto :3
    """
    def nuevo_produ(self, producto):
        self.inventari[producto.codigo] = producto 


    """
    aca se imprime todo el inventario
    """
    def productosp(self): 
        for x in self.inventari.values():
            print(x) #como la clase producto ya tiene un __str__ cuando hago print aparece el mismo print de la clase 
    
    """
    aqui se cambia el stock
    """
    def stockito(self, codigo_del_que_se_tiene_que_cambiar ,nuevo_stock ):
        for x , i in zip(self.inventari,self.inventari.values()):
            if x == codigo_del_que_se_tiene_que_cambiar:
                i.stock = nuevo_stock 

                i.historial.append((f"nuevo cambio al stock: {nuevo_stock}"))
                break           #aca agrego el cambio a el historial solo para que el cambio igual se registre en la lista

    """
    y aca da el total del inventario
    """
    def totalinv(self):
        total_de_la_boleta = []
        for valor in self.inventari.values(): 
            costo = valor.stock * valor.precio
            total_de_la_boleta.append(costo)
        
        print(f"el valor total de todo el inventario es: {sum(total_de_la_boleta)}")
#aqui yo creo una instancia del inventario
inv = Inventario()

#aca agrego productos
inv.nuevo_produ(producto1)
inv.nuevo_produ(producto2)

#aca muestro el inventario
inv.productosp()


#aca cambio el stock de un producto
inv.stockito(10001111111 , 20) #el primer valor es el codigo del producto el segundo el nuevo stock

#aca se imprime el valor total 
inv.totalinv()
