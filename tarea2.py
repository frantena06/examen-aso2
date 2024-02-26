import psutil

def obtener_porcentaje_uso():
    
    particiones = psutil.disk_partitions()

    for particion in particiones:
        try:

            espacio_usado = psutil.disk_usage(particion.mountpoint).percent
           
            particion_device = particion.device.replace('\\', '/')
        
            print(f"{particion_device} {espacio_usado:.1f}%")
        except Exception as e:
            print(f"No se pudo obtener el porcentaje de uso para {particion.device}: {str(e)}")

if __name__ == "__main__":
    print("Porcentaje de espacio ocupado en cada particion:")
    obtener_porcentaje_uso()
