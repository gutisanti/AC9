from typing import Tuple
import math

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperatura_total = 0
        humedad_total = 0
        presion_total = 0
        velocidad_viento_total = 0
        direccion_viento_grados = []
        direccion_viento_map = {
            "N": 0,
            "NNE": 22.5,
            "NE": 45,
            "ENE": 67.5,
            "E": 90,
            "ESE": 112.5,
            "SE": 135,
            "SSE": 157.5,
            "S": 180,
            "SSW": 202.5,
            "SW": 225,
            "WSW": 247.5,
            "W": 270,
            "WNW": 292.5,
            "NW": 315,
            "NNW": 337.5
        }

        with open(self.nombre_archivo, 'r') as file:
            for line in file:
                if line.startswith("Temperatura:"):
                    temperatura = float(line.split(":")[1].strip())
                    temperatura_total += temperatura
                elif line.startswith("Humedad:"):
                    humedad = float(line.split(":")[1].strip())
                    humedad_total += humedad
                elif line.startswith("Presión:"):
                    presion = float(line.split(":")[1].strip())
                    presion_total += presion
                elif line.startswith("Viento:"):
                    viento_info = line.split(":")[1].strip()
                    velocidad, direccion = viento_info.split(',')
                    velocidad_viento_total += float(velocidad)
                    direccion_viento_grados.append(direccion_viento_map[direccion])

        # Calcular las estadísticas
        num_registros = len(direccion_viento_grados)
        temperatura_promedio = temperatura_total / num_registros
        humedad_promedio = humedad_total / num_registros
        presion_promedio = presion_total / num_registros
        velocidad_viento_promedio = velocidad_viento_total / num_registros

        # Calcular la dirección predominante del viento
        direccion_promedio_grados = sum(direccion_viento_grados) / num_registros
        direccion_promedio = ""
        for dir, dir_grados in direccion_viento_map.items():
            if math.isclose(direccion_promedio_grados, dir_grados, abs_tol=11.25):
                direccion_promedio = dir
                break

        return (
            temperatura_promedio,
            humedad_promedio,
            presion_promedio,
            velocidad_viento_promedio,
            direccion_promedio
        )

# Ejemplo de uso
archivo_meteorologico = "datos_meteorologicos.txt"
datos = DatosMeteorologicos(archivo_meteorologico)
estadisticas = datos.procesar_datos()
print("Temperatura promedio:", estadisticas[0])
print("Humedad promedio:", estadisticas[1])
print("Presión promedio:", estadisticas[2])
print("Velocidad del viento promedio:", estadisticas[3])
print("Dirección predominante del viento:", estadisticas[4])
