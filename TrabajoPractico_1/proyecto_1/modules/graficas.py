import io
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as plt

def generar_graficas(datos_usuarios):
    """
    Genera gráficas a partir de los datos de los usuarios.

    Args:
        datos_usuarios (list): Lista de listas con los datos de los usuarios.
    """

    nombres_usuario = []
    puntuaciones = []

    for usuario in datos_usuarios:
        # Verificar que el usuario tenga al menos dos elementos
        if len(usuario) >= 1:
            nombres_usuario.append(usuario[0])
            puntuaciones.append(usuario[1], default=0)

    # Convertir las puntuaciones a enteros
    puntuaciones = [int(p) for p in puntuaciones]


    # Gráfica de barras: Distribución de puntuaciones
    plt.figure()
    plt.bar(nombres_usuario, puntuaciones)
    plt.xlabel("Usuario")
    plt.ylabel("Puntuación")
    plt.title("Distribución de puntuaciones")

    # Gráfica de pastel: Porcentaje de usuarios por rango de puntuación
    rangos_puntuacion = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50)]
    conteo_rangos = [0] * len(rangos_puntuacion)
    for puntuacion in puntuaciones:
        for i, rango in enumerate(rangos_puntuacion):
            if puntuacion >= rango[0] and puntuacion <= rango[1]:
                conteo_rangos[i] += 1

    porcentajes_rangos = [round((conteo/len(datos_usuarios))*100, 2) for conteo in conteo_rangos]

    plt.figure()
    plt.pie(porcentajes_rangos, labels=[f"{r[0]}-{r[1]}" for r in rangos_puntuacion])
    plt.title("Porcentaje de usuarios por rango de puntuación")

    # Guardar las gráficas en un archivo PDF en memoria
    pdf_buffer = io.BytesIO()
    with PdfPages(pdf_buffer) as pdf:
        for _ in plt.get_fignums():
            pdf.savefig()

    # Reiniciar la figura actual de matplotlib para evitar errores
    plt.close('all')

    # Mover el cursor al principio del archivo PDF en memoria
    pdf_buffer.seek(0)

    return pdf_buffer
