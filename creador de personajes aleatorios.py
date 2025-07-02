import random

def generar_personaje():
    nombres = ["Frodo","Gandalf", "Thorin","Kirito","Kazuya","Asuna","Mikasa","Bulma","Konan","Kefla"]
    razas = ["Humano","Elfo","Enano","Demonio","Bestia","Gyioyin", "Dios", "Metahumano","Ciberhumano","Hada"]
    clases = ["Guerrero","Mago","Arquero","Curandero","Apoyo","Francotirador","Tanque","Herrero","Aldeano","Espadachin"]
    
    return {
        "nombre": random.choice(nombres),
        "raza": random.choice(razas),
        "clase": random.choice(clases),
        "vida": random.randint(50, 100),
        "ataque": random.randint(10, 50),
        "defensa": random.randint(5, 30)
    }

pj = generar_personaje()
print(pj)
