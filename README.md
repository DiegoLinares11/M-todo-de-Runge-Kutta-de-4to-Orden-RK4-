# Resolviendo EDO por medio del Método de Runge-Kutta de 4to Orden

Este proyecto utiliza el **Método de Runge-Kutta de 4to Orden (RK4)** para resolver ecuaciones diferenciales ordinarias (EDO) de primer orden.

### Ecuaciones Diferenciales que se Resolveran

Las ecuaciones diferenciales que resolveremos son de la forma:

1. **Ejemplo de ecuación de primer orden:**

   La ecuación de primer orden que resolvemos es:

   \[
   f(x, y) = x * sqrt{y}
   \]

   Donde:
   - \( x \) es la variable independiente,
   - \( y \) es la función que deseamos resolver.

2. **Sistema de primer orden equivalente para EDO de segundo orden:**

   Para resolver EDOs de segundo orden, primero transformamos la ecuación en un sistema de primer orden. Un ejemplo es:

   \[
   z''(t) = 2e^t - 2z'(t) - z(t)
   \]
   
   Usamos el cambio de variable \( y(t) = z'(t) \), lo que nos lleva a un sistema de dos ecuaciones de primer orden:

   \[
   y'(t) = 2e^t - 2y(t) - z(t)
   \]

   \[
   z'(t) = y(t)
   \]

### Cómo usar el código

1. **Clonar el repositorio:**

   Si aún no has clonado el repositorio, puedes hacerlo con el siguiente comando:

   ```bash
   git clone https://github.com/DiegoLinares11/Metodo-de-Runge-Kutta-de-4to-Orden-RK4
