import numpy as np
import matplotlib.pyplot as plt


def f1(y1, y2):
    return y2

def f2(y1, y2):
    return 3 * y2 - 2 * y1

# Método de Runge-Kutta de 4to orden para sistemas
def runge_kutta_2nd_order(f1, f2, y1_0, y2_0, t0, t_end, h):
    t_values = [t0]
    y1_values = [y1_0]
    y2_values = [y2_0]
    t = t0
    y1 = y1_0
    y2 = y2_0

    while t < t_end:
        if t + h > t_end:
            h = t_end - t

        # k's para y1
        k1_y1 = h * f1(y1, y2)
        k2_y1 = h * f1(y1 + k1_y1 / 2, y2 + h / 2 * k1_y1)
        k3_y1 = h * f1(y1 + k2_y1 / 2, y2 + h / 2 * k2_y1)
        k4_y1 = h * f1(y1 + k3_y1, y2 + h * k3_y1)

        # k's para y2
        k1_y2 = h * f2(y1, y2)
        k2_y2 = h * f2(y1 + k1_y2 / 2, y2 + h / 2 * k1_y2)
        k3_y2 = h * f2(y1 + k2_y2 / 2, y2 + h / 2 * k2_y2)
        k4_y2 = h * f2(y1 + k3_y2, y2 + h * k3_y2)

        # Actualización de valores
        y1 += (k1_y1 + 2 * k2_y1 + 2 * k3_y1 + k4_y1) / 6
        y2 += (k1_y2 + 2 * k2_y2 + 2 * k3_y2 + k4_y2) / 6
        t += h

        t_values.append(t)
        y1_values.append(y1)
        y2_values.append(y2)

    return t_values, y1_values, y2_values

# Solución analítica
def solucion_analitica(t):
    C1, C2 = 1, -1  # Constantes determinadas por condiciones iniciales
    return C1 * np.exp(t) + C2 * np.exp(2 * t)

# Resolución del sistema
def resolver_edo(y1_0, y2_0, t0, t_end, h):
    # Solución numérica
    t_vals, y1_vals, y2_vals = runge_kutta_2nd_order(f1, f2, y1_0, y2_0, t0, t_end, h)
    
    # Solución analítica
    t_analitica = np.linspace(t0, t_end, 100)
    y_analitica = solucion_analitica(t_analitica)

    # Comparación de resultados
    for t, y1, y2 in zip(t_vals, y1_vals, y2_vals):
        print(f"t = {t:.2f}, y = {y1:.4f}, y' = {y2:.4f}")
    
    # Graficar
    plt.plot(t_vals, y1_vals, label='y(t) - Numérico', marker='o')
    plt.plot(t_analitica, y_analitica, label='y(t) - Analítico', linestyle='--')
    plt.xlabel('t')
    plt.ylabel('Valores de y')
    plt.title('Comparación de Soluciones Numérica y Analítica')
    plt.grid(True)
    plt.legend()
    plt.savefig('graficos/edo_segundo_orden.png')
    plt.show()
