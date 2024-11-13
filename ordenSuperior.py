import numpy as np
import matplotlib.pyplot as plt

# Funciones que representan el sistema de ecuaciones de primer orden
def f1(t, z, y):
    # Ecuación para y' = 2e^t - 2y - z
    return 2 * np.exp(t) - 2 * y - z

def f2(t, z, y):
    # Ecuación para z' = y
    return y

# Condiciones iniciales
t0 = 0   
z0 = 0   
y0 = 1   
t_end = 2  
h = 0.1  

# Función para el método Runge-Kutta de 4to orden
def runge_kutta_4(f1, f2, t0, z0, y0, t_end, h):
    # almacenar los valores de t, z, y
    t_values = [t0]
    z_values = [z0]
    y_values = [y0]
    
    # condiciones iniciales
    t = t0
    z = z0
    y = y0
    
    #  Runge-Kutta para cada paso
    while t < t_end:
        if t + h > t_end:
            break
        
        # Calcular los k1, k2, k3, k4 para z y y
        k1z = h * f2(t, z, y)
        k1y = h * f1(t, z, y)
        
        k2z = h * f2(t + h / 2, z + k1z / 2, y + k1y / 2)
        k2y = h * f1(t + h / 2, z + k1z / 2, y + k1y / 2)
        
        k3z = h * f2(t + h / 2, z + k2z / 2, y + k2y / 2)
        k3y = h * f1(t + h / 2, z + k2z / 2, y + k2y / 2)
        
        k4z = h * f2(t + h, z + k3z, y + k3y)
        k4y = h * f1(t + h, z + k3z, y + k3y)
        
        # Actualizamos los valores de z y y
        z = z + (k1z + 2*k2z + 2*k3z + k4z) / 6
        y = y + (k1y + 2*k2y + 2*k3y + k4y) / 6
        t = t + h
        
        # Almacenamos los resultados
        t_values.append(t)
        z_values.append(z)
        y_values.append(y)

    return t_values, z_values, y_values



# Llamamos a la función Runge-Kutta
t_vals, z_vals, y_vals = runge_kutta_4(f1, f2, t0, z0, y0, t_end, h)

# Imprimimos los resultados
for t, z, y in zip(t_vals, z_vals, y_vals):
    print(f"t = {t:.2f}, z = {z:.4f}, z' = {y:.4f}")

# Graficamos los resultados
plt.plot(t_vals, z_vals, label="z(t)", color='b', marker='o')
plt.plot(t_vals, y_vals, label="z'(t)", color='r', marker='x')
plt.xlabel('t')
plt.ylabel('Valores de z y z\'')
plt.title('Método de Runge-Kutta de 4to Orden - EDO de Orden Superior')
plt.legend()
plt.grid(True)
plt.savefig('graficos/imagen2.png')  # guardarà el gráfico como archivo .png
plt.show()
