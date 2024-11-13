class Personaje():
    def __init__(self, name, hp, dmg):
        self.name= name
        self.hp=hp
        self.dmg=dmg
    
    def attack(self, otro_personaje):
        print(f"{self.name} ataca a {otro_personaje.name} haciendo {self.dmg}!")
        otro_personaje.hp -= self.dmg

    def verificacion(self):
        return self.hp > 0

    def __str__(self):
        return f"Estado: {self.name} queda con {self.hp} de vida."
    
personaje1= Personaje("JoseGamer777", 200, 33)
personaje2= Personaje("Victor", 100, 40)
Combate=True
while Combate:
    personaje1.attack(personaje2)
    print(personaje1)
    print(personaje2)
    if personaje2.verificacion()==False:
        print(f"{personaje1.name} ha quedado de pie y {personaje2.name} ha caido")
        Combate=False
    else:
        personaje2.attack(personaje1)
        print(personaje1)
        print(personaje2)
        if personaje1.verificacion()==False:
            print(f"{personaje2.name} ha quedado de pie y {personaje1.name} ha caido")
            Combate=False
        



