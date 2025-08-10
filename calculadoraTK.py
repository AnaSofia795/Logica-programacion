import tkinter 
import math
import re

expr = ""  # expresion del usuario... variable global para que todas las funciones puedan acceder a ella

def limpiar():
    global expr
    expr = ""  #limpiar la expresion
    equa.set(expr) #limpiar la expresion que ve el usuario

def presionar(num):
    global expr 
    expr = expr + str(num)
    equa.set(expr) # mostar la expresion

def calc():
    global expr
    try:   # es para intentar ejecutar el codigo y muestra error en vez de edetenerse
        # Reemplazar "√número" por "math.sqrt(número)"
        expr_eval = re.sub(r"√(\d+(\.\d+)?)", r"math.sqrt(\1)", expr) #explicacion: # r"√(\d+(\.\d+)?)" significa
# √ --------> el simbolo de raiz
# \d+ -------->  uno o mas digitos
# (\.\d+)? --------> punto decimal y mas digitos para numeros con decimales

        ttl = str(eval(expr_eval, {"math": math})) # gauarda la expresion
        equa.set(ttl)
        expr = ttl
    except:
        equa.set("Error")
        expr = ""



#agrgar botones
def aboton(gui):
    #fila 1
    boton_limpiar= tkinter.Button(gui, text="AC", fg="black", bg="#f8acf5",
                                  command=lambda: limpiar(),height=2, width=16)
    boton_limpiar.grid(row=4, column=0, columnspan=3) #aqui se definio el boton para "limpiar" 

    boton_div= tkinter.Button(gui, text="/", fg="black", bg="#f9ffc9",
                                  command=lambda: presionar("/"),height=2, width=4)
    boton_div.grid(row=4, column=3) #aqui se definio el boton para dividir

    #fila2
    
    boton7= tkinter.Button(gui, text="7", fg="black", bg="#fbafca",
                                  command=lambda: presionar(7),height=2, width=4)
    boton7.grid(row=5, column=0) #aqui se definio el boton del num 7
    
    boton8= tkinter.Button(gui, text="8", fg="black", bg="#fbafca",
                                  command=lambda: presionar(8),height=2, width=4)
    boton8.grid(row=5, column=1) #aqui se definio el boton del num 8
    
    boton9= tkinter.Button(gui, text="9", fg="black", bg="#fbafca",
                                  command=lambda: presionar(9),height=2, width=4)
    boton9.grid(row=5, column=2) #aqui se definio el boton del num 9
    
    boton_mult= tkinter.Button(gui, text="*", fg="black", bg="#f9ffc9",
                                  command=lambda: presionar("*"),height=2, width=4)
    boton_mult.grid(row=5, column=3) #aqui se definio el boton de multiplicacion
    #fila3
    boton4= tkinter.Button(gui, text="4", fg="black", bg="#fbafca",
                                  command=lambda: presionar(4),height=2, width=4)
    boton4.grid(row=6, column=0) #aqui se definio el boton del num 4
    
    boton5= tkinter.Button(gui, text="5", fg="black", bg="#fbafca",
                                  command=lambda: presionar(5),height=2, width=4)
    boton5.grid(row=6, column=1) #aqui se definio el boton del num 5
    
    boton6= tkinter.Button(gui, text="6", fg="black", bg="#fbafca",
                                  command=lambda: presionar(6),height=2, width=4)
    boton6.grid(row=6, column=2) #aqui se definio el boton del num 6
    
    boton_res= tkinter.Button(gui, text="-", fg="black", bg="#f9ffc9",
                                  command=lambda: presionar("-"),height=2, width=4)
    boton_res.grid(row=6, column=3) #aqui se definio el boton de resta
    #fila4
    boton1= tkinter.Button(gui, text="1", fg="black", bg="#fbafca",
                                  command=lambda: presionar(1),height=2, width=4)
    boton1.grid(row=7, column=0) #aqui se definio el boton del num 1
    
    boton2= tkinter.Button(gui, text="2", fg="black", bg="#fbafca",
                                  command=lambda: presionar(2),height=2, width=4)
    boton2.grid(row=7, column=1) #aqui se definio el boton del num 2
    
    boton3= tkinter.Button(gui, text="3", fg="black", bg="#fbafca",
                                  command=lambda: presionar(3),height=2, width=4)
    boton3.grid(row=7, column=2) #aqui se definio el boton del num 3
    
    boton_sum= tkinter.Button(gui, text="+", fg="black", bg="#f9ffc9",
                                  command=lambda: presionar("+"),height=2, width=4)
    boton_sum.grid(row=7, column=3) #aqui se definio el boton de suma
#fila5
    boton0= tkinter.Button(gui, text="0", fg="black", bg="#fbafca",
                                  command=lambda: presionar(0),height=2, width=4)
    boton0.grid(row=8, column=0) #aqui se definio el boton 0

    boton_p= tkinter.Button(gui, text=".", fg="black", bg="#f9ffc9",
                                  command=lambda: presionar("."),height=2, width=4)
    boton_p.grid(row=8, column=1) #aqui se definio el boton punto

    boton_rz= tkinter.Button(gui, text="√", fg="black", bg="#f9ffc9",
                                  command=lambda: presionar("√"),height=2, width=4)
    boton_rz.grid(row=8, column=2) #aqui se definio el boton de la raiz
    
    boton_ig= tkinter.Button(gui, text="=", fg="black", bg="#f8acf5",
                                  command=lambda: calc(),height=2, width=4)
    boton_ig.grid(row=8, column=3) #aqui se definio el boton del igual
    

gui = tkinter.Tk() #definir gui
gui.configure(background="#f7cfe4") #cambiar el color del fondo
gui.title("CALCULADORA") #poner titulo
gui.geometry("200x240") #establecer tamaño

#seccion donde van a aparecer los numeros que presione el usuario
equa= tkinter.StringVar() #aqui se almacena la ecuacion
campoexp = tkinter.Entry(gui, textvariable=equa,width=26)
campoexp.grid(columnspan=4) #cuantas columnas queremos que ocupe la barra

aboton(gui) #para ejecutar la funcion de los botones la llamamos

gui.mainloop() #para poder ejecutar