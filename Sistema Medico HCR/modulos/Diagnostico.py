import sys
import os

# Esto es para que no tire error al conectar con las otras carpetas del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Traemos las patologías que Génesis ya dejó listas en Datos_Iniciales
from Datos.Datos_Iniciales import patologias_frecuentes

class ArbolDiagnostico:
    def __init__(self):
        # Armo la base de conocimiento asignando síntomas a TODAS las enfermedades del HRC
      
        self.base_conocimiento = {
            "Infecciones Respiratorias Agudas": ["tos", "fiebre", "dificultad para respirar"],
            "Diabetes Mellitus": ["mucha sed", "vision borrosa", "fatiga constante"],
            "Hipertensión Arterial": ["dolor de cabeza fuerte", "zumbido en oidos", "mareos"],
            "Gastroenteritis": ["diarrea", "vomito", "dolor de estomago"],
            "Fracturas Óseas": ["dolor agudo", "hinchazon", "deformidad visible"],
            "Accidentes de Tránsito": ["trauma", "hemorragia", "fracturas multiples"],
            "Enfermedades Cardiovasculares": ["dolor en el pecho", "palpitaciones", "dificultad para respirar"],
            "Enfermedades Renales": ["dolor lumbar", "orina oscura", "hinchazon en piernas"],
            "Enfermedades Hepáticas": ["ictericia", "dolor abdominal alto", "nauseas"],
            "Enfermedades Infecciosas": ["fiebre alta", "sudoracion", "malestar general"],
            "Enfermedades Dermatológicas": ["sarpullido", "picazon", "enrojecimiento"],
            "Enfermedades Neurológicas": ["convulsiones", "perdida de memoria", "confusion"]
        }

    def evaluar_paciente(self, sintomas_presentados, paciente):
        # Lista vacía donde guardaremos el diagnóstico si se encuentra
        diagnostico_encontrado = []
        enfermedades = list(self.base_conocimiento.keys())

        # Arrancamos la búsqueda
        exito = self._buscar_diagnostico(
            sintomas_presentados, 
            enfermedades, 
            indice_actual=0, 
            ruta_actual=diagnostico_encontrado
        )

        # Si el algoritmo encontró algo, lo devuelve. Si no, lo manda a observación
        if exito and diagnostico_encontrado:
            return diagnostico_encontrado[0]
        else:
            return "Indeterminado"

    def _buscar_diagnostico(self, sintomas_paciente, enfermedades, indice_actual, ruta_actual):
        # --- Aquí empieza la lógica de Recursividad + Backtracking ---
        
        # CASO BASE 1: Si ya metimos una enfermedad en la ruta, corta ahí
        if len(ruta_actual) > 0:
            return True

        # CASO BASE 2: Si ya revisó toda la lista y no hubo match, F (falso)
        if indice_actual >= len(enfermedades):
            return False

        # Sacamos la enfermedad actual que vamos a evaluar
        enfermedad_actual = enfermedades[indice_actual]
        sintomas_de_enfermedad = self.base_conocimiento.get(enfermedad_actual, [])

        # Cuento cuántos síntomas coinciden (le puse mínimo 2 para que sea válido)
        coincidencias = sum(1 for s in sintomas_paciente if s in sintomas_de_enfermedad)
        
        if coincidencias >= 2:
            # Si hay coincidencias, tomamos la decisión y la metemos a la ruta
            ruta_actual.append(enfermedad_actual)

            # RECURSIVIDAD
            if self._buscar_diagnostico(sintomas_paciente, enfermedades, indice_actual + 1, ruta_actual):
                return True

            # BACKTRACKING
            ruta_actual.pop()

        # Si no hubo match, recursividad para saltar a evaluar la siguiente enfermedad
        return self._buscar_diagnostico(sintomas_paciente, enfermedades, indice_actual + 1, ruta_actual)