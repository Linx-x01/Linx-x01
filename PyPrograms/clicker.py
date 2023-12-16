import pyautogui as pu
import time
# my clicker function
def clicker():
  button = input("Do u want key or mouse? k/m: ")
  if button == 'k':
      key = input("What key?: ")
  clicks = int(input("How Many Clicks Do U Want?: "))
  q2 = input("Do U Want A Delay y/n: ")

  if q2 == 'y':
      Delay = float(input("How Much Delay For Every Click (in seconds)?: "))
  else:
      Delay = 0

  start = input("'yes' To Start: ")
  if start == 'yes':
      print("3")
      time.sleep(1)
      print("2")
      time.sleep(1)
      print("1")
      time.sleep(1)
      print("")

      if button == 'm':
        for _ in range(clicks):
            pu.click()
            time.sleep(Delay)
      elif button == 'k':
        for _ in range(clicks):
            pu.press(key)
            time.sleep(Delay)

print("""\033[34m   ___ _ _    _           
  / __| (_)__| |_____ _ _ 
 | (__| | / _| / / -_) '_|
  \___|_|_\__|_\_\___|_|  
                          \033[0m""")

while True:
  clicker()