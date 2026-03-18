import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

data = response.json()
df = pd.DataFrame(data)

# Análisis: longitud de contenido
df["length"] = df["body"].apply(len)

# Top usuarios con más contenido
top_users = df.groupby("userId")["length"].sum().sort_values(ascending=True)

print("Top usuarios con más contenido:\n")
print(top_users)

# Visualización
top_users.plot(kind="bar")
plt.title("Usuarios más activos (por contenido)")
plt.xlabel("Usuario")
plt.ylabel("Cantidad de texto")
plt.show()