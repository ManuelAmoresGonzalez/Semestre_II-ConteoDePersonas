# PeopleCounting
***El proyecto tiene como fin automatizar el proceso del conteo de pasajeros en el transporte público mediante la implementación de la librería OpenCV***

El programa ha sido ejecutado en la terminal de Anaconda y de Pycharm, para ejecutar el programa seguir el tutorial paso a paso:

# ¿Cómo instalar las librerías?
*Si al correr el programa (run, F5...) manda una excepción debido a una librería, abrir el CMD y utilizar el comando "pip install " seguido del nombre de la librería que da error, en caso de no ser así, googlear cómo instalar librería que nos da problemas, googlear cómo instalar pip en caso de error por el pip*
# Librerias que deberán instalarse

* Lo primero será instalar el instalador de python el cual es el pip, iniciar instalando pip en el cmd.
* Continuamos con la librería pyimagesearch la cual ayudara en el control de elementos como los son las coordenadas para ubicar la posición y el movimiento en el que se dirige el pasajero.
* Imutils es otra librería muy importante que ayuda en el procesamiento del video que se utilizara para procesar.
* El numpy es una librería que ayuda a ubicar y a recorrer coordenadas, vectores y matrices en un area especifica.
* La libreria delib es una librería encargada de lo que se llama traking, a esto se refiere con el movimiento de objetos de un area a otra.
* Por ultimo y la mas importante es la librería opencv la cual es la encargada de procesar imagenes y visión computarizada.

# ¿Cómo ejecutar el programa?

*Primero se abre la terminal del sistema, para ejecutarlo es necesario posicionarse en la carpeta utilizando el comando cd y moviendo la carpeta a la terminal. Ejemplo:

cd C:\Users\Usuario\Downloads\people-counting-opencv

*Luego, para ejecturar el programa hay que realizar una serie de comandos escenciales para la ejecución del programa 
Además hay que seleccionar el video a escanear después del --input, y escoger el nombre del video después del --output. Comando a ejecutar en la terminal editando el nombre del video:*

python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/nombreDelVideoAEscanear.mp4 --output output/nombreDelVideoLuegoDeRealizarElTracking.avi

*Ejemplo con un video ya existente en la carpeta videos*

python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/escaleras.mp4 --output output/escaleras.avi

Cabe mencionar que se recomienda correr el sistema desde la terminal del id utilizado para Python ya sea PyCharm, Spyder de Anaconda o su id preferido.

