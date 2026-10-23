#Desarrollo Taller 
#Para Ejecutar este taller instalamos 

# 1. PANDAS: pip install pandas
# 2. SCIKIT-LEARN: pip install scikit-learn


import pandas as pd
from sklearn.preprocessing import MinMaxScaler #para el punto 10

df = pd.read_csv("datos_para_limpiar.csv")

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#print(df.head())# las primeras filas

# Mostrar la información general del DataFrame
#print(df.info())#todos los datos 

#print(df.isnull().sum())#ver valores nulos por colm

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#2.
# Elimina las columnas ID y Notas.

#df = df.drop(columns=["ID", "Notas"])

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#3.
# #Renombra las columnas para que estén en minúsculas, sin espacios y sin tildes.

#df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("á", "a").str.replace("é", "e")

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#4.
# #Unifica los valores de la columna ciudad.
#df["ciudad"] = df["ciudad"].str.strip().str.lower().replace({"bogotá": "bogota", "medellín": "medellin", "cali": "cali"})

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#5.
# #manejo de valores faltantes según reglas

# Rplz val nulos en la colum edad con la media
#df["edad"] = df["edad"].fillna(df["edad"].mean())

# Rplz val nulos en la colum salario con la mediana
#df["salario"] = df["salario"].fillna(df["salario"].median())

# Rplz val nulos en las colum ciudad y genero con la moda
#df["ciudad"] = df["ciudad"].fillna(df["ciudad"].mode()[0])
#df["genero"] = df["genero"].fillna(df["genero"].mode()[0])

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#6.
# Convierte las columnas edad y fecha a sus tipos correctos.

# Conv la columna edad a tipo num
#df["edad"] = pd.to_numeric(df["edad"], errors='coerce')

# Convla columna fecha a formato de fecha
#df["fecha"] = pd.to_datetime(df["fecha"], errors='coerce')

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#7.
#Elimina registros con edades fuera del rango 0–120 años y salarios mayores a 1.000 millones.
# Filtrar datos fuera de rango

#df = df[(df["edad"].between(0, 120)) & (df["salario"] <= 1_000_000_000)]

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#8.
#Convierte la columna nivel a valores numéricos según la siguiente escala:
# bajo → 1
# medio → 2
# alto → 3

#orden = {"bajo": 1, "medio": 2, "alto": 3}
#df["nivel"] = df["nivel"].map(orden)

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#9.
#Convierte las variables categóricas genero y ciudad a variables numéricas utilizando
#pd.get_dummies, eliminando la primera categoría para evitar multicolinealidad.

#df = pd.get_dummies(df, columns=["genero", "ciudad"], drop_first=True)

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#10.
#Escala las columnas edad e ingresos a un rango entre 0 y 1, utilizando MinMaxScaler.

#scaler = MinMaxScaler()
#df[["edad", "ingresos"]] = scaler.fit_transform(df[["edad", "ingresos"]])

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#11.
#Elimina las filas duplicadas que existan en el dataset.
# Eliminar registros duplicados

#df = df.drop_duplicates()

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#12.
#Agrega una nueva columna llamada utilidad, calculada como:
#utilidad = ingresos - gastos

#df["utilidad"] = df["ingresos"] - df["gastos"]

#"::::::::::::::SEPARADOR :::::::::::::::::::::::"

#13.
#Exporta el DataFrame final a un archivo llamado:datos_limpios.csv

#df.to_csv("datos_limpios.csv", index=False)

#"::::::::::::::THE END :::::::::::::::::::::::"

