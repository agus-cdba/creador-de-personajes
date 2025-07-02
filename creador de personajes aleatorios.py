import random


nombres = ["Frodo","Gandalf", "Thorin","Kirito","Kazuya","Asuna","Mikasa","Bulma","Konan","Kefla"]
razas = ["Humano","Elfo","Enano","Demonio","Bestia","gyioyin", "dios", "Metahumano","Ciberhumano ","Hadas"]
clases = ["Guerrero","Mago","Arquero","Curandero","Apoyo","Francotirador","Tanque","Herrero","Aldeano","Espadachin"]

def generar_personaje(): 
    nombre = random.choice(nombres)
    raza = random.choice(razas)
    clase = random.choice(clases)
    vida = random.randint(50,101)
    ataque = random.randint(10,51)
    defensa = random.randint(5,31)

    personaje ={
        "nombre":nombre,
        "raza":raza,
        "clase":clase,
        "vida":vida,
        "ataque":ataque,
        "defensa":defensa
    }
    return personaje 

nuevo_personaje = generar_personaje()
print(nuevo_personaje)