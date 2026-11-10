import json
import requests
import numpy as np
from sklearn.linear_model import LogisticRegression

# API del clima
URL = "https://api.open-meteo.com/v1/forecast"


def consultar_y_predecir_clima():
  try:
    # coordenadas
    ciudad = "Popayan"
    latitud = 2.4419
    longitud = -76.6063

    # Consultar la API del clima
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "hourly": "temperature_2m,relative_humidity_2m,precipitation_probability",
        "timezone": "America/Bogota",
    }

    print("Consultando la API del clima...")
    respuesta = requests.get(URL, params=parametros, timeout=10)
    respuesta.raise_for_status()

    datos = respuesta.json()
    
    # Extraemos datos actuales y las probabilidades de lluvia horarias
    temperatura_actual = datos["hourly"]["temperature_2m"][0]
    humedad_actual = datos["hourly"]["relative_humidity_2m"][0]
    prob_lluvia_lista = datos["hourly"]["precipitation_probability"]

    horas_entrenamiento = 24
    X = np.array([[i] for i in range(horas_entrenamiento)])
    y = np.array([1 if p > 40 else 0 for p in prob_lluvia_lista[:horas_entrenamiento]])

    try:
      # para saber si lloverá
      modelo = LogisticRegression()
      modelo.fit(X, y)
      prediccion_ml = modelo.predict([[24]])[0]
    except Exception:
      
      prediccion_ml = 1 if prob_lluvia_lista[24] > 40 else 0

    # Interpretamos la prediccion
    va_a_llover = "Si" if prediccion_ml == 1 else "No"
    probabilidad_siguiente_hora = prob_lluvia_lista[24]

    resultado = {
        "ciudad": ciudad,
        "temperatura_actual": temperatura_actual,
        "humedad_actual": humedad_actual,
        "probabilidad_lluvia_siguiente_hora": f"{probabilidad_siguiente_hora}%",
        "prediccion_scikit_learn_va_a_llover": va_a_llover,
        "unidad_temperatura": "°C",
        "unidad_humedad": "%"
    }

    print("\n informacion del clima :")
    print("Ciudad:", resultado["ciudad"])
    print("Temperatura Actual:", resultado["temperatura_actual"], "°C")
    print("Humedad Actual:", resultado["humedad_actual"], "%")
    print("Probabilidad de Lluvia:", resultado["probabilidad_lluvia_siguiente_hora"])
    print("Va a llover: ", resultado["prediccion_scikit_learn_va_a_llover"])

    # 3. JSON
    with open("clima_lluvia.json", "w", encoding="utf-8") as archivo:
      json.dump(resultado, archivo, indent=4, ensure_ascii=False)

    print("\nDatos y predicción guardados en clima_lluvia.json")

  # 4. MANEJO DE ERRORES
  except requests.exceptions.RequestException as error:
    print("Error al consultar la API:", error)

  except (KeyError, ValueError, json.JSONDecodeError) as error:
    print("Error al procesar los datos:", error)


consultar_y_predecir_clima()