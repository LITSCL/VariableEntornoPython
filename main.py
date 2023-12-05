#1. Importar librerías necesarias.
import os
from dotenv import load_dotenv

#2. Cargar variables de entorno desde el archivo .env.
load_dotenv()

#3. Asignar variables de entorno a variables.
nombre: str = os.getenv("MI_NOMBRE")
apellido: str = os.getenv("MI_APELLIDO")
edad: str = os.getenv("MI_EDAD")

#4. Utilizar variables de entorno.
print(nombre)
print(apellido)
print(edad)