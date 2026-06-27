class Recurso:

    def __init__(self, area, total_camas):
        self.area = area                      # Seguimos repitiendo el area (es ultra importante xd)"Emergencia", "UCI", "Pediatría"
        self.total_camas = total_camas        # Aqui damos la capacidad máxima del área
        self.camas_ocupadas = 0              # Aqui revisamos cuántas camas están en uso
        self.pacientes_en_area = []          # Y finalmente la lista de pacientes en cada área
 
    def admitir_paciente(self, paciente):
        #Admite un paciente al área si hay camas disponibles.
        if self.camas_disponibles() == 0:
            print(f"No hay camas disponibles en {self.area}.")
            return False
        self.camas_ocupadas += 1
        self.pacientes_en_area.append(paciente)
        paciente.area_asignada = self.area
        print(f"Paciente {paciente.nombre} admitido en {self.area}. "
              f"Camas disponibles: {self.camas_disponibles()}")
        return True
 
    def liberar_cama(self, paciente):
        #Libera una cama cuando el paciente recibe el alta.
        if paciente in self.pacientes_en_area:
            self.pacientes_en_area.remove(paciente)
            self.camas_ocupadas -= 1
            print(f"Cama liberada en {self.area}. "
                  f"Camas disponibles: {self.camas_disponibles()}")
            return True
        print(f"El paciente {paciente.nombre} no está en {self.area}.")
        return False
 
    def camas_disponibles(self):
        #Retorna el número de camas libres en el área.
        return self.total_camas - self.camas_ocupadas
 
    def esta_colapsada(self):
        #Retorna True si el área está al 100% de ocupación.
        return self.camas_ocupadas >= self.total_camas
 
    def porcentaje_ocupacion(self):
        #Retorna el porcentaje de ocupación del área.
        return round((self.camas_ocupadas / self.total_camas) * 100, 1)
 
    def __str__(self):
        estado = "COLAPSADA" if self.esta_colapsada() else "OK"
        return (f"{self.area} | Camas: {self.camas_ocupadas}/{self.total_camas} "
                f"({self.porcentaje_ocupacion()}%) | {estado}")
