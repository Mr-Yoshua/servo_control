import cv2
import numpy as np
from pyzbar.pyzbar import decode
import json
import pygame
import pygame.camera
import time
from gpiozero import Servo

def cleanRoute():
    return []

def ReadQR():

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)  
    arr_ruta = []
    while True:
        ## mientras se pueda acceder a camara leer codigo QR desde camara, qr data es el contenido pts es para crear un cuadrado que limita el QR que se obtienen las dim desde
        # los datos de lectura, se utiliza para esta accion numpy
        success,img = cap.read()
        for barcode in decode(img):
            
            qrdata = barcode.data.decode('utf-8')
            
            dataexample = qrdata.replace("'",'"')
            
            final_data = json.loads(dataexample)
           
            nombre_lectura = final_data["nombrePaciente"]
            box_lectura = final_data["numeroBox"]
            ruta_lectura = final_data["ruta"]
            arr_ruta = ruta_lectura.split(',')
            print("Ruta :" + arr_ruta[0])
            #Settings para proyectar en pantalla
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(0,0,255),5)
            pts2 = barcode.rect
            #print(pts2[0])
            cv2.putText(img,('Box : ' + str(box_lectura)),(pts2[0],pts2[1]-60),cv2.FONT_HERSHEY_SIMPLEX,0.9,(57,255,20),2)
            cv2.putText(img,('Paciente : ' +nombre_lectura),(pts2[0],pts2[1]-20),cv2.FONT_HERSHEY_SIMPLEX,0.9,(57,255,20),2)
            # return 
        cv2.imshow('Result',img)
        if len(arr_ruta) != 0 :
                desplazar(arr_ruta)
                arr_ruta = cleanRoute()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            cv2.destroyAllWindows()
        
      
def desplazar(arr_ruta):
    print(arr_ruta)
    for event in arr_ruta: 
        if event == 'w':
            servo_left.max()
            servo_right.min()
            print("Adelante")
            time.sleep(0.5)
        
        elif event == 's':
            print("Atras")
            servo_left.min()
            servo_right.max()
            time.sleep(0.5)
            
        elif event == 'a':
            print("Izquierda")
            servo_left.min()
            servo_right.min()
            time.sleep(0.5)
            
        elif 'd':
            print("Derecha")
            servo_right.max()
            servo_left.max()
            time.sleep(0.5)
    print("Ruta Terminada :)")

def controlDistancia():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    servo_left = Servo(17)
    servo_right = Servo(18)
    
    while True:    
        for event in pygame.event.get():
            servo_left.value = -0.13
            servo_right.value = -0.15
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    servo_left.max()
                    servo_right.min()
                    print("Adelante")
                    sleep(0.5)
                
                elif event.key == pygame.K_s:
                    servo_left.min()
                    servo_right.max()
                    print("Atras")
                    sleep(0.5)
                    
                elif event.key == pygame.K_a:
                    #servo_left.value = -0.15
                    servo_left.min()
                    servo_right.min()
                    print("Izquierda")
                    sleep(0.5)
                    
                elif event.key == pygame.K_d:
                    #servo_left.value = -0.13
                    servo_right.max()
                    servo_left.max()
                    print("Derecha")
                    sleep(0.5)
                    
                elif event.key == pygame.K_SPACE:
                    servo_left.value = -0.13
                    servo_right.value = -0.20
                    print("Detener")


ReadQR();
