import pygame
from gpiozero import Servo
from time import sleep

def main():
    
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
                    servo_left.min()
                    servo_right.min()
                    print("Adelante")
                    sleep(0.5)
                
                elif event.key == pygame.K_s:
                    servo_left.max()
                    servo_right.max()
                    print("Atras")
                    sleep(0.5)

                elif event.key == pygame.K_a:
                    servo_left.value = -0.13
                    servo_right.min()
                    print("Izquierda")
                    sleep(0.5)

                elif event.key == pygame.K_d:
                    servo_left.value = -0.13
                    servo_left.min()
                    print("Derecha")
                    sleep(0.5)

                elif event.key == pygame.K_SPACE:
                    servo_left.value = -0.13
                    servo_right.value = -0.15
                    print("Detener")
main()