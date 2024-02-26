import logging
import psutil

def analizar_espacio(particion="/"):
    # Obtener el uso de la partición
    espacio = psutil.disk_usage(particion)
    porcentaje_ocupado = espacio.percent

    # Configurar el logging
    logging.basicConfig(filename='/home/fran/Escritorio/logs/espacio_2.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Determinar el nivel de logging según el porcentaje de espacio ocupado
    if porcentaje_ocupado > 80:
        logging.error(f"El espacio en la partición {particion} está por encima del 80% de uso.")
    elif porcentaje_ocupado > 60:
       logging.warning(f"El espacio en la partición {particion} está por encima del 60% y por debajo del 80% de uso.")
    else:
        logging.info(f"El espacio en la partición {particion} está por debajo del 60% de uso.")

if __name__ == "__main__":
    analizar_espacio()
