import random

usuarios = []

for i in range(1000):
    name = random.choice(['Sara', 'Juan', 'Jorge', 'Andrés'])
    password = random.choice(['Admin123', 'Arboles000'])
    gender = random.choice(['H', 'M'])
    age = random.randint(18, 62)
    salary = random.randint(1160000, 5000000)
    usuario = [name, password, age, gender, salary]
    usuarios.append(usuario)

