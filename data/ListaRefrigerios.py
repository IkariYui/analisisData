import random
snacks = []


for i in range(500):
    name = random.choice(['Bimbo', 'Sencillo', 'Completo', 'Premium'])
    price = random.randint(5000, 25000)
    cuantity = random.randint(500, 5000)
    totalPrice = (price * cuantity)
    snack = [name, price, cuantity, totalPrice]
    snacks.append(snack)

