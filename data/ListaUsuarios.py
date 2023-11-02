import random
usuarios = []

for i in range(10):
    name = random.choice(['Sara', 'Juan', 'Jorge', 'Andrés'])
    password = random.choice(['Admin123', 'Arboles000'])
    age = random.randint(18, 62)
    usuario = [name, password, age]
    usuarios.append(usuario)

print (usuarios)    