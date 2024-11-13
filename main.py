# Método de Runge-Kutta de 4to Orden (RK4) # 
import numpy as np

# Condiciones iniciales
x0 = 1  
y0 = 4  
x_end = 1.6  
h = 0.2 

# Función a probar de la forma x * raizdeY
def f(x, y):
    return x * np.sqrt(y)


def runge_kutta(f, x0, y0, x_end, h):
    #para almacenar los valores de x y y
    x_values = [x0]
    y_values = [y0]

    # Comenzamos en las condiciones inicales
    x = x0
    y = y0

    while x <= x_end:

        # Lo podriamos poner si no queremos que el limite no supere al x_end
        #if x + h > x_end:
         #   break 

        # Calculamos los k's
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)

        # Actualizamos el valor de y y de x 
        y = y + 1/6 * (k1 + 2*k2 + 2*k3 + k4) * h
        x = x + h
        
        # Almacenamos los valores de y y x
        y_values.append(y)
        x_values.append(x)


    return x_values, y_values

x_vals, y_vals = runge_kutta(f, x0, y0, x_end, h)

# Imprimimos los resultados
for x, y in zip(x_vals, y_vals):
    print(f"x = {x:.2f}, y = {y:.4f}")
