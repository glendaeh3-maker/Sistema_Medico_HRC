from datetime import datetime

class Paciente:
    #Aqui construimos la clase paciente con sus atributos principales :)
    def __init__(self, id, nombre, edad, procedencia, nivel_triaje, es_referido=False):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.procedencia = procedencia   # Aqui puede venir ya sea de: "Chota", "Cutervo", "Zona rural"
        self.nivel_triaje = nivel_triaje # El nivel de atencion de los clientes 1=Inmediato, 2=Urgente, 3=Moderado, 4=Leve, 5=Sin urgencia
        self.es_referido = es_referido   # ¿Viene derivado de una posta?
        self.estado = "En espera"        # En espera → En atención → Alta
        self.hora_llegada = datetime.now()
        self.hora_atencion = None
 
    def iniciar_atencion(self):
        #Cambia el estado del paciente a 'En atención' y registra la hora
        self.estado = "En atención"
        self.hora_atencion = datetime.now()
 
    def dar_alta(self):
        #Cambia el estado del paciente a 'Alta'.
        self.estado = "Alta"
 
    def tiempo_espera(self):
        #Retorna los minutos que esperó el paciente antes de ser atendido.
        if self.hora_atencion:
            diferencia = self.hora_atencion - self.hora_llegada
            return round(diferencia.total_seconds() / 60, 2)
        return None
 
    def es_critico(self):
        #Retorna True si el paciente necesita atención inmediata (triaje 1 o 2).
        return self.nivel_triaje <= 2
 
    def __str__(self):
        referido = " [Referido]" if self.es_referido else ""
        return (f"ID: {self.id} | {self.nombre} | {self.edad} años | "
                f"{self.procedencia}{referido} | Triaje: {self.nivel_triaje} | {self.estado}")
 
    def __lt__(self, otro):
        #Permite comparar pacientes por triaje (para ordenarlos en la cola).
        return self.nivel_triaje < otro.nivel_triaje
