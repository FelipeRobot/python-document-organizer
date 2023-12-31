import os
import shutil

extensiones_dict = {
    '.txt' : 'documentos',
    '.docx': 'documentos',
    '.pdf' : 'documentos',
    '.jpg': 'imágenes',
    '.png': 'imágenes',
    '.exe' : 'ejecutable'
}
predeterminated = 'otros'

carpeta_organizar_ruta = r'C:\Users\Felip\Downloads' 
archivos = os.listdir(carpeta_organizar_ruta)

for archivo in archivos:
    archivo_origen_ruta = os.path.join(carpeta_organizar_ruta, archivo)

    if os.path.isfile(archivo_origen_ruta):
        _, extension =os.path.splitext(archivo)
        nombre_carpeta = extensiones_dict.get(extension.lower(), predeterminated)

        archivo_destino_ruta = os.path.join(carpeta_organizar_ruta, nombre_carpeta)

        if not os.path.exists(archivo_destino_ruta):
            os.makedirs(archivo_destino_ruta)
        shutil.move(archivo_origen_ruta, archivo_destino_ruta)