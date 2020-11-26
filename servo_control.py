import pygame
from gpiozero import Servo
from time import sleep

def main():
    
    pygame.init()

    screen = pygame.display.set_mode((800,600))

    servo_left = Servo(17)
    

    while True:
        
        for event in pygame.event.get():
            servo_left.value = -0.13
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    servo_left.min()
                    print("Adelante")
                    sleep(0.5)
                
                elif event.key == pygame.K_s:
                    servo_left.max()
                    print("Atras")
                    sleep(0.5)
                elif event.key == pygame.K_SPACE:
                    servo_left.value = -0.13
                    print("Detener")
                    
            
main()