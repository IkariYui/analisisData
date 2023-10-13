import pandas as pd
import random
from funcionCrearDatos import sumarArboles
#Analyze a list of data
cities = ['Medellín', 'Bogotá', 'Cali', 'Barranquilla', 'Santa Marta', 'Montería', 'Ciénaga', 'Valledupar', 'Sincelejo', 'Manizales']

# List of municipalities in Antioquia
municipalities = ['Carepa',
'Carmen De Viboral',
'Carolina',
'Caucasia',
'Chigorodó',
'Cisneros',
'Cocorná',
'Concepción',
'Concordia',
'Copacabana',
'Dabeiba',
'Don Matías',
'Ebejico',
'El Bagre',
'Entrerrios',
'Envigado',
'Fredonia',
'Frontino',
'Giraldo',
'Girardota',
'Gómez Plata',
'Granada',
'Guadalupe'
'Guarne',
'Guatapé',
'Heliconia',
'Hispania',
'Itagui',
'Ituango',
'Jardín',
'Jericó',
'La Ceja',
'La Estrella',
'La Pintada',
'La Unión',
'Liborina',
'Maceo',
'Marinilla',
'Montebello',
'Murindó',
'Mutatá',
'Nariño',
'Nechí',
'Necoclí',
'Olaya',
'Peñol',
'Peque',
'Pueblorrico',
'Puerto Berrío',
'Puerto Nare',
'Puerto Triunfo',
'Remedios',
'Retiro',
'Rionegro',
'Sabanalarga',
'Sabaneta',
'Salgar',
'San Andrés',
'San Carlos',
'San Francisco',
'San Pedro De Uraba',
'San José De La Montaña',
'San Juan De Uraba',
'Santa Rosa De Osos',
'San Pedro',
'San Jerónimo',
'San Rafael',
'San Roque',
'San Vicente',
'Santa Bárbara',
'San Luis',
'Santafé de Antioquia',
'Santo Domingo',
'Santuario',
'Segovia',
'Sonsón',
'Sopetrán',
'Támesis',
'Taraza',
'Tarso',
'Titirib',
'Toledo',
'Turbo',
'Uramita',
'Urrao',
'Valdivia',
'Valparaíso',
'Vegachi',
'Venecia',
'Vigía Del Fuerte',
'Yali',
'Yarumal',
'Yolombó',
'Yondó',
'Zaragoza'
]


#Analyze an list of dictionaries
students = [
    {'id':1, 'nombre':'Juan', 'promedio':2.8},
    {'id':2,'nombre':'María','promedio':2.5},
    {'id':3, 'nombre':'Carlos', 'promedio':2.9},
    {'id':4, 'nombre': 'Andrés', 'promedio':2.6},
    {'id':5,'nombre':'Jerónimo','promedio':2.3}
]

treePerMunicipality =[
    {'id':1,'municipality':'Girardota','treeType': 'Guayacanes','amount':1500}
]

# List of municipalities in Antioquia
municipalities = ['Medellin', 'Bello', 'Itagui', 'Envigado', 'Sabaneta', 'Rionegro', 'La Ceja', 'Girardota', 'Caldas', 'Copacabana', 'Barbosa', 'Others...']

# List of tree types
tree_types = ['Guayacanes', 'Acacias', 'Cedros', 'Pinos', 'Eucaliptos', 'Robles', 'Palmas', 'Others...']

# Generate 250 random dictionaries
random_data = []
for i in range(1, 251):
    municipality = random.choice(municipalities)
    tree_type = random.choice(tree_types)
    amount = random.randint(100, 5000)  # Random amount between 100 and 5000
    
    data = {'id': i, 'municipality': municipality, 'treeType': tree_type, 'amount': amount}
    random_data.append(data)

# Print the generated data
for item in random_data:
    print(item)





#Convert lists and list of dictionaries in DataFrames
df1 = pd.DataFrame(cities)
df2 = pd.DataFrame(students)
print(df1)
print(df2)



#Analyze a CSV