import tkinter

# Variable para guardar la expresión
expr = ""

def presionar(numero):
    global expr
    expr = expr + str(numero)
    texto.set(expr)

def limpiar():
    global expr
    expr = ""
    texto.set(expr)

def calcular():
    global expr
    try:
        resultado = str(eval(expr))
        texto.set(resultado)
        expr = resultado
    except:
        texto.set("Error")
        expr = ""

# Crear ventana
ventana = tkinter.Tk()
ventana.title("Calculadora")

# Variable para mostrar texto
texto = tkinter.StringVar()

# Caja donde se muestra la expresión o resultado
entrada = tkinter.Entry(ventana, textvariable=texto, width=20)
entrada.grid(row=0, column=0, columnspan=4)

# Botones
boton1 = tkinter.Button(ventana, text="1", command=lambda: presionar(1), width=5)
boton1.grid(row=1, column=0)

boton2 = tkinter.Button(ventana, text="2", command=lambda: presionar(2), width=5)
boton2.grid(row=1, column=1)

boton3 = tkinter.Button(ventana, text="3", command=lambda: presionar(3), width=5)
boton3.grid(row=1, column=2)

boton_mas = tkinter.Button(ventana, text="+", command=lambda: presionar("+"), width=5)
boton_mas.grid(row=1, column=3)

boton4 = tkinter.Button(ventana, text="4", command=lambda: presionar(4), width=5)
boton4.grid(row=2, column=0)

boton5 = tkinter.Button(ventana, text="5", command=lambda: presionar(5), width=5)
boton5.grid(row=2, column=1)

boton6 = tkinter.Button(ventana, text="6", command=lambda: presionar(6), width=5)
boton6.grid(row=2, column=2)

boton_menos = tkinter.Button(ventana, text="-", command=lambda: presionar("-"), width=5)
boton_menos.grid(row=2, column=3)

boton7 = tkinter.Button(ventana, text="7", command=lambda: presionar(7), width=5)
boton7.grid(row=3, column=0)

boton8 = tkinter.Button(ventana, text="8", command=lambda: presionar(8), width=5)
boton8.grid(row=3, column=1)

boton9 = tkinter.Button(ventana, text="9", command=lambda: presionar(9), width=5)
boton9.grid(row=3, column=2)

boton_multiplicar = tkinter.Button(ventana, text="*", command=lambda: presionar("*"), width=5)
boton_multiplicar.grid(row=3, column=3)

boton_limpiar = tkinter.Button(ventana, text="C", command=limpiar, width=5)
boton_limpiar.grid(row=4, column=0)

boton0 = tkinter.Button(ventana, text="0", command=lambda: presionar(0), width=5)
boton0.grid(row=4, column=1)

boton_punto = tkinter.Button(ventana, text=".", command=lambda: presionar("."), width=5)
boton_punto.grid(row=4, column=2)

boton_dividir = tkinter.Button(ventana, text="/", command=lambda: presionar("/"), width=5)
boton_dividir.grid(row=4, column=3)

boton_igual = tkinter.Button(ventana, text="=", command=calcular, width=22)
boton_igual.grid(row=5, column=0, columnspan=4)

ventana.mainloop()
