import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_excel("Tienda.xlsx")
print("Datos de los cliente")
print(df)
x = df[["Valor"]]
y = df["Compra"]

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(x, y)
df=input("cuanto dinero ha gastado: ")

cliente= pd.DataFrame({"Valor": [df]})
prediccion = modelo.predict(cliente)

if prediccion[0] == 1:
  print("El cliente puede comprar")
else:
  print("El cliente no puede comprar")