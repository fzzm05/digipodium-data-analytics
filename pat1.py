from turtle import *
speed('fastest')
pensize('3')
for i in range(6):
    pencolor('RED')
    fd(100)

    for i in range(6):
         pencolor('BLACK')
         fd(50)
    
         for i in range (6):
             pencolor('BLUE')
             fd(25)
             lt(360/6)
         lt(360/6)
    lt(360/6) 
             
             
mainloop()