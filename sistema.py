import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
    return x + 2 * y

def f2(x, y):
    return -3 * x - y

# Método de Runge-Kutta de 4to orden para sistemas
def runge_kutta_system(f1, f2, x0, y0, t0, t_end, h):
    t_values = [t0]
    x_values = [x0]
    y_values = [y0]
    t = t0
    x = x0
    y = y0

    while t < t_end:
        if t + h > t_end:
            h = t_end - t

        # k's para x
        k1_x = h * f1(x, y)
        k2_x = h * f1(x + k1_x / 2, y + h / 2 * k1_x)
        k3_x = h * f1(x + k2_x / 2, y + h / 2 * k2_x)
        k4_x = h * f1(x + k3_x, y + h * k3_x)

        # k's para y
        k1_y = h * f2(x, y)
        k2_y = h * f2(x + k1_y / 2, y + h / 2 * k1_y)
        k3_y = h * f2(x + k2_y / 2, y + h / 2 * k2_y)
        k4_y = h * f2(x + k3_y, y + h * k3_y)

        # Actualización de valores
        x += (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        y += (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        t += h

        t_values.append(t)
        x_values.append(x)
        y_values.append(y)

    return t_values, x_values, y_values

# Solución analítica
def solucion_analitica(t):
    # Solución analítica del sistema
    # Autovalores y autovectores del sistema (calculados aparte)
    lam1, lam2 = -1 + 2j, -1 - 2j
    C1, C2 = 1, -1  # Constantes arbitrarias (dependerán de las condiciones iniciales)

    x = np.real(C1 * np.exp(lam1 * t) + C2 * np.exp(lam2 * t))
    y = np.real(C1 * lam1 * np.exp(lam1 * t) + C2 * lam2 * np.exp(lam2 * t))
    return x, y

# Resolución del sistema
def resolver_sistema(x0, y0, t0, t_end, h):
    # Solución numérica
    t_vals, x_vals, y_vals = runge_kutta_system(f1, f2, x0, y0, t0, t_end, h)
    
    # Solución analítica
    t_analitica = np.linspace(t0, t_end, 100)
    x_analitica, y_analitica = solucion_analitica(t_analitica)

    # Comparación de resultados
    for t, x, y in zip(t_vals, x_vals, y_vals):
        print(f"t = {t:.2f}, x = {x:.4f}, y = {y:.4f}")
    
    # Graficar
    plt.plot(t_vals, x_vals, label='x(t) - Numérico', marker='o')
    plt.plot(t_vals, y_vals, label='y(t) - Numérico', marker='x')
    plt.plot(t_analitica, x_analitica, label='x(t) - Analítico', linestyle='--')
    plt.plot(t_analitica, y_analitica, label='y(t) - Analítico', linestyle=':')
    plt.xlabel('t')
    plt.ylabel('Valores')
    plt.title('Comparación de Soluciones Numérica y Analítica')
    plt.grid(True)
    plt.legend()
    plt.savefig('graficos/comparacion.png')
    plt.show()
