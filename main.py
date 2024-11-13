from ordenSuperior import f1, f2, resolver_edo
from RungeKutta import resolver_ecuacion


def main():
    opcion = input("¿Que ecuaciòn deseas resolver? \n1. para EDO de primer orden \n2. para EDO de segundo orden transformada a sistema\n ")

    if opcion == "1":
        print("Resolviendo EDO de primer orden (Ejemplo: f(x, y) = x * raizde(y))")

        # Condiciones iniciales para la EDO de primer orden
        x0 = 1   
        y0 = 4    
        x_end = 1.6  
        h = 0.2    
        resolver_ecuacion(x0, y0, x_end, h)

    elif opcion == "2":
        # EDO de segundo orden Ejemplo z'' = 2e^t - 2z' - z
        print("Resolviendo EDO de segundo orden transformada a sistema (Ejemplo: z'' = 2e^t - 2z' - z)")

        # Condiciones iniciales para la EDO de segundo orden
        t0 = 0     
        z0 = 0     
        y0 = 1    
        t_end = 2  
        h = 0.1    
        resolver_edo(t0, z0, y0, t_end, h)

    else:
        print("Opción no válida. Por favor ingresa 1 o 2.")

if __name__ == "__main__":
    main()
