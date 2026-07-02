import sys
import os

# Esto es para que no tire error al conectar con las otras carpetas del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datos.Datos_Iniciales import patologias_frecuentes


class ArbolDiagnostico:
    def __init__(self):
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
        enfermedades = list(self.base_conocimiento.keys())

        mejor_diagnostico = self._buscar_diagnostico(
            sintomas_presentados,
            enfermedades,
            indice_actual=0,
            mejor_actual=None
        )

        return mejor_diagnostico if mejor_diagnostico else "Indeterminado"

    def _buscar_diagnostico(self, sintomas_paciente, enfermedades, indice_actual, mejor_actual):
        """
        Recursividad + backtracking:
        revisa todas las enfermedades y se queda con la que tenga más coincidencias.
        """
        if indice_actual >= len(enfermedades):
            return mejor_actual[0] if mejor_actual else None

        enfermedad_actual = enfermedades[indice_actual]
        sintomas_de_enfermedad = self.base_conocimiento.get(enfermedad_actual, [])

        coincidencias = sum(
            1 for sintoma in sintomas_paciente
            if sintoma.lower().strip() in sintomas_de_enfermedad
        )

        if coincidencias >= 2 and (mejor_actual is None or coincidencias > mejor_actual[1]):
            mejor_actual = (enfermedad_actual, coincidencias)

        return self._buscar_diagnostico(
            sintomas_paciente,
            enfermedades,
            indice_actual + 1,
            mejor_actual
        )

