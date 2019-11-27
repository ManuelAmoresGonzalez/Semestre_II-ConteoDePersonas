# PeopleCounting
***El proyecto tiene como fin automatizar el proceso del conteo de pasajeros en el transporte p�blico mediante la implementaci�n de la librer�a OpenCV***

El programa ha sido ejecutado en la terminal de Anaconda y de Pycharm, para ejecutar el programa seguir el tutorial paso a paso:

# �C�mo instalar las librer�as?
*Si al correr el programa (run, F5...) manda una excepci�n debido a una librer�a, abrir el CMD y utilizar el comando "pip install " seguido del nombre de la librer�a que da error, en caso de no ser as�, googlear c�mo instalar librer�a que nos da problemas, googlear c�mo instalar pip en caso de error por el pip*

# �C�mo ejecutar el programa?

*Primero se abre la terminal del editor de texto preferido, para ejecutarlo es necesario posicionarse en la carpeta utilizando el comando cd y moviendo la carpeta a la terminal. Ejemplo:*
cd C:\Users\Usuario\Downloads\people-counting-opencv

*Luego, para ejecturar el programa hay que realizar una serie de comandos escenciales para la ejecuci�n del programa 
Adem�s hay que seleccionar el video a escanear despu�s del --input, y escoger el nombre del video despu�s del --output. Comando a ejecutar en la terminal editando el nombre del video:*
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/nombreDelVideoAEscanear.mp4 --output output/nombreDelVideoLuegoDeRealizarElTracking.avi

*Ejemplo con un video ya existente en la carpeta videos*
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/escaleras.mp4 --output output/escaleras.avi