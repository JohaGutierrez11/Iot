import requests
import pandas as pd
import matplotlib.pyplot as plt

#url para extraer datos
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

#Contar post por usuario
post_by_user = df["userId"].value_counts()
id_user = df["id"]
print(post_by_user)


# Gráfico
post_by_user.plot(kind="bar")
plt.title("Posts por usuario")
plt.xlabel("Usuario")
plt.ylabel("Cantidad")
plt.show()