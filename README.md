# PeopleCounting
***El proyecto tiene como fin automatizar el proceso del conteo de pasajeros en el transporte público mediante la implementación de la librería OpenCV***

El programa ha sido ejecutado en la terminal de Anaconda y de Pycharm, para ejecutar el programa seguir el tutorial paso a paso:

# ¿Cómo instalar las librerías?
*Si al correr el programa (run, F5...) manda una excepción debido a una librería, abrir el CMD y utilizar el comando "pip install " seguido del nombre de la librería que da error, en caso de no ser así, googlear cómo instalar librería que nos da problemas, googlear cómo instalar pip en caso de error por el pip*

# ¿Cómo ejecutar el programa?

*Primero se abre la terminal del editor de texto preferido, para ejecutarlo es necesario posicionarse en la carpeta utilizando el comando cd y moviendo la carpeta a la terminal. Ejemplo:*
cd C:\Users\Usuario\Downloads\people-counting-opencv

*Luego, para ejecturar el programa hay que realizar una serie de comandos escenciales para la ejecución del programa 
Además hay que seleccionar el video a escanear después del --input, y escoger el nombre del video después del --output. Comando a ejecutar en la terminal editando el nombre del video:*
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/nombreDelVideoAEscanear.mp4 --output output/nombreDelVideoLuegoDeRealizarElTracking.avi

*Ejemplo con un video ya existente en la carpeta videos*
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/escaleras.mp4 --output output/escaleras.avi