"""
    INFORMACIÓN DEL PROGRAMA:

    Módulo:       revision_v1_1.py
    Propósito:    Revisa factores de diseño arquitectónico para trámite de permisos de construcción
    Versión:      1.1 CMD
    Autor:        Angel Flores Chávez
    Fecha:        03-05-2016
"""

#afc Pasar a versión Windows --> OK

# Importar módulos necesarios
import datetime
import os
import subprocess

from tabulate import tabulate

os.system("cls")

# INTRODUCCIÓN
print('''
+----------------------------------------------------------------------------------+
| Revisión de parámetros de diseño de proyectos arquitectónicos para factores COS, |
| CUS y CAS utilizados en trámites de permisos de construcción para el municipio   |
| de Saltillo, Coah. Mx.                                                           |
| -------------------------------------------------------------------------------- |
| Versión: 1.1 CMD                                                                 |
| Fecha:   03-05-2016                                                              |
| Autor:   Angel Flores Chávez                                                     |
+----------------------------------------------------------------------------------+
''')

# ASIGNA VALORES INICIALES A LAS VARIABLES SOLO PARA COMPROBAR QUE SEAN NUMÉRICOS
a1 = 0  # Solo se asigna el primero, pues todos los valores cambiarán después
yy = datetime.date.today().year
mm = datetime.date.today().month
dd = datetime.date.today().day

# Se asignan las etiquetas a utilizar
iCOS = '\tFactor COS --> '
iCUS = '\tFactor CUS --> '
iCAS = '\tFactor CAS --> '
iTer = '\tSuperficie total del terreno --> '
iCon = '\tSuperficie total del construcción --> '
iKtk = '\tSuperficie de contacto --> '
iAbs = '\tSuperficie de absorción --> '
iPry = '\tNombre del proyecto --> '
iCli = '\tNombre del cliente  --> '
tHoy = '\tFecha               --> ' + str(dd) + '/' + str(mm) + '/' + str(yy) + '\n'


# FUNCIÓN PARA REVISAR QUE TODOS LOS VALORES INTRODUCIDOS SEAN NUMÉRICOS
def not_float(anydata, anytxt):
    global a1, a2, a3, b1, b2, b3, b4
    while True:
        try:
            a1 = a2 = a3 = b1 = b2 = b3 = b4 = float(input(anydata))
        except ValueError:
            print('Error: El valor debe ser numérico. Intenta de nuevo.')
            continue
        else:
            return a1, a2, a3, b1, b2, b3, b4
            break


# FUNCIÓN PARA GUARDAR EL REPORTE EN ARCHIVO
def reporte():
    global stat_cos, stat_cas, stat_cus, coeficientes, tabla, tablad

    f = open('reporte_cmd.txt', 'w+')

    f.write('''
+----------------------------------------------------------------------------------+
| Revisión de parámetros de diseño de proyectos arquitectónicos para factores COS, |
| CUS y CAS utilizados en trámites de permisos de construcción para el municipio   |
| de Saltillo, Coah. Mx.                                                           |
| -------------------------------------------------------------------------------- |
| Versión: 1.1 CMD                                                                 |
| Fecha:   03-05-2016                                                              |
| Autor:   Angel Flores Chávez                                                     |
+----------------------------------------------------------------------------------+
    ''')

    f.write('\n\n')
    f.write('+----------------------------------------------------------------------------------+\n')
    f.write('|                                   DATOS GENERALES                                |\n')
    f.write('+----------------------------------------------------------------------------------+\n')
    f.write('')
    f.write(tPry)
    f.write(tCli)
    f.write(tHoy)
    f.write('\n')

    f.write('+----------------------------------------------------------------------------------+\n')
    f.write('|                                 TABLA DE RESULTADOS                              |\n')
    f.write('+----------------------------------------------------------------------------------+\n')
    f.write(tabla)
    f.write('\n')
    f.write('+----------------------------------------------------------------------------------+')

    # Parámetros de Diseño
    f.write('\n\n')
    f.write('+----------------------------------------------------------------------------------+\n')
    f.write('|                                PARÁMETROS DE DISEÑO                              |\n')
    f.write('+----------------------------------------------------------------------------------+\n')
    f.write(tablad)
    f.write('\n\n')
    f.write('\tNOTA:\n'
            '\tLos parámetros de diseño se comparan de la siguiente manera:\n'
            '\tCOS --> Calculado >= Proyecto = Correcto\n'
            '\tCAS --> Calculado <= Proyecto = Correcto\n'
            '\tCUS --> Calculado >= Proyecto = Correcto\n'
            )
    f.write('\n')
    f.write('\t<-- Fin del Reporte -->')
    f.write('\n')

    f.close()


# DEFINE LOS FACTORES DE REVISIÓN
print('+----------------------------------------------------------------------------------+')
print('| Define los factores de revisión:                                                 |')
print('+----------------------------------------------------------------------------------+')

not_float(iCOS, a1)  # Factor COS
COS = a1  # Reasigna el valor a una nueva variable
not_float(iCAS, a3)  # Factor CAS
CAS = a3  # Reasigna el valor a una nueva variable
not_float(iCUS, a2)  # Factor CUS
CUS = a2  # Reasigna el valor a una nueva variable

# DEFINE LOS DATOS DEL PROYECTO
print('+----------------------------------------------------------------------------------+')
print('| Define los datos del proyecto:                                                   |')
print('+----------------------------------------------------------------------------------+')

# Datos generales
nPry = input(iPry)
tPry = str(iPry + nPry + '\n')
nCli = input(iCli)
tCli = str(iCli + nCli + '\n')

# Datos de diseño
not_float(iTer, b1)  # Superficie del terreno
sTer = b1  # Reasigna el valor a una nueva variable
not_float(iCon, b2)  # Superficie total de construcción
sCon = b2  # Reasigna el valor a una nueva variable
not_float(iKtk, b3)  # Superficie de contacto
sKtk = b3  # Reasigna el valor a una nueva variable
not_float(iAbs, b4)  # Superficie de absorción
sAbs = b4  # Reasigna el valor a una nueva variable

# REALIZA LAS OPERACIONES CON LOS DATOS REVISADOS
rvCOS = COS * sTer
rvCUS = sCon / sTer
rvCAS = CAS * sTer

if rvCOS >= sKtk:
    stat_cos = 'Correcto'
else:
    stat_cos = 'Revisar'

if rvCAS <= sAbs:
    stat_cas = 'Correcto'
else:
    stat_cas = 'Revisar'

if rvCUS <= CUS:
    stat_cus = 'Correcto'
else:
    stat_cus = 'Revisar'

# MUESTRA LA TABLA DE RESULTADOS
os.system("cls")
print()
print('+----------------------------------------------------------------------------------+')
print('|                                 TABLA DE RESULTADOS                              |')
print('+----------------------------------------------------------------------------------+')

coeficientes = [['Ocupación de Superficie   (COS)', COS, rvCOS, sKtk, stat_cos],
                ['Absorción de Superficie   (CAS)', CAS, rvCAS, sAbs, stat_cas],
                ['Utilización de Superficie (CUS)', CUS, CUS, rvCUS, stat_cus]]
tabla = tabulate(coeficientes, headers=['Coeficiente', 'Factor', 'Calculado', 'Proyecto', 'Estado'],
                 tablefmt='orgtbl', numalign='right', floatfmt='8.2f')
datos_pry = [['Sup. de Terreno', sTer], ['Sup. de Construcción', sCon], ['Sup. de Contacto', sKtk],
             ['Sup. de Absorción', sAbs]]
tablad = tabulate(datos_pry, numalign='right', floatfmt='8.2f')
print(tabla)
print('+----------------------------------------------------------------------------------+')

# Parámetros de diseño
print()
print('+----------------------------------------------------------------------------------+')
print('|                                  PARÁMETROS DE REVISIÓN                          |')
print('+----------------------------------------------------------------------------------+')
print()
print(tablad)
print()
print('\tNOTA:\n'
      '\tLos parámetros de diseño se comparan de la siguiente manera:\n'
      '\tCOS --> Calculado >= Proyecto = Correcto\n'
      '\tCAS --> Calculado <= Proyecto = Correcto\n'
      '\tCUS --> Calculado >= Proyecto = Correcto\n'
      )

# GUARDA EL REPORTE EN UN ARCHIVO
reporte()

# AVISO
print('\n\tNOTA: Se creó el archivo reporte_cmd.txt dentro de la carpeta\n'
      '\tdel programa para consultar los resultados.\n\n'
      '\tCada vez que se crea un archivo de reporte, el nuevo sustituye\n'
      '\tal anterior.\n'
      '\tPara conservar el actual, renombra el archivo o cámbialo\n'
      '\tde ubicación.\n'
      )

# ABRIR CON BLOC DE NOTAS
resp = input('\n\tDeseas abrir el reporte (S/N)? --> ')
if resp == 'S' or resp == 's':
    txtfile = "reporte_cmd.txt"
    notepadPath = r'C:\WINDOWS\system32\notepad.exe'
    subprocess.Popen("%s %s" % (notepadPath, txtfile))
else:
    print('\n\t** NO SE ABRIRÁ EL ARCHIVO DE REPORTE **')

# FIN DEL PROGRAMA
print('\nPara SALIR del programa:')
os.system("pause")
