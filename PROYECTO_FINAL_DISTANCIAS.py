import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# Crear ventana
ventana = tk.Tk()
ventana.title("Gráfica Frame")# titulo
ventana.geometry("600x500") # dimensiones
ventana.configure(bg="#FFC0CB")

# Entradas y etiquetas
tk.Label(ventana, text="Valor X:", bg="#FCB9FC", fg="#3600B5", font=("Century Gothic", 12)).place(x=30, y=30)
entrada_x = tk.Entry(ventana)
entrada_x.place(x=100, y=30)

tk.Label(ventana, text="Valor Y:", bg="#FCB9FC", fg="#3600B5", font=("Century Gothic", 12)).place(x=30, y=70)
entrada_y = tk.Entry(ventana)
entrada_y.place(x=100, y=70)

tk.Label(ventana, text="Valor X2:", bg="#FCB9FC", fg="#3600B5", font=("Century Gothic", 12)).place(x=300, y=30)
entrada_x2 = tk.Entry(ventana)
entrada_x2.place(x=370, y=30)

tk.Label(ventana, text="Valor Y2:", bg="#FCB9FC", fg="#3600B5", font=("Century Gothic", 12)).place(x=300, y=70)
entrada_y2 = tk.Entry(ventana)
entrada_y2.place(x=370, y=70)

### Frame para la gráfica
ancho_px = 400
alto_px = 300
frame_grafica = tk.Frame(ventana, width=ancho_px, height=alto_px, bg="white")
frame_grafica.place(x=100, y=140)

### label para mostar resultados de las operaciones
resultado_label = tk.Label(ventana, text="Resultado: ", bg="#FCB9FC", fg="#3600B5", font=("Century Gothic", 12))
resultado_label.place(x=100, y=420)


### Funciones para suma, resta y multiplicacion

def sumar():
    try:
        x1 = float(entrada_x.get())
        y1 = float(entrada_y.get())
        x2 = float(entrada_x2.get())
        y2 = float(entrada_y2.get())
        resultado = (x1 + x2, y1 + y2)
        print("Suma:", resultado)
        resultado_label.config(text=f"Resultado: {resultado}")  #mostar en ventana

    except ValueError:
        print("Ingresa solo numeros")

def restar():
    try:
        x1 = float(entrada_x.get())
        y1 = float(entrada_y.get())
        x2 = float(entrada_x2.get())
        y2 = float(entrada_y2.get())
        resultado = (x1 - x2, y1 - y2)
        print("Resta:", resultado)
        resultado_label.config(text=f"Resultado: {resultado}")  #mostrar en ventana
    except ValueError:
        print("Ingresa solo numeros")

def multiplicar():
    try:
        x1 = float(entrada_x.get())
        y1 = float(entrada_y.get())
        x2 = float(entrada_x2.get())
        y2 = float(entrada_y2.get())
        resultado = (x1 * x2, y1 * y2)
        print("Multiplicación:", resultado)
        resultado_label.config(text=f"Resultado: {resultado}")  #mostrar en ventana

    except ValueError:
        print("Ingresa solo numeros")


### Función para graficar
def graficar():
    try:
        x1 = float(entrada_x.get())
        y1 = float(entrada_y.get())

        x2 = float(entrada_x2.get())
        y2 = float(entrada_y2.get())
        # Limpiar gráfica anterior
        for widget in frame_grafica.winfo_children():
            widget.destroy()
        # Convertir tamaño del frame de píxeles a pulgadas (100 dpi por defecto)
        dpi = 100
        ancho_pulg = ancho_px / dpi
        alto_pulg = alto_px / dpi

        # Crear figura con tamaño ajustado
        fig = plt.figure(figsize=(ancho_pulg, alto_pulg), dpi=dpi)
        plt.plot([x1, x2], [y1, y2], marker='o', color="#CE1276")
        plt.title("Punto ingresado")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        # Mostrar figura en Frame
        canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=0, width=ancho_px, height=alto_px)
    except ValueError:
        print("Ingresa solo números.")

#### Botón
tk.Button(ventana, text="Graficar", command=graficar, bg="#FFF7A0", fg="#CE1276", font=("Century Gothic", 12)).place(x=250, y=100)
tk.Button(ventana, text="Sumar", command=sumar,bg="#FFF7A0", fg="#CE1276", font=("Century Gothic", 12)).place(x=100, y=450)
tk.Button(ventana, text="Restar", command=restar,bg="#FFF7A0", fg="#CE1276", font=("SCentury Gothic", 12)).place(x=200, y=450)
tk.Button(ventana, text="Multiplicar", command=multiplicar,bg="#FFF7A0", fg="#CE1276", font=("Century Gothic", 12)).place(x=300, y=450)


ventana.mainloop()
