from datetime import datetime

class Doctor:
    """
    Turno: "mañana" (7am-1pm), "tarde" (1pm-7pm), "noche" (7pm-7am)
    """
 
    def __init__(self, id, nombre, especialidad, turno):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad  # Aqui colocamos a lo que se dedica el doctor "Emergencia", "Cirugía", "Pediatría"
        self.turno = turno                # Su turno de disponibilidad :v "mañana", "tarde", "noche"
        self.disponible = True            # (Aqui si esta ocupad o no) True = libre, False = atendiendo paciente
        self.paciente_actual = None       # Aqui al paciente que está atendiendo ahora
        self.pacientes_atendidos = []     # Y finalmente su historial del turno
 
    def asignar_paciente(self, paciente):
        #Aqui se asigna un paciente al doctor si está disponible
        if not self.disponible:
            print(f"El Dr. {self.nombre} ya está ocupado con {self.paciente_actual.nombre}.")
            return False
        self.disponible = False
        self.paciente_actual = paciente
        paciente.iniciar_atencion()
        print(f"Dr. {self.nombre} atendiendo a {paciente.nombre}.")
        return True
 
    def liberar(self):
        # Libera al doctor cuando termina de atender al paciente
        if self.paciente_actual:
            self.paciente_actual.dar_alta()
            self.pacientes_atendidos.append(self.paciente_actual)
            print(f"Dr. {self.nombre} dio de alta a {self.paciente_actual.nombre}.")
            self.paciente_actual = None
        self.disponible = True
 
    def total_atendidos(self):
        # Su record de atendidos jsjsjs
        return len(self.pacientes_atendidos)
 
    def esta_en_turno(self):
        # Verifica si el doctor está en su turno según la hora actual
        hora = datetime.now().hour
        if self.turno == "mañana":
            return 7 <= hora < 13
        elif self.turno == "tarde":
            return 13 <= hora < 19
        elif self.turno == "noche":
            return hora >= 19 or hora < 7
        return False
 
    def __str__(self):
        estado = "Disponible" if self.disponible else f"Atendiendo a {self.paciente_actual.nombre}"
        return (f"Dr. {self.nombre} | {self.especialidad} | "
                f"Turno: {self.turno} | {estado} | "
                f"Atendidos hoy: {self.total_atendidos()}")