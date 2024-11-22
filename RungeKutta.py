# Método de Runge-Kutta de 4to Orden (RK4) # 
import numpy as np
import matplotlib.pyplot as plt


# Función de la ecuación diferencial y' + y = e^x
def f(x, y):
    return np.exp(x) - y

# Método de Runge-Kutta de 4to orden
def runge_kutta(f, x0, y0, x_end, h):
    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    while x <= x_end:
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h / 2 * k1)
        k3 = f(x + h / 2, y + h / 2 * k2)
        k4 = f(x + h, y + h * k3)

        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

# Solución analítica de la ecuación diferencial
def solucion_analitica(x):
    # La solución general es y = e^x + Ce^(-x)
    C = 4 - np.exp(1)  # Condición inicial: y(1) = 4
    return np.exp(x) + C * np.exp(-x)

# Resolver la ecuación diferencial y compararla con la solución analítica
def resolver_ecuacion(x0, y0, x_end, h):
    # Solución numérica con Runge-Kutta
    x_vals_rk, y_vals_rk = runge_kutta(f, x0, y0, x_end, h)

    # Solución analítica
    x_vals_analitica = np.linspace(x0, x_end, 100)
    y_vals_analitica = solucion_analitica(x_vals_analitica)

    # Mostrar resultados numéricos
    print("Resultados del método de Runge-Kutta:")
    for x, y in zip(x_vals_rk, y_vals_rk):
        print(f"x = {x:.2f}, y = {y:.4f}")

    # Graficar las soluciones
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals_rk, y_vals_rk, label='Runge-Kutta 4to orden', marker='o', color='b')
    plt.plot(x_vals_analitica, y_vals_analitica, label='Solución analítica', linestyle='--', color='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Comparación de soluciones: Analítica vs Runge-Kutta')
    plt.grid(True)
    plt.legend()
    plt.savefig('imagen1.png')  # Guarda el gráfico en el directorio actual
    plt.show()

