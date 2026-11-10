import requests
import json
import numpy as np
from sklearn.linear_model import LinearRegression

# URL de una API pública de prueba
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # 4. requests: Realizar la petición HTTP a la API
    print("Conectando con la API...")
    response = requests.get(url, timeout=10)
    
    # 3. Manejo de errores: Verificar si la petición fue exitosa (código 200)
    response.raise_for_status()
    
    # 2. Json: Parsear la respuesta de texto a un objeto JSON (lista de diccionarios)
    datos_api = response.json()
    print(f"¡Datos obtenidos con éxito! Total de registros: {len(datos_api)}")
    
    # Preparar los datos para scikit-learn usando una parte de la información de la API
    # Ejemplo: Predecir la longitud del título basándonos en el ID del post
    X = np.array([[item['id']] for item in datos_api[:20]]) # Variable independiente (features)
    y = np.array([len(item['title']) for item in datos_api[:20]]) # Variable dependiente (target)
    
    # scikit-learn: Crear y entrenar el modelo de Regresión Lineal
    modelo = LinearRegression()
    modelo.fit(X, y)
    
    # Realizar una predicción de prueba para el ID 21
    id_a_predecir = [[21]]
    prediccion = modelo.predict(id_a_predecir)
    
    resultado_prediccion = {
        "id_consultado": 21,
        "longitud_titulo_predicha": float(prediccion[0])
    }
    
    print(f"Predicción generada: {resultado_prediccion}")
    
    # 1. Archivos: Guardar el resultado en un archivo JSON local
    nombre_archivo = "resultado_modelo.json"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(resultado_prediccion, archivo, indent=4, ensure_ascii=False)
        print(f"Resultado guardado correctamente en el archivo '{nombre_archivo}'.")

# 3. Manejo de errores específicos
except requests.exceptions.HTTPError as err_http:
    print(f"Error HTTP ocurrido: {err_http}")
except requests.exceptions.ConnectionError:
    print("Error de conexión: Verifica tu conexión a internet.")
except requests.exceptions.Timeout:
    print("La petición a la API ha tardado demasiado tiempo.")
except json.JSONDecodeError:
    print("Error al decodificar la respuesta JSON de la API.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")