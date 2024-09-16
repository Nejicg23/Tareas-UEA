# Definir la matriz de temperaturas
temperaturas = [
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 35},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 38},
            {"day": "Viernes", "temp": 39},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]

# Inicializar los nombres de las ciudades
ciudades = ["Guayaquil", "Quito", "Cuenca"]

# Calcular y mostrar los promedios
for i, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    for semana_num, semana in enumerate(temperaturas[i]):
        suma_temperaturas = sum(dia["temp"] for dia in semana)
        promedio_semana = suma_temperaturas / len(semana)
        print(f"  Semana {semana_num + 1}: {promedio_semana:.2f}°C")
    print()
