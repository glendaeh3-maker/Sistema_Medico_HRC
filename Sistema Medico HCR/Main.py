"""
MAIN - Sistema Medico Hospital Regional de Cajamarca
Aqui se conecta todo el sistema con un menu simple de consola.
"""
import sys
import os
 
# Esto es para que no tire error al conectar con las otras carpetas del proyecto
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
 
from clases.Paciente import Paciente
from clases.Doctor import Doctor
from clases.Recurso import Recurso
 
from modulos.Cola_Pacientes import agregar_paciente, mostrar_cola, siguiente_paciente
from modulos.Triajes import asignar_triaje_voraz
from modulos.Diagnostico import ArbolDiagnostico
from modulos.Reportes import generar_reporte_optimizacion_dp
from modulos.Recursos import area_mas_colapsada, area_menos_colapsada, total_camas_disponibles, mostrar_resumen_recursos
 
from datos.Datos_Iniciales import doctores_iniciales, capacidad_camas, zonas_procedencia
 
 
# ============================================================
# DATOS EN MEMORIA (mientras el programa esta corriendo)
# ============================================================
cola_pacientes = []          # Lista de pacientes en espera
contador_id = 1              # Para ir dando un ID nuevo a cada paciente
 
# Armamos los doctores iniciales a partir de Datos_Iniciales
lista_doctores = [Doctor(id, nombre, especialidad, turno)
                   for (id, nombre, especialidad, turno) in doctores_iniciales]
 
# Armamos las areas/recursos a partir del diccionario de capacidad_camas
lista_recursos = [Recurso(area, capacidad) for area, capacidad in capacidad_camas.items()]
 
arbol_diagnostico = ArbolDiagnostico()
 
 
# ============================================================
# FUNCIONES DEL MENU (cada una hace una sola cosa, facil de leer)
# ============================================================
 
def registrar_paciente():
    global contador_id
    print("\n--- Registrar nuevo paciente ---")
    nombre = input("Nombre del paciente: ")
    edad = input("Edad: ")
 
    print(f"Zonas de procedencia sugeridas: {zonas_procedencia}")
    procedencia = input("Procedencia: ")
 
    nivel_triaje = input("Nivel de triaje (1=Critico ... 5=Leve): ")
    nivel_triaje = int(nivel_triaje)
 
    paciente = Paciente(contador_id, nombre, edad, procedencia, nivel_triaje)
    contador_id += 1
 
    agregar_paciente(cola_pacientes, paciente)
    print(f"\nPaciente {nombre} registrado y agregado a la cola.")
 
 
def ver_cola():
    mostrar_cola(cola_pacientes)
 
 
def atender_siguiente():
    print("\n--- Atender siguiente paciente ---")
    paciente = siguiente_paciente(cola_pacientes)
    if paciente is None:
        return
 
    # Buscamos un doctor disponible de la misma especialidad si se puede, sino cualquiera libre
    doctor_disponible = None
    for doc in lista_doctores:
        if doc.disponible:
            doctor_disponible = doc
            break
 
    if doctor_disponible is None:
        print("No hay doctores disponibles en este momento.")
        return
 
    doctor_disponible.asignar_paciente(paciente)
    cola_pacientes.remove(paciente)
 
 
def aplicar_triaje_voraz():
    print("\n--- Aplicar Triaje Voraz (Greedy) ---")
    if not cola_pacientes:
        print("No hay pacientes en cola.")
        return
 
    camas_libres = total_camas_disponibles(lista_recursos)
    print(f"Camas disponibles en todo el hospital: {camas_libres}")
 
    atendidos, en_espera = asignar_triaje_voraz(cola_pacientes, camas_libres)
 
    print("\nPacientes que consiguieron cama:")
    for p in atendidos:
        print(f"  -> {p}")
 
    print("\nPacientes que se quedan en espera:")
    for p in en_espera:
        print(f"  -> {p}")
 
 
def diagnosticar_paciente():
    print("\n--- Diagnostico de paciente ---")
    if not cola_pacientes:
        print("No hay pacientes en cola.")
        return
 
    mostrar_cola(cola_pacientes)
    id_paciente = int(input("\nID del paciente a diagnosticar: "))
 
    paciente = next((p for p in cola_pacientes if p.id == id_paciente), None)
    if paciente is None:
        print("No se encontro ese paciente.")
        return
 
    sintomas = input("Ingresa los sintomas separados por coma: ")
    lista_sintomas = [s.strip() for s in sintomas.split(",")]
 
    diagnostico = arbol_diagnostico.evaluar_paciente(lista_sintomas, paciente)
    print(f"\nDiagnostico sugerido para {paciente.nombre}: {diagnostico}")
 
 
def ver_recursos():
    print("\n--- Estado de Areas (Divide y Venceras) ---")
    mostrar_resumen_recursos(lista_recursos)
 
    peor = area_mas_colapsada(lista_recursos)
    mejor = area_menos_colapsada(lista_recursos)
 
    print(f"\nArea MAS colapsada: {peor}")
    print(f"Area MENOS colapsada: {mejor}")
 
 
def generar_reporte():
    print("\n--- Reporte de Optimizacion (Programacion Dinamica) ---")
    if not cola_pacientes:
        print("No hay pacientes en cola.")
        return
 
    tiempo = int(input("Tiempo disponible en minutos: "))
    valor_total, seleccionados = generar_reporte_optimizacion_dp(cola_pacientes, tiempo)
 
    print(f"\nUrgencia total cubierta: {valor_total}")
    print("Pacientes seleccionados para atender en ese tiempo:")
    for p in seleccionados:
        print(f"  -> {p}")
 
 
def ver_doctores():
    print("\n--- Lista de doctores ---")
    for doc in lista_doctores:
        print(f"  {doc}")
 
 
# ============================================================
# MENU PRINCIPAL
# ============================================================
 
def mostrar_menu():
    print("\n" + "=" * 50)
    print(" SISTEMA MEDICO - HOSPITAL REGIONAL DE CAJAMARCA")
    print("=" * 50)
    print("1. Registrar paciente")
    print("2. Ver cola de pacientes")
    print("3. Atender siguiente paciente")
    print("4. Aplicar triaje")
    print("5. Diagnosticar paciente")
    print("6. Ver estado de areas / recursos")
    print("7. Generar reporte")
    print("8. Ver doctores")
    print("0. Salir")
 
 
def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opcion: ")
 
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            ver_cola()
        elif opcion == "3":
            atender_siguiente()
        elif opcion == "4":
            aplicar_triaje_voraz()
        elif opcion == "5":
            diagnosticar_paciente()
        elif opcion == "6":
            ver_recursos()
        elif opcion == "7":
            generar_reporte()
        elif opcion == "8":
            ver_doctores()
        elif opcion == "0":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpcion invalida, intenta de nuevo.")
 
 
if __name__ == "__main__":
    main()
 