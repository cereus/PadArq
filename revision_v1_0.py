# Módulo:       revision_v1_0.py
# Propósito:    Revisa factores de diseño arquitectónico para trámite de permisos de construcción
# Versión:      1.0
# Autor:        Angel Flores Chávez
# Fecha:        27-04-2016

#afc Implementar funciones para reducir el código --> OK
#afc Escribir una rutina para mostrar los parámetros de diseño --> OK
#afc Escribir una rutina para imprimir archivo de texto --> OK

import os
os.system("cls")

# Introducción
print('''
+---------------------------------------------------------------+
| Revisión de parámetros de diseño de proyectos arquitectónicos |
| para factores COS, CUS y CAS utlizados en trámites de permi-  |
| sos de construcción para el municipio de Saltillo, Coah. Mx.  |
| ------------------------------------------------------------- |
| Versión: 1.0                                                  |
| Fecha: 27-04-2016                                             |
| Autor: Angel Flores Chávez                                    |
+---------------------------------------------------------------+
''')

# Define los factores de revisión
print('+---------------------------------------------------------------+')
print('| Factores de revisión:                                         |')
print('+---------------------------------------------------------------+')
# Factor COS
while True:
    try:
        factCOS = float(input('\tFactor COS --> '))
    except ValueError:
        print('\t¡El dato debe ser numérico!')
        continue
    else:
        break

# Factor CUS
while True:
    try:
        factCUS = float(input('\tFactor CUS --> '))
    except ValueError:
        print('\t¡El dato debe ser numérico!')
        continue
    else:
        break

# Factor CAS
while True:
    try:
        factCAS = float(input('\tFactor CAS --> '))
    except ValueError:
        print('\t¡El dato debe ser numérico!')
        continue
    else:
        break

# Define los datos del proyecto
print('+---------------------------------------------------------------+')
print('| Datos del proyecto (m2):                                      |')
print('+---------------------------------------------------------------+')
# Superficie de terreno
while True:
    try:
        terreno = float(input('\tSuperficie de terreno --> '))
    except ValueError:
        print('\t¡El dato debe ser numérico!')
        continue
    else:
        break

# Superficie de construcción
while True:
    try:
        construccion = float(input('\tSuperficie de construcción total --> '))
    except ValueError:
        print('\t¡El dato debe ser numérico!')
        continue
    else:
        break

# Superficie de contacto
while True:
    try:
        pb = float(input('\tSuperficie de contacto con el terreno --> '))
    except ValueError:
        print('\t¡El dato debe ser numérico!')
        continue
    else:
        break

# Superficie de absorción
while True:
    try:
        absor = float(input('\tSuperficie de absorción de jardines --> '))
    except ValueError:
        print('\t¡El dato debe ser numérico!')
        continue
    else:
        break

# Operaciones
COS = terreno * factCOS
CUS = construccion / terreno
CAS = terreno * factCAS

# Presenta los resultados
print('+---------------------------------------------------------------+')
print('++-------------------------------------------------------------++')
print('||                    TABLA DE RESULTADOS                      ||')
print('++-------------------------------------------------------------++')
print('+---------------------------------------------------------------+')
print('| Parámetro\tProyecto\tCalculado\tEstado\t\t|')
print('+---------------------------------------------------------------+')

# Comparativo COS
if COS >= pb:
    print('| COS      \t', pb, '    \t', round(COS, 2), '\t\tOk\t\t|')
    print('+---------------------------------------------------------------+')

else:
    print('| COS      \t', pb, '    \t', round(COS, 2), '\t\tRevisar\t\t|')
    print('+---------------------------------------------------------------+')

# Comparativo CUS
if CUS <= factCUS:
    print('| CUS      \t', round(CUS, 2), '    \t', factCUS, '\t\tOk\t\t|')
    print('+---------------------------------------------------------------+')
else:
    print('| CUS      \t', round(CUS, 2), '    \t', factCUS, '\t\tRevisar\t\t|')
    print('+---------------------------------------------------------------+')

# Comparativo CAS
if CAS <= absor:
    print('| CAS      \t', round(absor, 2), '    \t', CAS, '\t\tOk\t\t|')
    print('+---------------------------------------------------------------+')
else:
    print('| CAS      \t', round(absor, 2), '    \t', CAS, '\t\tRevisar\t\t|')
    print('+---------------------------------------------------------------+')

print('\nPara SALIR del programa:')
os.system("pause")

# Fin del programa
