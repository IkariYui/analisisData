
import random
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

agricultureSecretary=[
    'Juan Carlos',
    'Andrés Pérez',
    'Carlos Soza',
    'Camilo Gómez',
    'David Madrid',
    'Daniela Alzate',
    'Alejandro Hernández'
]

alcaldias = []

for _ in range(125):
    nombre_alcaldia = random.choice(municipalities)
    presupuesto_siembra = random.randint(1000000, 10000000)
    nombre_secretario = random.choice(agricultureSecretary)
    alcaldia = {
        'NombreAlcaldía': nombre_alcaldia,
        'PresupuestoSiembra': presupuesto_siembra,
        'NombreSecretario': nombre_secretario
    }
    
    alcaldias.append(alcaldia)

for item in alcaldias:
    print(item)
    
#Municipio, especie, cantidad árboles
#Municipios con más de 90 árboles
#Municipios con ceibas
#Municipios con siembras <10

#Dentro de cultivadores, refrigerios, siembras  secciones para cada filtro    