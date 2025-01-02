from tkinter import*#IMPORTAMOS LIBRERIA TKINTER 
from os import remove

import linecache
import aspose.words as aw

continuas_cursos = [["arquitectura/continuas.txt","arquitectura/continuas2.txt","arquitectura/continuas3.txt"],
                    ["calculo/continuas.txt","calculo/continuas2.txt","calculo/continuas3.txt"],
                    ["cc/continuas.txt","cc/continuas2.txt","cc/continuas3.txt"],
                    ["dbp/continuas.txt","dbp/continuas2.txt","dbp/continuas3.txt"],
                    ["interdisciplinar/continuas.txt","interdisciplinar/continuas2.txt","interdisciplinar/continuas3.txt"],
                    ["ingles/continuas.txt","ingles/continuas2.txt","ingles/continuas3.txt"],
                    ["ciudadania/continuas.txt","ciudadania/continuas2.txt","ciudadania/continuas3.txt"]]

parciales_cursos = [["arquitectura/parciales.txt","arquitectura/parciales2.txt","arquitectura/parciales3.txt"],
                    ["calculo/parciales.txt","calculo/parciales2.txt","calculo/parciales3.txt"],
                    ["cc/parciales.txt","cc/parciales2.txt","cc/parciales3.txt"],
                    ["dbp/parciales.txt","dbp/parciales2.txt","dbp/parciales3.txt"],
                    ["interdisciplinar/parciales.txt","interdisciplinar/parciales2.txt","interdisciplinar/parciales3.txt"],
                    ["ingles/parciales.txt","ingles/parciales2.txt","ingles/parciales3.txt"],
                    ["ciudadania/parciales.txt","ciudadania/parciales2.txt","ciudadania/parciales3.txt"]]

auxiliar_cursos = [["arquitectura/auxiliar.txt","arquitectura/auxiliar2.txt"],
                   ["calculo/auxiliar.txt","calculo/auxiliar2.txt"],
                   ["cc/auxiliar.txt","cc/auxiliar2.txt"],
                   ["dbp/auxiliar.txt","dbp/auxiliar2.txt"],
                   ["interdisciplinar/auxiliar.txt","interdisciplinar/auxiliar2.txt"],
                   ["ingles/auxiliar.txt","ingles/auxiliar2.txt"],
                   ["ciudadania/auxiliar.txt","ciudadania/auxiliar2.txt"]]

notas_finales_cursos = ["arquitectura/Notas_Finales.txt","calculo/Notas_Finales.txt","cc/Notas_Finales.txt","dbp/Notas_Finales.txt",
                        "interdisciplinar/Notas_Finales.txt","ingles/Notas_Finales.txt","ciudadania/Notas_Finales.txt"]

notas_cursos = ["arquitectura/notas_finales2.txt","calculo/notas_finales2.txt","cc/notas_finales2.txt","dbp/notas_finales2.txt",
                "interdisciplinar/notas_finales2.txt","ingles/notas_finales2.txt","ciudadania/notas_finales2.txt"]

informes_cursos = ["arquitectura/Informe_Notas_Finales_Arquitectura.pdf","calculo/Informe_Notas_Finales_Calculo.pdf",
                   "cc/Informe_Notas_Finales_Ciencias_de_la_Computación.pdf","dbp/Informe_Notas_Finales_Desarrollo_Basado_en_Plataformas.pdf",
                   "interdisciplinar/Informe_Notas_Finales_Trabajo_Interdisciplinar.pdf","ingles/Informe_Notas_Finales_Inglés_Tecnino_III.pdf",
                   "ciudadania/Informe_Notas_Finales_Ciudadania.pdf"]

def txt_notas(curso):
    notas_info = nota_continua.get()
    comp=linecache.getline(auxiliar_cursos[curso][0],1).strip()
    if(int(comp)==0):
        file1 = open(continuas_cursos[curso][0],"a")
        file1.write(notas_info)
        file1.write("\n")
        file1.close()
        file_c=open(auxiliar_cursos[curso][0],"w")
        file_c.write(str(1))
        file_c.close()
    if(int(comp)==1):
        file2 = open(continuas_cursos[curso][1],"a")
        file2.write(notas_info)
        file2.write("\n")
        file2.close()
        file_c=open(auxiliar_cursos[curso][0],"w")
        file_c.write(str(2))
        file_c.close()
    if(int(comp)==2):
        file3 = open(continuas_cursos[curso][2],"a")
        file3.write(notas_info)
        file3.write("\n")
        file3.close()
        file_c=open(auxiliar_cursos[curso][0],"w")
        file_c.write(str(3))
        file_c.close()


def txt_notas_parciales(curso):
    notas_info = nota_parcial.get()
    comp=linecache.getline(auxiliar_cursos[curso][1],1).strip()
    if(int(comp)==0):
        file1 = open(parciales_cursos[curso][0],"a")
        file1.write(notas_info)
        file1.write("\n")
        file1.close()
        file_c=open(auxiliar_cursos[curso+1],"w")
        file_c.write(str(1))
        file_c.close()
    if(int(comp)==1):
        file2 = open(parciales_cursos[curso][1],"a")
        file2.write(notas_info)
        file2.write("\n")
        file2.close()
        file_c=open(auxiliar_cursos[curso][1],"w")
        file_c.write(str(2))
        file_c.close()
    if(int(comp)==2):
        file3 = open(parciales_cursos[curso][2],"a")
        file3.write(notas_info)
        file3.write("\n")
        file3.close()
        file_c=open(auxiliar_cursos[curso][1],"w")
        file_c.write(str(3))
        file_c.close()



def pdf_notas_final(curso):
    remove(notas_finales_cursos[curso])
    remove(notas_cursos[curso])
    contador_=2
    promedio_final=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    file_min = open("nota_minima.txt","r")
    nota_minima = int(file_min.read())
    file_min.close()
    aprobados=0
    desaprobados=0
    quien_tuvo_mayor_nota=" "
    quien_tuvo_menor_nota=lista_alum[0]
    menor_nota=int(promedio_final[0])
    mayor_nota=int(promedio_final[0])

    
    for i in range (0,39):
        con_1=linecache.getline(continuas_cursos[curso][0],i+1).strip()
        con_2=linecache.getline(continuas_cursos[curso][1],i+1).strip()
        con_3=linecache.getline(continuas_cursos[curso][2],i+1).strip()
        par_1=linecache.getline(parciales_cursos[curso][0],i+1).strip()
        par_2=linecache.getline(parciales_cursos[curso][1],i+1).strip()
        par_3=linecache.getline(parciales_cursos[curso][2],i+1).strip()

        promedio_final[i]=(int(con_1)*0.1)+(int(con_2)*0.1)+(int(con_3)*0.3)+((int(par_1)*0.1)+(int(par_2)*0.1)+(int(par_3)*0.3))
        promedio_final[i]=round(promedio_final[i])
        menor_nota=promedio_final[0]
        file_main = open(notas_finales_cursos[curso],"a")
        file_2 = open(notas_cursos[curso],"a")
        esp=" "
        if(contador_-1==1):
            file_main.write("\nNOTAS DEL CURSO DE" + cursos_mayusc[curso] + ":" +"\n"+"\nAPELLIDOS Y NOMBRES"+"\t\t\t"+"    PROMEDIO"+"\t\n")
        file_main.write(str(contador_-1))
        if(len(lista_alum[contador_-2])<29):
            file_main.write(". "+lista_alum[contador_-2]+esp*(29-len(lista_alum[contador_-2]))+"\t"+"|")
        else:
            file_main.write(". "+lista_alum[contador_-2]+"\t"+"|")
        file_main.write("\t")
        file_main.write(str(promedio_final[i]))
        file_main.write("\t|\n")
        file_2.write(str(promedio_final[i]))
        file_2.write("\n")
        file_main.close()
        file_2.close()

        if(int(promedio_final[i])>=nota_minima):
            aprobados+=1
        if(int(promedio_final[i])<nota_minima):
            desaprobados+=1
        if(int(promedio_final[i])<=menor_nota):
            menor_nota=int(promedio_final[i])
            quien_tuvo_menor_nota=lista_alum[contador_-2]
        if(int(promedio_final[i])>=mayor_nota):
            mayor_nota=int(promedio_final[i])
            quien_tuvo_mayor_nota=str(lista_alum[contador_-2])

        contador_+=1
    file_main = open(notas_finales_cursos[curso],"a")
    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nAlumno con la mayor nota: " + str(quien_tuvo_mayor_nota) + "(" + str(mayor_nota) + ")" + "\n")
    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nAlumno con la menor nota: " + str(quien_tuvo_menor_nota) + "(" + str(menor_nota) + ")" + "\n")
    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nCantidad de alumnos que aprobaron el semestre: " + str(aprobados) + "\n")
    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nCantidad de alumnos que desaprobaron eInforme_Notas_Finalesl semestre: " + str(desaprobados) + "\n")
    file_main.close()    
    file_2.close()
    
    
    doc = aw.Document(notas_finales_cursos[curso])
    doc.save(informes_cursos[curso])

def peligro_jalar():
    contador_=2
    promedio_final=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range (0,38):
        con_1=linecache.getline(continuas_cursos[curso][0],i+1).strip()
        con_2=linecache.getline(continuas_cursos[curso][1],i+1).strip()
        par_1=linecache.getline(parciales_cursos[curso][0],i+1).strip()
        par_2=linecache.getline(parciales_cursos[curso][1],i+1).strip()        

        promedio_final[i]=(((int(con_1)+int(con_2))+(int(par_1)+int(par_2)))/6)
        contador_+=1

    num_peligro=0
    for i in range(0,39,1):
        if(int(promedio_final[i])<=7):
            num_peligro+=1
    
    
    peligro = Tk()#sobrepone la ventana
    peligro.geometry("350x200")#define dimensiones
        
    peligro.title("Abandono de alumnos")#titulo de la ventana
    peligro.resizable(False,False)#hace que tenga un solo tamaño
    peligro.config(background = "#213141")#define fondo
    main_title6 = Label(peligro,text = "Alumnos que pueden jalar", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "200", height = "2")#define label de la ventana
    main_title6.pack()#ajusta los widgets a la ventana
    jalar=Label(peligro,text=num_peligro, font= ("",20))#label del alumno
    jalar.place(x = 150, y = 70)#ubicacion
    aceptar_btn= Button(peligro,text = "Aceptar", width = "13", height = "2",command =lambda:[peligro.destroy()],bg = "#00CD63")
    #imprime boton presencial, (lambda ejecuta funciones en cadena)
    aceptar_btn.place(x = 120, y = 110)#ubicacion en la ventana



#se da variable para poder inicializar
contador2=1
contador3=1

def imprimir(comp):#funcion imprimir
    global contador2,contador3#indicas variable global 
    if(comp==1):
        etiqueta2['text']=lista_alum[contador2]
        contador2+=1
        if(contador2-1==39):
            texto="Fin..."
            etiqueta2['text']==texto
            switch(submit_btn_guardar)
    elif(comp==2):
        etiqueta3['text']=lista_alum[contador3]
        contador3+=1
        if(contador3-1==39):
            texto2="Fin..."
            etiqueta3['text']==texto2
            switch(submit_btn_guardar2)


def salir(var):
    var.destroy()

def switch(comp):
    if(comp["state"]=="normal"):
        comp["state"]="disabled"




#Definimos lista de alumnos

lista_alum=["Apaza Apaza Nelzon Jorge",
"Apaza Quispe Angel Abraham",
"Benavente Aguirre Paolo Daniel",
"Carazas Quispe Alessander Jesus",
"Castillo Sancho Sergio",
"Cayllahua Gutierrez Diego Yampier",
"Ccama Marron Gustavo Alonso",
"Cerpa Garcia Jean Franco",
"Condori Casquino Ebert Luis",
"Davis Coropuna Leon Felipe",
"Escarza Pacori Alexander Raul",
"Gonzales Condori Alejandro Javier",
"Gutierrez Zevallos Jaime José",
"Hualpa Lopez Jose Mauricio",
"Huaman Coaquira Luciana Julissa",
"Lazo Paxi Natalie Marleny",
"Lopez Condori Andrea Del Rosario",
"Lupo Condori Avelino",
"Maldonado Casilla Braulio Nayap",
"Maldonado Parejo Roy Abel",
"Mariños Hilario Princce Yorwin",
"Martínez Choque Aldo Raúl",
"Mayorga Villena Jharold Alonso",
"Mena Quispe Sergio Sebastian Santos",
"Mogollon Caceres Sergio Daniel",
"Montoya Choque Leonardo",
"Nizama Cespedes Juan Carlos Antonio",
"Olazábal Chávez Neill Elverth",
"Pardavé Espinoza Christian",
"Parizaca Mozo Paul Antony",
"Quilca Huamani Bryan",
"Quispe Rojas Javier Wilber",
"Roque Sosa Owen Haziel",
"Ruiz Mamani Eduardo German",
"Sucasaca Chire Edward Henry",
"Taya Yana Samuel Omar",
"Yavar Guillen Roberto Gustavo",
"Zamalloa Molina Sebastian Agenor",
"Zhong Callasi Linghai Joaquin",""]

cursos=["Arquitectura de Computadores","Calculo en varias Variables",
        "Ciencias de la Computacion II","Desarrollo Basado en Plataformas",
        "Trabajo Interdisciplinar","Ingles Tecnico III",
        "Ciudadania e Interculturalidad"]

cursos_mayusc=["ARQUITECTURA DE COMPUTADORES","CALCULO EN VARIAS VARIABLES",
        "CIENCIAS DE LA COMPUTACION II","DESARROLLO BASADO EN PLATAFORMAS",
        "TRABAJO INTERDISCIPLINAR","INGLES TECNICO III",
        "CIUDADANIA E INTERCULTURALIDAD"]

curso=0


def ingresar_notas(boton):
    global curso
    arqui_btn.place_forget()
    calculo_btn.place_forget()
    cc_btn.place_forget()
    dbp_btn.place_forget()
    ti_btn.place_forget()
    ingles_btn.place_forget()
    cei_btn.place_forget()

    main_title['text']=cursos[boton]


    ingreso_notas_label.place(x = 40, y = 70)#ubicacion 

    continua_label.place(x = 40, y = 120)#ubicacion

    nombres_label.place(x = 40, y = 150)#ubicacion

    etiqueta2.place(x = 40, y = 185)#ubicacion

    submit_btn_guardar.place(x = 100, y = 290)#ubicacion

    asistencia_label.place(x = 40, y = 218)#ubicacion

    nota_entry.place(x = 40, y = 250)#ubicacion


    parcial_label.place(x = 280, y = 120)#ubicacion 

    nombres2_label.place(x = 280, y = 150)#ubicacion

    etiqueta3.place(x = 280, y = 185)#ubicacion

    asistencia_label2.place(x = 280, y = 218)#ubicacion

    nota2_entry.place(x = 280, y = 250)#ubicacion

    submit_btn_guardar2.place(x = 310, y = 290)#ubicacion

    button_pdf_final.place(x=40,y=360)

    button_pdf_jalar.place(x=340,y=360)

    curso=int(boton)

#Pantalla principal

mywindow = Tk()#inicia variable de la ventana
mywindow.geometry("500x430")#dimensiones de la ventana
mywindow.title("Registro de Notas")#titulo de la ventana
mywindow.resizable(False,False)#tamaño constante
mywindow.config(background = "#213141")#color de fondo
main_title = Label(text = "Cursos", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")#encabezado de la ventana (widget)
main_title.pack()#ajusta los widgets a la ventana


arqui_btn = Button(mywindow,text = "Arquitectura de Computadores",width="30",height = "2",command =lambda:[ingresar_notas(0)],bg = "#00CD63")
arqui_btn.place(x=140,y=70)#ubicacion

calculo_btn = Button(mywindow,text = "Calculo en varias Variables",width="30",height = "2",command =lambda:[ingresar_notas(1)],bg = "#00CD63")
calculo_btn.place(x=140,y=110)#ubicacion

cc_btn = Button(mywindow,text = "Ciencias de la Computacion II",width="30",height = "2",command =lambda:[ingresar_notas(2)],bg = "#00CD63")
cc_btn.place(x=140,y=150)#ubicacion

dbp_btn = Button(mywindow,text = "Desarrollo Basado en Plataforma",width="30",height = "2",command =lambda:[ingresar_notas(3)],bg = "#00CD63")
dbp_btn.place(x=140,y=190)#ubicacion

ti_btn = Button(mywindow,text = "Trabajo Interdisciplinar",width="30",height = "2",command =lambda:[ingresar_notas(4)],bg = "#00CD63")
ti_btn.place(x=140,y=230)#ubicacion

ingles_btn = Button(mywindow,text = "Ingles Tecnico III",width="30",height = "2",command =lambda:[ingresar_notas(5)],bg = "#00CD63")
ingles_btn.place(x=140,y=270)#ubicacion

cei_btn = Button(mywindow,text = "Ciudadania e Interculturalidad",width="30",height = "2",command =lambda:[ingresar_notas(6)],bg = "#00CD63")
cei_btn.place(x=140,y=310)#ubicacion


#labels

nombre=lista_alum[0]#muestra en pantalla el primer elemento de la lista

#send_data
cerrar_btn = Button(mywindow,text = "Salir",width="10",height = "2",command =lambda:[salir(mywindow)],bg = "#00CD63")#label del boton salir
cerrar_btn.place(x=210,y=360)#ubicacion

#COLUMNA INGRESO DE NOTAS CONTINUAS

ingreso_notas_label = Label(text = "INGRESO DE NOTAS", font = ("Italic", 14,"bold"), bg = "#00FFFF", fg = "red", width = "18", height = "1")#indica label de la ASISTENCIA
#ingreso_notas_label.place(x = 40, y = 70)#ubicacion 

continua_label = Label(text = "CONTINUA:", bg = "#00FFFF",font=("",13))#indica label de la fecha
#continua_label.place(x = 40, y = 120)#ubicacion

nombres_label = Label(text = "Apellidos y Nombres: ", bg = "#00FFFF",font =("",14))#label de nbombres(estetica)
#nombres_label.place(x = 40, y = 150)#ubicacion

etiqueta2=Label (text=nombre, font= ("",12) )#label del alumno
#etiqueta2.place(x = 40, y = 185)#ubicacion

submit_btn_guardar = Button(mywindow,text = "GUARDAR",command =lambda:[imprimir(1),txt_notas(curso)], width = "9", height = "2",bg = "#00CD63")#label del boton guardar
#submit_btn_guardar.place(x = 100, y = 290)#ubicacion

asistencia_label = Label(text = "Nota: ", bg = "#00FFFF",font=("",14))#label de la nota
#asistencia_label.place(x = 40, y = 218)#ubicacion

nota_continua = StringVar()#variable tipo cadena(recibe texto de label nota)
nota_entry = Entry(textvariable = nota_continua, width = "30")#label de entrada 
#nota_entry.place(x = 40, y = 250)#ubicacion


##NOTAS PARCIALES

parcial_label = Label(text = "PARCIAL:", bg = "#00FFFF",font=("",13))#indica label de la fecha
#parcial_label.place(x = 280, y = 120)#ubicacion 

nombres2_label = Label(text = "Apellidos y Nombres: ", bg = "#00FFFF",font =("",14))#label de nbombres(estetica)
#nombres2_label.place(x = 280, y = 150)#ubicacion

etiqueta3=Label(text=nombre, font= ("",12) )#label del alumno
#etiqueta3.place(x = 280, y = 185)#ubicacion

asistencia_label2 = Label(text = "Nota: ", bg = "#00FFFF",font=("",14))#label de la nota
#asistencia_label.place(x = 280, y = 218)#ubicacion

nota_parcial = StringVar()#variable tipo cadena(recibe texto de label nota)
nota2_entry = Entry(textvariable = nota_parcial, width = "30")#label de entrada 
#nota2_entry.place(x = 280, y = 250)#ubicacion

submit_btn_guardar2 = Button(mywindow,text = "GUARDAR",command =lambda:[imprimir(2),txt_notas_parciales(curso)], width = "9", height = "2",bg = "#00CD63")#label del boton guardar
#submit_btn_guardar2.place(x = 310, y = 290)#ubicacion

#PDF

button_pdf_final = Button(mywindow,text="INFORME NOTAS",command=lambda:[pdf_notas_final(curso)],width="16",height="1",bg="#00CD63")
#button_pdf_final.place(x=40,y=360)

#PELIGRO DE JALAR
button_pdf_jalar = Button(mywindow,text="PUEDEN JALAR",command=lambda:[peligro_jalar(curso)],width="16",height="1",bg="#00CD63")
#button_pdf_final.place(x=340,y=360)

mywindow.mainloop()#mantiene el programa en espera hasta que el usuario desea cerrarlo.
#Gracias :D



