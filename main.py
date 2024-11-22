from ordenSuperior import f1, f2, resolver_edo
from RungeKutta import resolver_ecuacion
from sistema import resolver_sistema 

def main():
    opcion = input("¿Que ecuaciòn deseas resolver? \n1. para EDO de primer orden \n2. para EDO de segundo orden transformada a sistema\n3. Sistema de ecuaciones")

    if opcion == "1":

        # Condiciones iniciales para la EDO de primer orden
        x0 = 1   
        y0 = 4    
        x_end = 50  
        h = 0.1    
        resolver_ecuacion(x0, y0, x_end, h)

    elif opcion == "2":

        # Condiciones iniciales para la EDO de segundo orden
        t0 = 0     
        z0 = 0     
        y0 = 1    
        t_end = 50  
        h = 0.1    
        resolver_edo(t0, z0, y0, t_end, h)
    elif opcion == "3":
        x0 = 1
        y0 = 4
        t0 = 0
        t_end = 50
        h = 0.1
        resolver_sistema(x0,y0,t0,t_end,h)
    else:
        print("Opción no válida. Por favor ingresa 1 o 2.")

if __name__ == "__main__":
    main()
