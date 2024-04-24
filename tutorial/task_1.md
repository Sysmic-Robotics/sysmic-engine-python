## Introduccion - Familiarizacion con el engine


Siguiendo las practicas vista en los tutoriales y tareas anteriores, haz lo siguiente:


Objetivo:

Crear un codigo que permita mover a un robot con las flechas del teclado en el simulador grsim

1 Crea un archivo task_1.py dentro de la carpeta python-engine/src

2 Importa el modulo grsim utilizando:

``` from communications.grsim import Grsim ```

Con el modulo ya importado puedes crear un objeto ```Grsim ``` y utilizar sus metodos para comunicarte con el simulador, por ejemplo:

``` 
radio = Grsim() 
radio.communicate_grsim(id=1, isteamyellow=0, velnormal=1)

```

El codigo de arriba hace que el robot 1 del equipo azul se mueva paralelo al eje x. Tambien se puede hacer que se mueva paralelo al eje x con el parametro ```veltangent``` 


3 Ahora utilizando una libreria para detectar el input del teclado, de preferencia la libreria ```keyboard```, crea un codigo que permita mover a un robot con las cuatro flechas del teclado.

Algunos tips:

- Si utilizas la libreria keyboard, probablemente te pida acceso root, utiliza ```sudo -s``` en la consola para solucionarlo.

