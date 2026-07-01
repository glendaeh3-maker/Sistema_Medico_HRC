import sys
import os

# Esto es para que no tire error al conectar con las otras carpetas del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Traemos las patologías que Génesis ya dejó listas en Datos_Iniciales
from datos.Datos_Iniciales import patologias_frecuentes

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

def evaluar_paciente(self, sintomas_presentados, paciente):
    enfermedades = list(self.base_conocimiento.keys())
    mejor_diagnostico = self._buscar_diagnostico(sintomas_presentados, enfermedades, 0, mejor_actual=None)
    return mejor_diagnostico if mejor_diagnostico else "Indeterminado"


def _buscar_diagnostico(self, sintomas_paciente, enfermedades, indice_actual, mejor_actual):
    """
    Recursividad + Backtracking real: explora TODAS las enfermedades candidatas
    en vez de detenerse en la primera, y se queda con la de mas coincidencias.
    mejor_actual guarda una tupla (nombre_enfermedad, cantidad_coincidencias).
    """
    # CASO BASE: ya revisamos toda la lista de enfermedades
    if indice_actual >= len(enfermedades):
        return mejor_actual[0] if mejor_actual else None

    enfermedad_actual = enfermedades[indice_actual]
    sintomas_de_enfermedad = self.base_conocimiento.get(enfermedad_actual, [])
    coincidencias = sum(1 for s in sintomas_paciente if s in sintomas_de_enfermedad)

    # Decision: ¿esta enfermedad es mejor candidata que la que llevamos hasta ahora?
    if coincidencias >= 2 and (mejor_actual is None or coincidencias > mejor_actual[1]):
        # Tomamos la decision (avanzamos con esta como mejor candidata)
        nueva_mejor = (enfermedad_actual, coincidencias)
        resultado = self._buscar_diagnostico(sintomas_paciente, enfermedades, indice_actual + 1, nueva_mejor)
        # (el "retroceso" aqui es implicito: si mas adelante no mejora, resultado sigue siendo nueva_mejor)
        return resultado

    # No es mejor candidata (o no alcanza el minimo): seguimos explorando sin cambiar mejor_actual
    return self._buscar_diagnostico(sintomas_paciente, enfermedades, indice_actual + 1, mejor_actual)