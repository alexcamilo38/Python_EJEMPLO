import json
from datetime import datetime
import requests

# Dirección web de la API del clima de Open-Meteo
URL_API_CLIMA = "https://api.open-meteo.com/v1/forecast"


def interpretar_codigo_clima(codigo: int) -> str:
    """Traduce los números raros que manda la API (códigos meteorológicos)

    a palabras que cualquier persona pueda entender fácilmente.
    """
    codigos_wmo = {
        0: "Despejado",
        1: "Mayormente despejado",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Neblina",
        51: "Llovizna ligera",
        61: "Lluvia ligera",
        63: "Lluvia moderada",
        65: "Lluvia fuerte",
        80: "Chubascos",
        95: "Tormenta eléctrica",
    }
    # Si la API devuelve un código que no tenemos aquí, regresamos algo genérico
    return codigos_wmo.get(codigo, "Variable")


def obtener_pronostico_hoy_y_manana(latitud: float, longitud: float) -> dict:
    """Le pedimos a la API el pronóstico exclusivo para 2 días

    (lo que dura hoy y lo que pasará mañana).
    """
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        # Aquí pedimos las temperaturas, la lluvia esperada y el estado del cielo por día
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max,weather_code",
        "timezone": "America/Bogota",
        "forecast_days": 2,
    }

    # Hacemos la petición y nos aseguramos de que no haya fallado
    respuesta = requests.get(URL_API_CLIMA, params=parametros, timeout=10)
    respuesta.raise_for_status()

    return respuesta.json()


def guardar_en_json(datos: dict, nombre_archivo: str = "pronostico_hoy_manana.json") -> None:
    """Agarra toda la información que procesamos y la guarda ordenadita

    en un archivo JSON en tu computadora.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def predecir_hoy_y_manana(ciudad: str, latitud: float, longitud: float):
    """Función principal: organiza todo el proceso de consulta,

    lectura en pantalla y guardado del archivo.
    """
    try:
        print(f"Buscando el clima actual para {ciudad}...")
        datos = obtener_pronostico_hoy_y_manana(latitud, longitud)

        diario = datos["daily"]
        etiquetas = ["HOY", "MANANA"]
        predicciones = []

        # Recorremos los dos días que nos devolvió la API para darles forma
        for i in range(len(etiquetas)):
            info_dia = {
                "etiqueta": etiquetas[i],
                "fecha": diario["time"][i],
                "temperatura_maxima": diario["temperature_2m_max"][i],
                "temperatura_minima": diario["temperature_2m_min"][i],
                "probabilidad_lluvia_max": diario["precipitation_probability_max"][i],
                "total_lluvia_mm": diario["precipitation_sum"][i],
                "estado_clima": interpretar_codigo_clima(diario["weather_code"][i]),
            }
            predicciones.append(info_dia)

        # Armamos el paquete final con la fecha y hora en que consultamos
        resultado_final = {
            "ciudad": ciudad,
            "fecha_consulta": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "pronostico": predicciones,
        }

        # Mostramos los resultados directo en la consola para que los leas rápido
        for p in predicciones:
            print(f"\n{p['etiqueta']} ({p['fecha']})")
            print(f"Estado: {p['estado_clima']}")
            print(f"Temp. Maxima: {p['temperatura_maxima']} C")
            print(f"Temp. Minima: {p['temperatura_minima']} C")
            print(f"Probabilidad de Lluvia: {p['probabilidad_lluvia_max']}%")
            print(f"Total Lluvia Estimada: {p['total_lluvia_mm']} mm")

        # Guardamos el respaldo en el archivo JSON
        guardar_en_json(resultado_final)
        print("\nDatos guardados ")

    # Si algo sale mal con el internet o la API, caemos aquí
    except requests.exceptions.RequestException as error:
        print(f"Uy, hubo un problema de conexion con la API: {error}")
    # Si la estructura de los datos cambió o falló al leerlos
    except (KeyError, ValueError) as error:
        print(f"Tuvimos un problema leyendo la informacion: {error}")
    # Si hubo problemas creando o escribiendo el archivo en disco
    except IOError as error:
        print(f"No pudimos guardar el archivo localmente: {error}")


# Punto de arranque de nuestro script
if __name__ == "__main__":
    predecir_hoy_y_manana(ciudad="Medellin", latitud=6.2518, longitud=-75.5636)