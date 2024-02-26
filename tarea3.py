import os

def crear_carpetas_y_ficheros():
    escritorio = '/home/fran/Escritorio'

    for i in range(1, 6):
        carpeta = os.path.join(escritorio, f"folder{i}")
        os.makedirs(carpeta, exist_ok=True)
        
        for j in range(1, 11):
            fichero = os.path.join(carpeta, f"fichero{j}.txt")
            with open(fichero, 'w') as f:
                f.write(f"Este es el contenido del fichero {j}")

if __name__ == "__main__":
    crear_carpetas_y_ficheros()
