import pygame
import time
from pynput import mouse
from pynput import keyboard

pygame.init()
pygame.joystick.init()
controller=pygame.joystick.Joystick(0)
controller.init()

last_activity = time.time()
is_rattling = False

def resetTimer(*args):
  global last_activity, is_rattling
  last_activity = time.time()
  if is_rattling:
    controller.stop_rumble()
    is_rattling = False

mouseListener = mouse.Listener(on_move=resetTimer, on_click=resetTimer)
keyboardListener = keyboard.Listener(on_press=resetTimer)

mouseListener.start()
keyboardListener.start()

try:
  while True:
    currentTime = time.time()
    noActivity = currentTime - last_activity

    if noActivity >= 1:
      is_rattling = True
      controller.rumble(0.5, 0.5, 200)
    time.sleep(0.1)
except KeyboardInterrupt:
  print("khalas")