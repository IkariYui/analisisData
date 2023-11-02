import random
snacks = []

for i in range(10):
    name = random.choice(['Bimbo', 'Sencillo', 'Completo', 'Premium'])
    drink = random.choice(['Hit', 'Tampico', 'Coca Cola'])
    cuantity = random.randint(1, 20)
    snack = [name, drink, cuantity]
    snacks.append(snack)

print (snacks)