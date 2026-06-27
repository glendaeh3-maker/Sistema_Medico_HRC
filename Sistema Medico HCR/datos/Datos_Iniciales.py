# Zonas de procedencia frecuentes para el Hospital Regional de Cajamarca
zonas_procedencia = [
    "Cajamarca",
    "Chota",
    "Cutervo",
    "Jaén",
    "San Ignacio",
    "San Marcos",
    "San Miguel",
    "San Pablo",
    "Santa Cruz",
    "Cajabamba",
    "Contumazá",
    "Hualgayoc",
    "Cajamarca Rural",
    "Zona Rural", #En caso si es generico
]

#Triaje de pacientes basado en la escala de Manchester
Niveles_Triaje = {
    1: "Emergencia Absoluta", #Atencion inmediata -> Rojo
    2: "Emergencia",  #Atencion en menos de 15 minutos -> Naranja
    3: "Urgencia", #Atencion en menos de 60 minutos -> Amarillo
    4: "Menos Urgente", #Atencion en menos de 120 minutos -> Verde
    5: "Urgencia Menor", #Atencion en menos de 240 minutos -> Azul
}

#Esto es para el arbol diagnostico.
#Patologias frecuentes atendidas en el Hospital Regional de Cajamarca
patologias_frecuentes = [
    "Infecciones Respiratorias Agudas",
    "Diabetes Mellitus",
    "Hipertensión Arterial",
    "Gastroenteritis",
    "Fracturas Óseas",
    "Accidentes de Tránsito",
    "Enfermedades Cardiovasculares",
    "Enfermedades Renales",
    "Enfermedades Hepáticas",
    "Enfermedades Infecciosas",
    "Enfermedades Dermatológicas",
    "Enfermedades Neurológicas",
]

#Areas de especialidad medica en el Hospital Regional de Cajamarca
Areas_Especialidad = [
    "Emergencia",
    "UCI",
    "Cirugía",
    "Medicina Interna",
    "Pediatría",
    "Ginecología y Obstetricia",
    "Traumatología",
    "Neumología",
    "Consulta Externa",
    "Observación",
]

#La capacidad de camas por area
capacidad_camas = {
    "Emergencia": 20,
    "UCI": 8,
    "Cirugía": 15,
    "Medicina Interna": 30,
    "Pediatría": 25,
    "Ginecología y Obstetricia": 20,
    "Traumatología": 15,
    "Observación": 12,
}

# Doctores iniciales xd
doctores_iniciales = [
    (1, "Carlos Mendoza",  "Emergencia",              "mañana"),
    (2, "Ana Rojas",       "Pediatría",               "mañana"),
    (3, "Luis Paredes",    "Cirugía",                 "tarde"),
    (4, "María Sánchez",   "Ginecología y Obstetricia","tarde"),
    (5, "Jorge Távara",    "UCI",                     "noche"),
    (6, "Rosa Chiclote",   "Medicina Interna",        "noche"),
    (7, "Pedro Alcántara", "Traumatología",           "mañana"),
    (8, "Elena Vargas",    "Neumología",              "tarde"),
]