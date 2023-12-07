import random 
from PIL import Image, ImageDraw
import math
import numpy as np
import math

#mode = int(input('mode:')) #Считываем номер преобразования. 
#image = Image.open("n\\img0001.png") #Открываем изображение. 
image = Image.open("output2\\img0001.png") #Открываем изображение. 
#image = Image.open("smile_py.png") #Открываем изображение. 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину.
print(width) 
height = image.size[1] #Определяем высоту. 	
print(height)
pix = image.load() #Выгружаем значения пикселей.




  
#a.dot(b)

a = np.array([ [1,4,6], [5,2,7], [3,9,8] ])
b = np.array([ [1,4,6], [5,2,7], [3,9,8] ])

c = a*b
#print(c)



filtr = np.array([ [1,0,-1], [2,0,-2], [1,0,-1] ])

for j in range(height):
    for i in range(width):
        red = pix[i, j][0]
        green = pix[i, j][1]
        blue = pix[i, j][2]
        #print(f"{a},{b},{c}", end=" ")
        if red<10: print(f"  {red},",end="")
        elif red>99: print(f"{red},",end="")
        else: print(f" {red},",end="")
        #if b<10: print(f"  {b},",end="")
        #elif b>99: print(f"{b},",end="")
        #else: print(f" {b},",end="")
        #if c<10: print(f"  {c},",end="")
        #elif c>99: print(f"{c},",end="")
        #else: print(f" {c},",end="")
    print("")





our_step = 3

# Начальные значения
j = 0

# Внешний цикл
while j < height-1:
    i = 0

    # Внутренний цикл
    while i < width-1:
        # Ваш код здесь
        red = pix[i, j][0]
        #if red<10: print(f"  {red},",end="")
        #elif red>99: print(f"{red},",end="")
        #else: print(f" {red},",end="")

        # Увеличиваем счетчик внутреннего цикла на 3
        i += our_step

    # Увеличиваем счетчик внешнего цикла на 3
    j += our_step
    #print("")








a = np.array([ [1,4,6], 
               [5,2,7],
              [3,9,8] ])

#print(a)

sred = np.mean(a)

#print(sred)

summa=0
kolvo = 0

for i in a:
    for j in i:
        summa+=j
        kolvo+=1

sred = summa/kolvo
    
#print(kolvo)
#print(summa)
#print(sred)

result_matrix = np.full((5, 5), sred)


pix = image.load()

i=3
j=3

w = np.array([[pix[i,j][0],pix[i+1,j][0],pix[i+2,j][0]],
[pix[i,j+1][0],pix[i+1,j+1][0],pix[i+2,j+1][0]],
[pix[i,j+2][0],pix[i+1,j+2][0],pix[i+2,j+2][0]]])

print(w)

a = np.mean(w)

a = math.floor(a)

print(a)

filtr = np.array([ [1,0,-1], [2,0,-2], [1,0,-1] ])

w*f


#def svertka(input_image, core_matrix):
    
#filtr = np.array([ [0,0,0], [0,0,0], [0,0,0] ])

