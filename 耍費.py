import pyautogui

width, hight = pyautogui.size()
j = 400
width = width/2
hight = hight/2
for i in range(0, 200,10):
    pyautogui.moveTo(width + j,hight + i, duration = 0.001)
    j-=10
    
width = width - i
hight = hight + i

for i in range(0, 200,10):
    pyautogui.moveTo(width + j+20,hight - i, duration = 0.001)
    j-=10

width = width - i
hight = hight - i
for i in range(0, 200,10):
    pyautogui.moveTo(width + j,hight - i, duration = 0.001)
    j+=10
    
width = width + i
hight = hight - i
for i in range(0, 200,10):
    pyautogui.moveTo(width + j,hight + i, duration = 0.001)
    j+=10

width = width + i
hight = hight + i
