import random
snacks = []


for i in range(500):
    name = random.choice(['Bimbo', 'Sencillo', 'Completo', 'Premium', 'Noel', 'Digiorno', 'HotPockets', 'Stouffers'])
    price = random.randint(1000, 25000)
    cuantity = random.randint(500, 2000)
    totalPrice = (price * cuantity)
    snack = [name, price, cuantity, totalPrice]
    snacks.append(snack)

