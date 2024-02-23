import turtle
import datetime as dt
import time
tt1=turtle.Turtle()
tt2=turtle.Turtle()
tt1.speed(0)
tt2.speed(0)
tt1.shape()
tt1.hideturtle()
screen = turtle.Screen()  
screen.bgcolor("orange") 
tt1.pensize(6)
tt1.pencolor("white") 
tt1.penup()
tt1.backward(200)
tt1.pendown()
tt1.forward(400)
tt1.left(90)
tt1.forward(100)
tt1.left(90)
tt1.forward(400)
tt1.left(90)
tt1.forward(100)
tt1.hideturtle()
secs = dt.datetime.now().second  
mins = dt.datetime.now().minute  
hrs = dt.datetime.now().hour  
tt2.pensize(3)  
tt2.color('white')  
tt2.penup()  
tt2.goto(-180,80)
tt2.pendown()
for j in range(2):  
   tt2.forward(350)  
   tt2.right(90)  
   tt2.forward(70)  
   tt2.right(90)  
tt2.hideturtle()
while True: 
   tt1.penup()
   tt1.goto(-110,10)
   tt1.pendown()
     
   tt1.hideturtle()  
   tt1.clear()   
   tt1.write(str(hrs).zfill(2)  
            + ":"+str(mins).zfill(2)+":"  
            + str(secs).zfill(2),  
            font=("Callibri Narrow", 40, "bold" ),align="left")  
   time.sleep(1)  
   secs += 1  
   if secs == 60:  
       secs = 0  
       mins += 1  
   if mins == 60:  
       mins = 0  
       hrs += 1  
   if hrs == 13:  
       hrs = 1  
turtle.mainloop()
