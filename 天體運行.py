import pyautogui
import math

coordinates_x, coordinates_y = pyautogui.size()

coordinates_x /= 2
coordinates_y /= 2

Circle_radius = 300
angle = 0

print('coordinates_x is ' + str(coordinates_x))
print('coordinates_y is ' + str(coordinates_y))

try:
    while True:

        if angle == 360:
            angle = 0
            
        pyautogui.moveTo(coordinates_x + Circle_radius* math.cos(angle/180*3.1415926),
                         coordinates_y + Circle_radius *math.sin(angle/180*3.1415926))
        pyautogui.PAUSE = 0
        
        angle += 1

        x ,y = pyautogui.position()
        positionStr = 'X: '+ str(x).rjust(4) + '  Y: '+ str(y).rjust(4) + '  angle: ' + str(angle).rjust(4)

        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        print('\n')
        
except KeyboardInterrupt:
    print('\nDone')
