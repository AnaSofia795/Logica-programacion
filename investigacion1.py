import matplotlib.pyplot as plt

# Coordenadas
x = [2, 3, 4, 5, 6, 7, 8,
    9, 10, 11, 10, 9, 8,
    7, 6, 5, 4, 3, 2, 1]

y = [8, 9,10,10, 8.5,10,10,
    9, 8, 7, 6, 5, 4,
    3, 2, 3, 4, 5, 6, 7]

# Puntos
plt.scatter(x, y, color="#FA93AB", s=80)

# lineas que unen los puntos
plt.plot(x + [x[0]], y + [y[0]], color='#FA93AB')

plt.title("Corazón")
plt.show()
