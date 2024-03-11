
# usar datetime para mostrar la fecha y hora actuales


import datetime
fecha_hora_actual=datetime.datetime.now()

formato= "%d/%m/%Y %H:%m"
fecha_hora_formato=fecha_hora_actual.strftime(formato)

print("fecha y hora actuales: ", fecha_hora_formato)