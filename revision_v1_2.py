"""
    INFORMACIÓN DEL PROGRAMA:

    Módulo:       revision_v1_2.py
    Propósito:    Revisa factores de diseño arquitectónico para trámite de permisos de construcción
    Versión:      1.2 Windows 10
    Autor:        Angel Flores Chávez
    Fecha:        06-05-2016
"""

from tkinter import *  # Importar funciones para crear ventanas
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tabulate import tabulate
import datetime
import subprocess  # Incluir para abrir archivos desde su aplicación


def infobox():  # Botón info...
    messagebox.showinfo(message='Módulo:\t\tPadArq Win\n'
                                'Versión:\t\t1.2 Windows\n'
                                'Autor:\t\tAngel Flores Chávez\n'
                                'Fecha:\t\t03-05-2016\n'
                                '\nDescripción:\n'
                                'Revisa factores de diseño arquitectónico para trámite de permisos de construcción '
                                'en la cuidad de Saltillo, Coah. Mx.\n\n'
                                '\nLos parámetros de diseño se comparan de la siguiente manera:\n\n'
                                '     COS --> Calculado >= Proyecto = Correcto\n'
                                '     CAS --> Calculado <= Proyecto = Correcto\n'
                                '     CUS --> Calculado >= Proyecto = Correcto',
                                title='Acerca de PadARQ Win'
                        )


def rep(*args):  # Botón de Reporte
    np = n_proy.get()  # Nombre del proyecto
    PryTxt = '\tNombre del proyecto  --> ' + np + '\n'
    nc = n_cli.get()   # Nombre del cliente
    PryCli = '\tNombre del cliente   --> ' + nc + '\n'
    yy = datetime.date.today().year  # Fecha de hoy
    mm = datetime.date.today().month
    dd = datetime.date.today().day
    PryHoy = '\tFecha                --> ' + str(dd) + '/' + str(mm) +'/' + str(yy) + '\n'

    # Definición de tabla
    coeficientes = [['Ocupación de Superficie   (COS)', dsp_f_cos.get(), dsp_cos.get(),
                     dsp_s_cont.get(), stat_cos.get()],
                    ['Absorción de Superficie   (CAS)', dsp_f_cas.get(), dsp_cas.get(),
                     dsp_s_abso.get(), stat_cos.get()],
                    ['Utilización de Superficie (CUS)', dsp_f_cus.get(), dsp_f_cus.get(),
                     dsp_cus.get(), stat_cus.get()]]
    tabla = tabulate(coeficientes, headers=['Coeficiente', 'Factor', 'Calculado', 'Proyecto', 'Estado'],
                     tablefmt='orgtbl', numalign='right')
    datos_pry = [['Sup. de Terreno', s_ter.get()], ['Sup. de Construcción', s_cons.get()],
                 ['Sup. de Contacto', s_cont.get()], ['Sup. de Absorción', s_abso.get()]]
    tablad = tabulate(datos_pry, tablefmt='orgtbl', numalign='right', floatfmt='8.2f')

    f = open('reporte.txt', 'w+')

    f.write('\n'
            '------------------------------------------------------------------------------------\n'
            'Revisión de parámetros de diseño de proyectos arquitectónicos para factores COS,\n'
            'CUS y CAS utilizados en trámites de permisos de construcción para el municipio de\n'
            'Saltillo, Coah. Mx.\n'
            '------------------------------------------------------------------------------------\n'
            '\tVersión: 1.2 Win\n'
            '\tFecha  : 03-05-2016\n'
            '\tAutor  : Angel Flores Chávez\n'
            '------------------------------------------------------------------------------------\n')

    f.write('\n\n')
    f.write('------------------------------------------------------------------------------------\n')
    f.write('\tDATOS GENERALES\n')
    f.write('------------------------------------------------------------------------------------\n')
    f.write('\n')
    f.write(PryTxt)
    f.write(PryCli)
    f.write(PryHoy)
    f.write('\n\n')
    f.write('------------------------------------------------------------------------------------\n')
    f.write('\tPARÁMETROS DE DISEÑO\n')
    f.write('------------------------------------------------------------------------------------\n')
    f.write(tablad)
    f.write('\n\n\n')
    f.write('+----------------------------------------------------------------------------------+\n')
    f.write('|\tTABLA DE RESULTADOS                                                        |\n')
    f.write('+----------------------------------------------------------------------------------+\n')
    f.write(tabla)
    f.write('\n')
    f.write('+----------------------------------------------------------------------------------+\n')
    f.write('\n')
    f.write('\tNOTA:\n'
            '\tLos parámetros de diseño se comparan de la siguiente manera:\n'
            '\tCOS --> Calculado >= Proyecto = Correcto\n'
            '\tCAS --> Calculado <= Proyecto = Correcto\n'
            '\tCUS --> Calculado >= Proyecto = Correcto\n'
            )

    f.write('\n\n')
    f.write('\t<-- Fin del Reporte -->')
    f.write('\n')

    f.close()

    messagebox.showinfo(message='Se creó el archivo "reporte.txt" dentro de la carpeta del programa.\n\n'
                        'Cada vez que se crea un archivo de reporte, el nuevo sustituye al anterior.\n\n'
                        'Para conservar el actual, renombra el archivo o cámbialo de ubicación.',
                        title='¡ A V I S O !'
                        )

    # Abrir con Bloc de Notas
    txtfile = "reporte.txt"
    notepadPath = r'C:\WINDOWS\system32\notepad.exe'
    subprocess.Popen("%s %s" % (notepadPath, txtfile))


def calculos(*args):  # Calcular el Coeficientes
    try:
        var1 = float(s_ter.get())
        var2 = float(s_cons.get())
        vcos = float(f_cos.get())
        vcas = float(f_cas.get())
        vcus = float(f_cus.get())
        vabs = float(s_abso.get())
        vctk = float(s_cont.get())
        res_cos.set(vcos * var1)
        res_cas.set(vcas * var1)
        res_cus.set(var2 / var1)
        flt_cos = float(res_cos.get())
        dsp_cos.set(round(flt_cos, 2))  # Para mostrar resultado en dos decimales
        dsp_f_cos.set(round(vcos, 2))
        flt_cas = float(res_cas.get())
        dsp_cas.set(round(flt_cas, 2))  # Para mostrar resultado en dos decimales
        dsp_f_cas.set(round(vcas, 2))
        flt_cus = float(res_cus.get())
        dsp_cus.set(round(flt_cus, 2))  # Para mostrar resultado en dos decimales
        dsp_f_cus.set(round(vcus, 2))  # Para mostrar resultado en dos decimales
        dsp_s_abso.set(round(vabs, 2))  # Para mostrar resultado en dos decimales
        dsp_s_cont.set(round(vctk, 2))  # Para mostrar resultado en dos decimales

        if flt_cos <= vctk:
            stat_cos.set('Ajustar')
        else:
            stat_cos.set('Correcto')

        if flt_cas >= vabs:
            stat_cas.set('Ajustar')
        else:
            stat_cas.set('Correcto')

        if flt_cus >= vcus:
            stat_cus.set('Ajustar')
        else:
            stat_cus.set('Correcto')

    except ValueError:
        pass


root = Tk()  # Establece ventana principal
root.title('PadARQ - Revisión de Parámetros de Diseño Arquitectónico')
root.minsize(790, 410)
root.maxsize(790, 410)
appHighlightFont = font.Font(family='Arial', size=10, weight='bold')

n_proy = StringVar()  # Variables para cálculos y datos generales
n_cli = StringVar()
f_cos = StringVar()
f_cas = StringVar()
f_cus = StringVar()
s_ter = StringVar()
s_cons = StringVar()
s_cont = StringVar()
s_abso = StringVar()
res_cos = StringVar()
res_cas = StringVar()
res_cus = StringVar()
stat_cos = StringVar()
stat_cas = StringVar()
stat_cus = StringVar()

dsp_f_cos = DoubleVar()  # Variables para mostrar resultados
dsp_f_cas = DoubleVar()
dsp_f_cus = DoubleVar()
dsp_s_abso = DoubleVar()
dsp_s_cont = DoubleVar()
dsp_cos = DoubleVar()
dsp_cas = DoubleVar()
dsp_cus = DoubleVar()


content = ttk.Frame(root, padding=(3, 3, 12, 12))  # Definición de widgets
datoslbl = ttk.Label(content, text='DATOS DEL PROYECTO', font=appHighlightFont)
proylbl = ttk.Label(content, text='Nombre del Proyecto')
proy = ttk.Entry(content, textvariable=n_proy)
clilbl = ttk.Label(content, text='Nombre del Cliente')
cli = ttk.Entry(content, textvariable=n_cli)
coslbl = ttk.Label(content, text='Factor COS')
cos = ttk.Entry(content, textvariable=f_cos)
caslbl = ttk.Label(content, text='Factor CAS')
cas = ttk.Entry(content, textvariable=f_cas)
cuslbl = ttk.Label(content, text='Factor CUS')
cus = ttk.Entry(content, textvariable=f_cus)
terlbl = ttk.Label(content, text='Sup. de Terreno')
ter = ttk.Entry(content, textvariable=s_ter)
conslbl = ttk.Label(content, text='Sup. de Construcción')
cons = ttk.Entry(content, textvariable=s_cons)
contlbl = ttk.Label(content, text='Sup. de Contacto')
cont = ttk.Entry(content, textvariable=s_cont)
abslbl = ttk.Label(content, text='Sup. de Absorción')
abso = ttk.Entry(content, textvariable=s_abso)
tbllbl = ttk.Label(content, text='\nTABLA DE RESULTADOS', font=appHighlightFont)
tblsep = ttk.Separator(content, orient=HORIZONTAL)
parlbl = ttk.Label(content, text='Parámetro', font=appHighlightFont)
faclbl = ttk.Label(content, text='Factor', font=appHighlightFont)
calclbl = ttk.Label(content, text='Calculado', font=appHighlightFont)
reallbl = ttk.Label(content, text='Proyecto', font=appHighlightFont)
resultllbl = ttk.Label(content, text='Resultado', font=appHighlightFont)
tbcoslbl = ttk.Label(content, text='Coeficiente de Ocupación de Superficie (COS)')
tbcaslbl = ttk.Label(content, text='Coeficiente de Absorción de Superficie (CAS)')
tbcuslbl = ttk.Label(content, text='Coeficiente de Utilización de Superficie (CUS)')

content.grid(column=0, row=0, sticky=(N, S, E, W))  # Distribución de widgets
datoslbl.grid(column=0, row=0, columnspan=5, sticky=(N, W), pady=5, padx=5)
proylbl.grid(column=0, row=1, columnspan=1, sticky=(N, E), pady=5, padx=5)
proy.grid(column=1, row=1, columnspan=6, sticky=(N, E, W), pady=5, padx=5)
clilbl.grid(column=0, row=2, columnspan=1, sticky=(N, E), pady=5, padx=5)
cli.grid(column=1, row=2, columnspan=6, sticky=(N, E, W), pady=5, padx=5)
coslbl.grid(column=0, row=3, columnspan=1, sticky=(N, E), pady=5, padx=5)
cos.grid(column=1, row=3, columnspan=1, sticky=(N, E, W), pady=5, padx=5)
caslbl.grid(column=2, row=3, columnspan=1, sticky=(N, E), pady=5, padx=5)
cas.grid(column=3, row=3, columnspan=1, sticky=(N, E, W), pady=5, padx=5)
cuslbl.grid(column=4, row=3, columnspan=1, sticky=(N, E), pady=5, padx=5)
cus.grid(column=5, row=3, columnspan=1, sticky=(N, E, W), pady=5, padx=5)
terlbl.grid(column=0, row=4, columnspan=1, sticky=(N, E), pady=5, padx=5)
ter.grid(column=1, row=4, columnspan=1, sticky=(N, E, W), pady=5, padx=5)
conslbl.grid(column=2, row=4, columnspan=1, sticky=(N, E), pady=5, padx=5)
cons.grid(column=3, row=4, columnspan=1, sticky=(N, E, W), pady=5, padx=5)
contlbl.grid(column=4, row=4, columnspan=1, sticky=(N, E), pady=5, padx=5)
cont.grid(column=5, row=4, columnspan=1, sticky=(N, E, W), pady=5, padx=5)
abslbl.grid(column=0, row=5, columnspan=1, sticky=(N, E), pady=5, padx=5)
abso.grid(column=1, row=5, columnspan=1, sticky=(N, E, W), pady=5, padx=5)
tbllbl.grid(column=0, row=6, columnspan=5, sticky=(N, W), pady=5, padx=5)

parlbl.grid(column=0, row=7, columnspan=2, sticky=(N, W), pady=5, padx=5)
faclbl.grid(column=2, row=7, columnspan=1, sticky=(N, E), pady=5, padx=5)
calclbl.grid(column=3, row=7, columnspan=1, sticky=(N, E), pady=5, padx=5)
reallbl.grid(column=4, row=7, columnspan=1, sticky=(N, E), pady=5, padx=5)
resultllbl.grid(column=5, row=7, columnspan=1, sticky=(N, E), pady=5, padx=5)
tblsep.grid(column=0, row=8, columnspan=6, sticky=(E, W))

tbcoslbl.grid(column=0, row=9, columnspan=2, sticky=(N, W), pady=5, padx=5)
tbcaslbl.grid(column=0, row=10, columnspan=2, sticky=(N, W), pady=5, padx=5)
tbcuslbl.grid(column=0, row=11, columnspan=2, sticky=(N, W), pady=5, padx=5)
ttk.Label(content, textvariable=dsp_f_cos).grid(column=2, row=9, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=dsp_f_cas).grid(column=2, row=10, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=dsp_f_cus).grid(column=2, row=11, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=dsp_cos).grid(column=3, row=9, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=dsp_cas).grid(column=3, row=10, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=dsp_f_cus).grid(column=3, row=11, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=dsp_s_cont).grid(column=4, row=9, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=dsp_s_abso).grid(column=4, row=10, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=dsp_cus).grid(column=4, row=11, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=stat_cos).grid(column=5, row=9, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=stat_cas).grid(column=5, row=10, columnspan=1, sticky=(N, E), pady=5, padx=5)
ttk.Label(content, textvariable=stat_cus).grid(column=5, row=11, columnspan=1, sticky=(N, E), pady=5, padx=5)

ttk.Label(content, text='').grid(column=0, row=12)  # Botones
ttk.Button(content, text="Calcular", command=calculos).grid(column=5, row=13, columnspan=1, sticky=(E, W), padx=5)
ttk.Button(content, text="Reporte", command=rep).grid(column=4, row=13, columnspan=1, sticky=(E, W))
ttk.Button(content, text="Info...", command=infobox).grid(column=0, row=13, columnspan=1, sticky=(E, W), padx=5)

root.columnconfigure(0, weight=1)  # Configuración general de filas y columnas
root.rowconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.columnconfigure(5, weight=1)

proy.focus()  # Enfoque y comandos de ejecución
root.bind('<Return>', calculos)
root.mainloop()
