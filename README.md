# Resolviendo EDO por medio del Método de Runge-Kutta de 4to Orden

Este proyecto utiliza el **Método de Runge-Kutta de 4to Orden (RK4)** para resolver ecuaciones diferenciales ordinarias (EDO) de segundo orden, transformadas en un sistema de ecuaciones de primer orden.

### Ecuaciones Diferenciales que se Resolverán

El proyecto resuelve las siguientes Ecuaciones Diferenciales Ordinarias (EDO) transformadas a sistemas de primer orden:

1. **EDO de segundo orden:**

   \[
   z''(t) = 2e^t - 2z'(t) - z(t)
   \]
   
   donde:
   - \( z(t) \) es la función que deseamos resolver,
   - \( z'(t) \) es la derivada de \( z(t) \),
   - \( z''(t) \) es la segunda derivada de \( z(t) \).

2. **Sistema de primer orden equivalente:**

   Después de aplicar el cambio de variable \( y(t) = z'(t) \), la ecuación de segundo orden se convierte en un sistema de ecuaciones de primer orden:
   
   \[
   y'(t) = 2e^t - 2y(t) - z(t)
   \]
   
   \[
   z'(t) = y(t)
   \]

   Donde ahora tenemos un sistema de dos ecuaciones diferenciales de primer orden para resolver.

### Cómo usar el código

1. **Clonar el repositorio:**

   Si aún no has clonado el repositorio, puedes hacerlo con el siguiente comando:

   ```bash
   git clone https://github.com/DiegoLinares11/Metodo-de-Runge-Kutta-de-4to-Orden-RK4
