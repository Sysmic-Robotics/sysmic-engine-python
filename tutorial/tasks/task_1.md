# Introduccion - Familiarizacion con el engine

Siguiendo las prácticas vistas en los tutoriales y tareas anteriores, realiza lo siguiente:

## Objetivo :

Crear un código que permita mover a un robot utilizando las flechas del teclado en el simulador grsim.

## Pasos
Con el GrSim abierto sigue los siguientes pasos:

1 Crea un archivo llamado task_1.py dentro de la carpeta python-engine/src.

2 Importa el módulo grsim utilizando:

``` from communications.grsim import Grsim ```

Con el módulo importado, puedes crear un objeto ```Grsim``` y utilizar sus métodos para comunicarte con el simulador. Por ejemplo:

``` 
radio = Grsim() 
radio.communicate_grsim(id=1, isteamyellow=0, velnormal=1)

```

El código anterior hace que el robot 1 del equipo azul se mueva paralelo al eje x. También se puede hacer que se mueva paralelo al eje y con el parámetro ```veltangent```.


3 Ahora, utilizando una biblioteca para detectar la entrada del teclado, preferiblemente la biblioteca **keyboard**, crea un código que permita mover un robot utilizando las cuatro flechas del teclado.

Algunos consejos:

- Si utilizas la biblioteca **keyboard**, es posible que solicite acceso de root. Utiliza sudo -s en la consola para solucionarlo.

4 Con el codigo terminado crea un pull request, recuerda seguir las practicas de la **task_0** 
