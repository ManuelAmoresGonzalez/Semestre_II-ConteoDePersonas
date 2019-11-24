# PeopleCounting
# Primero hay que posicionarse en la carpeta utilizando el comando cd. Ejemplo:
cd C:\Users\Usuario\Downloads\people-counting-opencv

#Luego para ejecturar el programa hay que realizar una serie de comandos escenciales para la ejecución del programa 
#Además hay que seleccionar el video a escanear después del --input, y escoger el nombre del video después del --output
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/nombreDelVideoAEscanear.mp4 --output output/nombreDelVideoLuegoDeRealizarElTracking.avi

#Ejemplo con un video ya existente en la carpeta videos
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/bus1.mp4 --output output/bus1.avi