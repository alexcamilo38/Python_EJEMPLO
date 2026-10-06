import pandas as pd
df=pd.read_excel("Prueba.xlsx")
mayores_25 = df[df["edad"]>=25]
print(mayores_25)