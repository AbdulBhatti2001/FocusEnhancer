import pygame
import time

pygame.init()
pygame.joystick.init()

print("Waiting for connection")

while True:
    # Refresh list of devices
    pygame.joystick.quit()
    pygame.joystick.init()
    
    count = pygame.joystick.get_count() #gets amount of connected deccvices
    
    if count > 0:
        controller = pygame.joystick.Joystick(0)
        controller.init()
        print(f"\n {controller.get_name()}")
        print("Connected successfullay")
        
        try:
            controller.rumble(0.1, 1,0)
            time.sleep(2) 
            print("buzzed")
        except:
            print("connected but (no energy?)")
        break
    
    time.sleep(1)