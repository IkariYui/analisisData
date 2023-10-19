import random
import pandas as pd

# List of tree types
tree_types = ['Guayacanes', 'Acacias', 'Cedros', 'Pinos', 'Eucaliptos', 'Robles', 'Palmas', 'Mimosa', 'Madroño', 'Ficus', 'Olivos']

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

def generateData(dataRecords):
    records = []

    for _ in range (dataRecords):
        municipality = random.choice(municipalities)
        treeType = random.choice(tree_types)
        quantity = random.randint(100, 5000)
        record = {'municipio': municipality, 'tipo de árbol': treeType, 'cantidad': quantity}
        records.append(record)

    return records

# records = generateData(2000)    

def createDataframe(records):
    df = pd.DataFrame(records)
    return df

