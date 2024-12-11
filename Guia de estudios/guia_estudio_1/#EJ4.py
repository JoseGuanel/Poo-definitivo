class Jardin_botanico:
    def __init__(self, tipo_planta, E_crecimiento, E_agua): 
        self.tipo_planta = tipo_planta
        self.E_crecimiento = E_crecimiento
        self.E_agua = E_agua
        self.necesita_riego = True  # Inicialmente, la planta necesita riego
    
    def __str__(self):
        return (f"Planta: {self.tipo_planta}, "
                f"Estado de Crecimiento: {self.E_crecimiento}, "
                f"Necesidades de Agua: {self.E_agua}, "
                f"Necesita Riego: {self.necesita_riego}")

class Herramienta: #creo una clase especial para herramientas y asi dejarlo aparte mejor
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return f"Herramienta: {self.nombre}, Cantidad: {self.cantidad}"

class Gestion_jardin:   # calse mas importantes ya que aqui haremos funcionar la gestiom
    def __init__(self): 
        self.area1 = [] # dividimo nuestro jardin en diferentes areas para mejor manejo y poder ir intercambiando las plantas de lugar
        self.area2 = []
        self.area3 = []
        self.area4 = []
        self.herramientas = []  # Lista de herramientas usasdad
        self.fertilizantes_usados = 0  # Contador de fertilizantes usados

    def agregar_plantas(self, planta, area):    
        if area == 1:
            self.area1.append(planta)
        elif area == 2:
            self.area2.append(planta)
        elif area == 3:
            self.area3.append(planta)
        elif area == 4:
            self.area4.append(planta)
        else:
            print("Área no válida.")
            return
        print(f"{planta.tipo_planta} ha sido añadida al área {area}")

    def cambio_lugar(self, planta, area_origen, area_destino):
        # Mueve la planta de un área a otra
        if area_origen == 1 and planta in self.area1:
            self.area1.remove(planta)
            self.agregar_plantas(planta, area_destino)
        elif area_origen == 2 and planta in self.area2:
            self.area2.remove(planta)
            self.agregar_plantas(planta, area_destino)
        elif area_origen == 3 and planta in self.area3:
            self.area3.remove(planta)
            self.agregar_plantas(planta, area_destino)
        elif area_origen == 4 and planta in self.area4:
            self.area4.remove(planta)
            self.agregar_plantas(planta, area_destino)
        else:
            print(f"La planta no se encuentra en el área {area_origen}.")

    def regar_planta(self, planta):
        if planta.necesita_riego:
            print(f"Regando la planta {planta.tipo_planta}...")
            planta.necesita_riego = False  # Cambiar estado de riego
            print(f"La planta {planta.tipo_planta} ha sido regada.")
        else:
            print(f"La planta {planta.tipo_planta} no necesita riego en este momento.")

    def agregar_herramienta(self, herramienta):
        self.herramientas.append(herramienta)
        print(f"{herramienta} ha sido añadida al inventario de herramientas.")

    def usar_fertilizante(self, cantidad):
        self.fertilizantes_usados += cantidad
        print(f"Se han usado {cantidad} unidades de fertilizante.")

    def mostrar_areas(self):  # Método que muestra las áreas del jardín
        print("Estado del Jardín:")
        print(f"Área 1: {[str(planta) for planta in self.area1]}")
        print(f"Área 2: {[str(planta) for planta in self.area2]}")
        print(f"Área 3: {[str(planta) for planta in self.area3]}")
        print(f"Área 4: {[str(planta) for planta in self.area4]}")
        print("Herramientas disponibles:")
        print([str(herramienta) for herramienta in self.herramientas])

# Crear algunas plantas
planta1 = Jardin_botanico("Rosa", "Brote", 10)
planta2 = Jardin_botanico("Cactus", "Planta Adulta", 5)

planta3 = Jardin_botanico("Lavanda", "Planta Adulta", 4)
planta4 = Jardin_botanico("Suculenta", "Brote", 2)

# Crear herramientas
herramienta1 = Herramienta("Pala", 3)
herramienta2 = Herramienta("Tijeras", 5)

# Crear la gestión del jardín
gestion = Gestion_jardin()

# Agregar plantas a las áreas
gestion.agregar_plantas(planta1, 1)
gestion.agregar_plantas(planta2, 2)

# Agregar herramientas al inventario
gestion.agregar_herramienta(herramienta1)
gestion.agregar_herramienta(herramienta2)

# Regar una planta
gestion.regar_planta(planta1)

# Usar fertilizante
gestion.usar_fertilizante(2)

# Cambiar la planta1 a otra área
gestion.cambio_lugar(planta1,1, 3)

# Mostrar estado del jardín
gestion.mostrar_areas()

#Agregamos nuevas plantas para tener una planta en cada area
gestion.agregar_plantas(planta3, 1)  # Agrega Lavanda al área 1
gestion.agregar_plantas(planta4, 4)  # Agrega Suculenta al área 4

#printeamos actualizacion de jardin y areas
gestion.mostrar_areas()

