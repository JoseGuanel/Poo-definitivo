
class Libro():
    def __init__(self,Titulo ,Autor,Año_publicacion,Stock_libros):
        self.titulaso = Titulo #tuve que ponerle asi por que decia un error por algo de .title
        self.autor = Autor
        self.año_de_publicacion = Año_publicacion
        self.cantidad_disponible = Stock_libros


class Biblioteca():
    def __init__(self):
        self.inventario= {


        }
    
    def agregar_libro(self, libro):
        if libro.titulaso not in self.inventario:
            self.inventario[libro.titulaso] = libro
            print("Libro agregado")
        else:
            preguntita = input("El libro se encuentra en el inventario. ¿Desea agregar más copias? (si/no): ")
            if preguntita.lower() == "si":
                preguntasa = int(input("¿Cuántas copias desea agregar? "))
                for x, i in zip(self.inventario, self.inventario.values()):
                    if x == libro:
                        i.cantidad_disponible += preguntasa 
                        break
        
    def busqueda(self,buscar):#Permite la busqueda de libros y sus datos
        for x,i in zip(self.inventario, self.inventario.values()):
            if x == buscar:
                print(f"""
                    Titulo del libro: {i.titulaso} 
                    Autor: {i.autor}
                    Año de publicacion: {i.año_de_publicacion}
                    cantidad en inventario: {i.cantidad_disponible}
                    """)
            if buscar not in self.inventario:
                print(f"el libro {buscar} no esta en el inventario")
                break
    
    def actualizar(self):
        pregunta = input("¿a que libro desea cambiarle la informacion? ")
        if pregunta in self.inventario:
            nueva_pregunta= input(f"""
                            ¿Que informacion desea cambiar de el libro: {pregunta}?
                            titulo: 1
                            Autor: 2
                            Año de publicacion: 3
                            Cantidad en inventario: 4
                            eliminar por completo del inventario: 007
                            ingrese una opcion numerica: """)
            if nueva_pregunta == "1":
                nuevo_titulo = input("Ingrese el nuevo titulo: ")
                for x, i in zip(self.inventario, self.inventario.values()):
                    if x == pregunta:
                        i.titulaso = nuevo_titulo
                        break
            elif nueva_pregunta == "2":
                nuevo_autor = input("Ingrese el nuevo autor: ")
                for x, i in zip(self.inventario, self.inventario.values()):
                    if x == pregunta:
                        i.autor = nuevo_autor
                        break
                
            elif nueva_pregunta == "3":
                nuevo_Año = input("Ingrese el nuevo año de publicacion: ")
                for x, i in zip(self.inventario, self.inventario.values()):
                    if x == pregunta:
                        i.año_de_publicacion = nuevo_Año
                        break
            elif nueva_pregunta == "4":
                nuevo_stock = input("Ingrese el nuevo stock de este libro: ")
                for x, i in zip(self.inventario, self.inventario.values()):
                    if x == pregunta:
                        i.cantidad_disponible = nuevo_stock
                        break
            elif nueva_pregunta == "007":
                for x in self.inventario:
                    if x == pregunta:
                        del(self.inventario[x])
                        break
            else:
                print("opcion invalida")
                
        else:
            print(f"el libro {pregunta} no esta en el inventario")
            
#Libros
librito1 = Libro("I Am Not a Serial Killer", "Dan Wells","5 de marzo de 2009", 12 )
librito2 = Libro("Dialogos de Platon", "Platon", "1513", 3 )
librito3 = Libro("Mala onda", "Alberto Fuguet", "14 de noviembre de 1991", 1)

#biblioteca 
inv= Biblioteca()

#agrego mis libritos 
inv.agregar_libro(librito1)
inv.agregar_libro(librito2)
inv.agregar_libro(librito3)

#busco mis libritos
inv.busqueda("Mala onda")

#Actualizo la informacion
inv.actualizar() #Aca no entra ningun parametro

#Aca verifica si el libro a agregar ya se encontraba en el inventario y agrega mas stock
inv.agregar_libro(librito3)



"""
print(librito3.cantidad_disponible) el libro 3 es mala onda esta linea de aca es solo para probar si cambia la informacion
"""
